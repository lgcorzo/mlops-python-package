
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller.kafka_app import app


def test_cors_middleware_present():
    """Test that CORSMiddleware is added to the application."""
    middleware_types = [m.cls for m in app.user_middleware]
    assert CORSMiddleware in middleware_types


def test_trusted_host_middleware_present():
    """Test that TrustedHostMiddleware is added to the application."""
    middleware_types = [m.cls for m in app.user_middleware]
    assert TrustedHostMiddleware in middleware_types


def test_cors_configuration():
    """Test CORSMiddleware configuration."""
    cors_middleware = next(m for m in app.user_middleware if m.cls == CORSMiddleware)
    # In this environment, it might be .kwargs or .options
    kwargs = getattr(cors_middleware, "kwargs", getattr(cors_middleware, "options", {}))

    assert kwargs["allow_origins"] == ["*"]
    assert kwargs["allow_credentials"] is True
    assert kwargs["allow_methods"] == ["*"]
    assert kwargs["allow_headers"] == ["*"]


def test_trusted_host_configuration():
    """Test TrustedHostMiddleware configuration."""
    trusted_host_middleware = next(m for m in app.user_middleware if m.cls == TrustedHostMiddleware)
    kwargs = getattr(trusted_host_middleware, "kwargs", getattr(trusted_host_middleware, "options", {}))

    assert kwargs["allowed_hosts"] == ["*"]
