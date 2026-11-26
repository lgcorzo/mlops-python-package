"""Unit tests for swarm_checksums."""

from regression_model_template.utils.swarm_checksums import sha256_canonical_json


def test_sha256_canonical_json_is_key_order_independent() -> None:
    """Key ordering must not change the resulting SHA-256 digest."""
    d1 = sha256_canonical_json({"b": 2, "a": {"y": 1, "x": 0}})
    d2 = sha256_canonical_json({"a": {"x": 0, "y": 1}, "b": 2})
    assert d1 == d2
    assert len(d1) == 64
