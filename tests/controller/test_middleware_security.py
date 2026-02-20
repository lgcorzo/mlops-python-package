import sys
import os
import pytest
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller.kafka_app import app

def test_middleware_presence():
    """Test that security middlewares are present in the app."""
    middleware_classes = [m.cls for m in app.user_middleware]

    assert CORSMiddleware in middleware_classes, "CORSMiddleware is missing"
    assert TrustedHostMiddleware in middleware_classes, "TrustedHostMiddleware is missing"

def test_middleware_configuration():
    """Test that middlewares are configured correctly."""
    # Find the middleware instances
    cors_middleware = next((m for m in app.user_middleware if m.cls == CORSMiddleware), None)
    trusted_host_middleware = next((m for m in app.user_middleware if m.cls == TrustedHostMiddleware), None)

    assert cors_middleware is not None
    assert trusted_host_middleware is not None

    # Check configurations (based on default env vars)
    # Note: In the sandbox, env vars might be defaults.
    # We can check that arguments were passed.

    # Starlette Middleware stores options in .options or similar, but FastAPI wrapper might hide it.
    # app.user_middleware contains Middleware objects which have .options (dict) or .kwargs (dict).

    # TrustedHostMiddleware
    # The arguments are passed to the __init__ of the middleware class.
    # app.user_middleware stores the Middleware wrapper which holds kwargs.

    assert "allowed_hosts" in trusted_host_middleware.kwargs
    assert trusted_host_middleware.kwargs["allowed_hosts"] == ["*"] # Default

    # CORSMiddleware
    assert "allow_origins" in cors_middleware.kwargs
    assert cors_middleware.kwargs["allow_origins"] == ["*"] # Default
    assert cors_middleware.kwargs["allow_credentials"] is False # Because origins is ["*"]
    assert cors_middleware.kwargs["allow_methods"] == ["*"]
    assert cors_middleware.kwargs["allow_headers"] == ["*"]
