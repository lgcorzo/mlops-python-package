import pytest
import time
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from regression_model_template.controller.kafka_app import RateLimiter, predict, PredictionRequest


def test_rate_limiter_allowed_requests():
    """Test that requests within the limit are allowed."""
    limiter = RateLimiter(limit=3, window=60, max_ips=10)

    assert limiter.is_allowed("192.168.1.1") is True
    assert limiter.is_allowed("192.168.1.1") is True
    assert limiter.is_allowed("192.168.1.1") is True


def test_rate_limiter_blocked_requests():
    """Test that requests exceeding the limit are blocked."""
    limiter = RateLimiter(limit=2, window=60, max_ips=10)

    assert limiter.is_allowed("10.0.0.1") is True
    assert limiter.is_allowed("10.0.0.1") is True
    assert limiter.is_allowed("10.0.0.1") is False  # 3rd request should be blocked
    assert limiter.is_allowed("10.0.0.1") is False


def test_rate_limiter_window_expiration():
    """Test that requests are allowed again after the window expires."""
    limiter = RateLimiter(limit=1, window=1, max_ips=10)

    assert limiter.is_allowed("172.16.0.1") is True
    assert limiter.is_allowed("172.16.0.1") is False  # Blocked immediately

    # Wait for the window to expire
    with patch("time.time", return_value=time.time() + 1.1):
        assert limiter.is_allowed("172.16.0.1") is True  # Allowed again


def test_rate_limiter_max_ips_eviction():
    """Test that old IPs are evicted when max_ips capacity is reached."""
    limiter = RateLimiter(limit=5, window=60, max_ips=2)

    assert limiter.is_allowed("ip1") is True
    assert limiter.is_allowed("ip2") is True

    # Both are tracked
    assert "ip1" in limiter.requests
    assert "ip2" in limiter.requests

    # Adding a third IP should evict the oldest ('ip1')
    assert limiter.is_allowed("ip3") is True

    assert "ip3" in limiter.requests
    assert "ip2" in limiter.requests
    assert "ip1" not in limiter.requests


@pytest.mark.asyncio
async def test_predict_endpoint_rate_limiting():
    """Test the /predict endpoint integration with RateLimiter."""
    mock_request = MagicMock()
    mock_request.client.host = "127.0.0.2"

    request_data = PredictionRequest()

    with patch("regression_model_template.controller.kafka_app.rate_limiter.is_allowed", return_value=False):
        with pytest.raises(HTTPException) as excinfo:
            await predict(request_data, request=mock_request)

        assert excinfo.value.status_code == 429
        assert excinfo.value.detail == "Too Many Requests"


@pytest.mark.asyncio
async def test_predict_endpoint_success_with_mock():
    """Test the /predict endpoint succeeds if rate limiting passes."""
    mock_request = MagicMock()
    mock_request.client.host = "127.0.0.3"

    request_data = PredictionRequest()

    with (
        patch("regression_model_template.controller.kafka_app.rate_limiter.is_allowed", return_value=True),
        patch("regression_model_template.controller.kafka_app.fastapi_kafka_service") as mock_service,
    ):
        # Mock successful prediction callback
        mock_result = MagicMock()
        mock_result.result = {"inference": [0.0]}
        mock_service.prediction_callback.return_value = mock_result

        # This shouldn't raise any HTTPException for rate limiting
        await predict(request_data, request=mock_request)
