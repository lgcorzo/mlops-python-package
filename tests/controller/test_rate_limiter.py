import time
from regression_model_template.controller.kafka_app import RateLimiter

def test_rate_limiter_allows_requests_below_limit():
    limiter = RateLimiter(max_requests=2, window_seconds=60, max_tracked_ips=10)
    assert limiter.is_allowed("192.168.1.1") is True
    assert limiter.is_allowed("192.168.1.1") is True

def test_rate_limiter_rejects_requests_above_limit():
    limiter = RateLimiter(max_requests=2, window_seconds=60, max_tracked_ips=10)
    assert limiter.is_allowed("192.168.1.2") is True
    assert limiter.is_allowed("192.168.1.2") is True
    assert limiter.is_allowed("192.168.1.2") is False

def test_rate_limiter_evicts_oldest_ips():
    limiter = RateLimiter(max_requests=5, window_seconds=60, max_tracked_ips=2)
    limiter.is_allowed("IP1")
    limiter.is_allowed("IP2")

    assert list(limiter.tracked_ips.keys()) == ["IP1", "IP2"]

    # Adding a 3rd IP should evict the oldest (IP1)
    limiter.is_allowed("IP3")
    assert list(limiter.tracked_ips.keys()) == ["IP2", "IP3"]
    assert "IP1" not in limiter.tracked_ips

def test_rate_limiter_window_expiration():
    limiter = RateLimiter(max_requests=1, window_seconds=1, max_tracked_ips=10)
    assert limiter.is_allowed("10.0.0.1") is True
    assert limiter.is_allowed("10.0.0.1") is False

    time.sleep(1.1)  # wait for window to expire
    assert limiter.is_allowed("10.0.0.1") is True

def test_rate_limiter_move_to_end_on_access():
    limiter = RateLimiter(max_requests=5, window_seconds=60, max_tracked_ips=2)
    limiter.is_allowed("IP1")
    limiter.is_allowed("IP2")

    # Access IP1 to make it the most recently used
    limiter.is_allowed("IP1")

    # Adding a 3rd IP should evict IP2 since IP1 was just accessed
    limiter.is_allowed("IP3")

    assert "IP2" not in limiter.tracked_ips
    assert list(limiter.tracked_ips.keys()) == ["IP1", "IP3"]
