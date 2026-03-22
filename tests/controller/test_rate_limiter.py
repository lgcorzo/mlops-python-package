import time
from unittest.mock import patch
from regression_model_template.controller.kafka_app import IPRateLimiter


def test_rate_limiter_allows_requests():
    """Test that the rate limiter allows normal requests within limit."""
    limiter = IPRateLimiter(max_requests=5, window_size=60)

    # Send 5 requests, all should be allowed
    for _ in range(5):
        assert limiter.is_rate_limited("192.168.1.1") is False


def test_rate_limiter_blocks_excessive_requests():
    """Test that the rate limiter blocks requests exceeding the limit."""
    limiter = IPRateLimiter(max_requests=5, window_size=60)

    # Send 5 requests, all should be allowed
    for _ in range(5):
        assert limiter.is_rate_limited("192.168.1.1") is False

    # The 6th request should be blocked
    assert limiter.is_rate_limited("192.168.1.1") is True


def test_rate_limiter_window_expiry():
    """Test that the rate limiter allows requests after the window expires."""
    limiter = IPRateLimiter(max_requests=2, window_size=1)

    # Send 2 requests
    assert limiter.is_rate_limited("192.168.1.2") is False
    assert limiter.is_rate_limited("192.168.1.2") is False

    # The 3rd request is blocked
    assert limiter.is_rate_limited("192.168.1.2") is True

    # Wait for the window to expire
    with patch("time.time", return_value=time.time() + 2):
        # The request should be allowed again
        assert limiter.is_rate_limited("192.168.1.2") is False


def test_rate_limiter_evicts_oldest_ip():
    """Test that the rate limiter evicts the oldest IP when tracking capacity is reached."""
    # Create limiter with capacity of 3 IPs
    limiter = IPRateLimiter(max_tracked_ips=3)

    # Track 3 IPs
    limiter.is_rate_limited("10.0.0.1")
    limiter.is_rate_limited("10.0.0.2")
    limiter.is_rate_limited("10.0.0.3")

    assert "10.0.0.1" in limiter.tracked_ips
    assert "10.0.0.2" in limiter.tracked_ips
    assert "10.0.0.3" in limiter.tracked_ips
    assert len(limiter.tracked_ips) == 3

    # Adding a 4th IP should evict the oldest one ("10.0.0.1")
    limiter.is_rate_limited("10.0.0.4")

    assert "10.0.0.1" not in limiter.tracked_ips
    assert "10.0.0.2" in limiter.tracked_ips
    assert "10.0.0.3" in limiter.tracked_ips
    assert "10.0.0.4" in limiter.tracked_ips
    assert len(limiter.tracked_ips) == 3

    # Updating an existing IP should move it to the end (most recently used)
    limiter.is_rate_limited("10.0.0.2")

    # Now adding another IP should evict "10.0.0.3" since "10.0.0.2" was just accessed
    limiter.is_rate_limited("10.0.0.5")

    assert "10.0.0.3" not in limiter.tracked_ips
    assert "10.0.0.2" in limiter.tracked_ips
    assert "10.0.0.4" in limiter.tracked_ips
    assert "10.0.0.5" in limiter.tracked_ips
    assert len(limiter.tracked_ips) == 3
