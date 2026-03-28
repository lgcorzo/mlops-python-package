import pytest
from pydantic import ValidationError

from regression_model_template.controller.kafka_app import MAX_INPUT_ROWS, MAX_INPUT_COLS, PredictionRequest


def test_prediction_request_max_rows():
    """Test that PredictionRequest enforces max rows limit."""

    # Create input with MAX_INPUT_ROWS + 1 rows
    excessive_rows = MAX_INPUT_ROWS + 1
    input_data = {"col1": [i for i in range(excessive_rows)], "col2": [i for i in range(excessive_rows)]}

    with pytest.raises(ValidationError) as excinfo:
        PredictionRequest(input_data=input_data)

    # Check error message
    assert "Input data exceeds maximum limit" in str(excinfo.value)
    assert "rows" in str(excinfo.value)


def test_prediction_request_max_cols():
    """Test that PredictionRequest enforces max cols limit."""

    # Create input with MAX_INPUT_COLS + 1 columns
    excessive_cols = MAX_INPUT_COLS + 1
    input_data = {f"col{i}": [1, 2] for i in range(excessive_cols)}

    with pytest.raises(ValidationError) as excinfo:
        PredictionRequest(input_data=input_data)

    # Check error message
    assert "Input data exceeds maximum limit" in str(excinfo.value)
    assert "columns" in str(excinfo.value)


def test_prediction_request_valid_rows():
    """Test that PredictionRequest accepts valid rows."""

    # Create input with MAX_INPUT_ROWS rows
    valid_rows = MAX_INPUT_ROWS
    input_data = {"col1": [i for i in range(valid_rows)], "col2": [i for i in range(valid_rows)]}

    request = PredictionRequest(input_data=input_data)
    assert len(request.input_data["col1"]) == valid_rows


def test_prediction_request_empty():
    """Test that PredictionRequest rejects empty input."""

    input_data = {}
    # Assuming empty dict triggers validation error for 'empty' check
    # But wait, InputSchema has default value.
    # If I pass explicit empty dict, validation should catch it.

    with pytest.raises(ValidationError) as excinfo:
        PredictionRequest(input_data=input_data)
    assert "Input data cannot be empty" in str(excinfo.value)


def test_prediction_request_inconsistent_lengths():
    """Test that PredictionRequest rejects inconsistent column lengths."""

    input_data = {
        "col1": [1, 2, 3],
        "col2": [1, 2],  # Different length
    }
    with pytest.raises(ValidationError) as excinfo:
        PredictionRequest(input_data=input_data)
    assert "All columns must have the same length" in str(excinfo.value)


@pytest.mark.asyncio
async def test_predict_rate_limiter_uses_proxy_middleware():
    """Test that ProxyHeadersMiddleware correctly modifies the ASGI scope for trusted proxies."""
    from regression_model_template.controller.kafka_app import app
    from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

    proxy_middleware_config = next(m for m in app.user_middleware if m.cls == ProxyHeadersMiddleware)
    assert proxy_middleware_config.kwargs["trusted_hosts"] == ["127.0.0.1"]

    async def mock_app(scope, receive, send):
        pass  # We just want to inspect the scope after middleware

    middleware_instance = ProxyHeadersMiddleware(app=mock_app, trusted_hosts=["10.0.0.1"])

    # Simulate request from a trusted proxy (10.0.0.1) passing a spoofed client (203.0.113.1)
    scope = {
        "type": "http",
        "client": ("10.0.0.1", 12345),
        "headers": [(b"x-forwarded-for", b"203.0.113.1, 198.51.100.1")],
    }

    async def mock_receive():
        return {"type": "http.request"}

    async def mock_send(msg):
        pass

    await middleware_instance(scope, mock_receive, mock_send)

    # Assert the middleware successfully updated the client IP since it trusted the proxy
    # Note: Uvicorn's ProxyHeadersMiddleware sets the client IP to the right-most IP in X-Forwarded-For
    # that is NOT a trusted proxy. Here we only trusted 10.0.0.1, so it picked 198.51.100.1.
    assert scope["client"][0] == "198.51.100.1"

    # Simulate request from an untrusted proxy (192.168.1.1)
    scope_untrusted = {
        "type": "http",
        "client": ("192.168.1.1", 12345),
        "headers": [(b"x-forwarded-for", b"203.0.113.1")],
    }

    await middleware_instance(scope_untrusted, mock_receive, mock_send)

    # Assert the middleware ignored the header and kept the untrusted IP
    assert scope_untrusted["client"][0] == "192.168.1.1"
