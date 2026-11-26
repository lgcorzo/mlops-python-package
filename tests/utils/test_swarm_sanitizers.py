"""Unit tests for swarm_sanitizers."""

import pytest

from regression_model_template.utils.swarm_sanitizers import sanitize_identifier

def test_sanitize_identifier_normalizes_and_truncates() -> None:
    """Verify lowercasing, punctuation replacement, and 64-char cap."""
    assert sanitize_identifier("  Swarm_Mode/Lane#01!  ") == "swarm-mode-lane-01"
    long_val = "a" * 80
    assert len(sanitize_identifier(long_val)) == 64

def test_sanitize_identifier_empty_raises() -> None:
    """Identifiers with no alphanumeric characters must raise ValueError."""
    with pytest.raises(ValueError, match="alphanumeric"):
        sanitize_identifier("///---!!!")
