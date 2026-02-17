
import pytest
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller.kafka_app import app

def test_middleware_presence():
    """Test that security middlewares are present in the FastAPI app."""
    middleware_types = [m.cls for m in app.user_middleware]

    # Check for CORSMiddleware
    assert CORSMiddleware in middleware_types, "CORSMiddleware is missing"

    # Check for TrustedHostMiddleware
    assert TrustedHostMiddleware in middleware_types, "TrustedHostMiddleware is missing"

def test_cors_configuration():
    """Test that CORSMiddleware is configured correctly with defaults."""
    # Find the CORSMiddleware instance
    cors_middleware = next(m for m in app.user_middleware if m.cls == CORSMiddleware)

    kwargs = cors_middleware.kwargs
    # Default ALLOWED_ORIGINS is "*"
    assert kwargs["allow_origins"] == ["*"]
    # If origins is "*", allow_credentials must be False
    assert kwargs["allow_credentials"] is False
    assert kwargs["allow_methods"] == ["*"]
    assert kwargs["allow_headers"] == ["*"]

def test_trusted_host_configuration():
    """Test that TrustedHostMiddleware is configured correctly with defaults."""
    trusted_host_middleware = next(m for m in app.user_middleware if m.cls == TrustedHostMiddleware)

    kwargs = trusted_host_middleware.kwargs
    # Default ALLOWED_HOSTS is "*"
    assert kwargs["allowed_hosts"] == ["*"]
