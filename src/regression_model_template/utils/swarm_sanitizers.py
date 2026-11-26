"""Identifier sanitization utilities for Swarm Mode."""


import re

_INVALID_CHARS_RE = re.compile(r"[^a-z0-9-]+")
_MULTI_HYPHEN_RE = re.compile(r"-{2,}")


def sanitize_identifier(value: str) -> str:
    """Normalize a string into a lowercase alphanumeric+hyphen identifier (<= 64 chars)."""
    cleaned = _INVALID_CHARS_RE.sub("-", value.strip().lower())
    cleaned = _MULTI_HYPHEN_RE.sub("-", cleaned).strip("-")
    cleaned = cleaned[:64].rstrip("-")
    if not cleaned:
        raise ValueError("identifier contains no alphanumeric characters")
    return cleaned
