"""Latency statistics utilities for Swarm Mode telemetry."""

import math


def compute_latency_stats(samples: list[float]) -> dict[str, float]:
    """Compute min, max, mean, and p95 latency statistics from sample values."""
    if not samples:
        raise ValueError("samples must not be empty")

    ordered = sorted(float(x) for x in samples)
    count = len(ordered)
    p95_index = min(count - 1, max(0, math.ceil(0.95 * count) - 1))

    return {
        "min": ordered[0],
        "max": ordered[-1],
        "mean": sum(ordered) / count,
        "p95": ordered[p95_index],
    }
