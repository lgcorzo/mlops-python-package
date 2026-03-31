import asyncio
from unittest.mock import MagicMock, patch

import pytest
from fastapi import HTTPException
from regression_model_template.controller.kafka_app import (
    PredictionRequest,
    PredictionService,
    predict,
)


def test_prediction_service_sanitization():
    """Test that PredictionService sanitizes exceptions."""

    # Mock model that raises a sensitive exception
    mock_model = MagicMock()
    sensitive_error = "Connection failed to database at 192.168.1.5 with user admin"
    mock_model.predict.side_effect = Exception(sensitive_error)

    service = PredictionService(model=mock_model)
    request = PredictionRequest()  # Use default values

    # Call predict
    response = service.predict(request)

    # Verify
    assert response.result["error"] == "An error occurred during prediction processing."
    assert sensitive_error not in response.result["error"]
    assert response.result["quality"] == 0
    assert response.result["inference"] == 0


def test_security_headers():
    """Test that the application adds necessary security HTTP headers."""

    async def run_async_test():
        # Since the custom middleware is added via @app.middleware("http"), it's wrapped in BaseHTTPMiddleware.
        # However, because we don't have TestClient, we can directly test the add_security_headers function
        # by passing a mock request and a mock call_next.

        from regression_model_template.controller.kafka_app import add_security_headers
        from fastapi import Response

        mock_request = MagicMock()
        mock_response = Response()

        async def mock_call_next(req):
            return mock_response

        final_response = await add_security_headers(mock_request, mock_call_next)

        headers = final_response.headers
        assert headers.get("X-Content-Type-Options") == "nosniff"
        assert headers.get("X-Frame-Options") == "DENY"
        assert headers.get("Strict-Transport-Security") == "max-age=31536000; includeSubDomains"
        assert headers.get("Content-Security-Policy") == "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net"
        assert "no-store" in headers.get("Cache-Control", "")

    asyncio.run(run_async_test())


def test_predict_endpoint_exception_leak():
    """Test that the predict endpoint does NOT leak exception details."""

    async def run_async_test():
        with patch(
            "regression_model_template.controller.kafka_app.fastapi_kafka_service", create=True
        ) as mock_fastapi_kafka_service:
            # Simulate a sensitive internal error raised by callback (unlikely now with PredictionService, but possible if something else fails)
            sensitive_error_message = "Database connection failed at 192.168.1.100:5432"
            mock_fastapi_kafka_service.prediction_callback.side_effect = Exception(sensitive_error_message)

            # Expect an HTTPException
            with pytest.raises(HTTPException) as excinfo:
                mock_request = MagicMock()
                mock_request.client.host = "127.0.0.1"
                await predict(PredictionRequest(), mock_request)

            # Verify that the sensitive message is leaked in the detail
            assert excinfo.value.status_code == 500
            assert excinfo.value.detail == "Internal Server Error"
            assert excinfo.value.detail != sensitive_error_message

    asyncio.run(run_async_test())
