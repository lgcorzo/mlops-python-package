"""Unit tests for swarm_metrics."""


import pytest

from regression_model_template.utils.swarm_metrics import compute_latency_stats


def test_compute_latency_stats_basic() -> None:
    """Verify min, max, mean, and p95 on a 20-element sample."""
    samples = [float(i) for i in range(1, 21)]
    stats = compute_latency_stats(samples)
    assert stats["min"] == 1.0
    assert stats["max"] == 20.0
    assert stats["mean"] == pytest.approx(10.5)
    assert stats["p95"] == 19.0


def test_compute_latency_stats_empty_raises() -> None:
    """Empty sample list must raise ValueError."""
    with pytest.raises(ValueError, match="empty"):
        compute_latency_stats([])
