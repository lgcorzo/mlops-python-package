from regression_model_template.controller import kafka_app
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import os
from unittest.mock import patch
from importlib import reload
import pytest

def test_middleware_present():
    """Test that security middlewares are correctly added to the FastAPI app with defaults."""
    # Ensure we start with a clean state (defaults)
    reload(kafka_app)
    app = kafka_app.app

    # Create a map of middleware class to the middleware object
    middlewares = {m.cls: m for m in app.user_middleware}

    # Assert CORSMiddleware is present
    assert CORSMiddleware in middlewares, "CORSMiddleware should be added to the app"
    cors_middleware = middlewares[CORSMiddleware]

    # Verify CORS configuration (checking kwargs as per memory instruction)
    assert cors_middleware.kwargs["allow_origins"] == ["*"]
    assert cors_middleware.kwargs["allow_credentials"] is True
    assert cors_middleware.kwargs["allow_methods"] == ["*"]
    assert cors_middleware.kwargs["allow_headers"] == ["*"]

    # Assert TrustedHostMiddleware is present
    assert TrustedHostMiddleware in middlewares, "TrustedHostMiddleware should be added to the app"
    trusted_host_middleware = middlewares[TrustedHostMiddleware]

    # Verify TrustedHost configuration
    assert trusted_host_middleware.kwargs["allowed_hosts"] == ["*"]

def test_middleware_configuration_from_env():
    """Test that middleware configuration respects environment variables."""
    # Set environment variables
    with patch.dict(os.environ, {
        "ALLOWED_ORIGINS": "https://example.com,https://api.example.com",
        "ALLOWED_HOSTS": "example.com,api.example.com"
    }):
        # Reload the module to pick up new env vars
        reload(kafka_app)
        app = kafka_app.app

        middlewares = {m.cls: m for m in app.user_middleware}

        # Verify CORS configuration
        cors_middleware = middlewares[CORSMiddleware]
        assert set(cors_middleware.kwargs["allow_origins"]) == {"https://example.com", "https://api.example.com"}

        # Verify TrustedHost configuration
        trusted_host_middleware = middlewares[TrustedHostMiddleware]
        assert set(trusted_host_middleware.kwargs["allowed_hosts"]) == {"example.com", "api.example.com"}

    # Restore default state for other tests if necessary
    reload(kafka_app)
