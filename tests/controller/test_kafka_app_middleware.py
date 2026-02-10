from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller.kafka_app import app, ALLOWED_ORIGINS, ALLOWED_HOSTS


def test_security_middleware_present():
    """Test that security middleware is added to the FastAPI app."""
    middleware_cls = [m.cls for m in app.user_middleware]

    assert CORSMiddleware in middleware_cls, "CORSMiddleware should be present"
    assert TrustedHostMiddleware in middleware_cls, "TrustedHostMiddleware should be present"


def test_security_middleware_configuration():
    """Test that security middleware is configured correctly."""

    # Check CORSMiddleware config
    cors_middleware = next(m for m in app.user_middleware if m.cls == CORSMiddleware)
    # Starlette Middleware stores args in kwargs
    assert cors_middleware.kwargs["allow_origins"] == ALLOWED_ORIGINS
    assert cors_middleware.kwargs["allow_origins"] == ["*"]  # Default

    # Check TrustedHostMiddleware config
    trusted_host_middleware = next(m for m in app.user_middleware if m.cls == TrustedHostMiddleware)
    assert trusted_host_middleware.kwargs["allowed_hosts"] == ALLOWED_HOSTS
    assert trusted_host_middleware.kwargs["allowed_hosts"] == ["*"]  # Default
