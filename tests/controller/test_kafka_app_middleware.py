from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller.kafka_app import app

def test_cors_middleware_present():
    """Verify that CORSMiddleware is present in the application."""
    middleware_types = [m.cls for m in app.user_middleware]
    assert CORSMiddleware in middleware_types, "CORSMiddleware should be present"

def test_trusted_host_middleware_present():
    """Verify that TrustedHostMiddleware is present in the application."""
    middleware_types = [m.cls for m in app.user_middleware]
    assert TrustedHostMiddleware in middleware_types, "TrustedHostMiddleware should be present"

def test_cors_configuration_defaults():
    """Verify default CORS configuration."""
    cors_middleware = next((m for m in app.user_middleware if m.cls == CORSMiddleware), None)
    assert cors_middleware is not None

    # By default, we expect allow_origins=["*"] and allow_credentials=False
    assert cors_middleware.kwargs["allow_origins"] == ["*"]
    assert cors_middleware.kwargs["allow_credentials"] is False
    assert cors_middleware.kwargs["allow_methods"] == ["*"]
    assert cors_middleware.kwargs["allow_headers"] == ["*"]

def test_trusted_host_configuration_defaults():
    """Verify default TrustedHost configuration."""
    trusted_host_middleware = next((m for m in app.user_middleware if m.cls == TrustedHostMiddleware), None)
    assert trusted_host_middleware is not None

    # By default, we expect allow_hosts=["*"]
    assert trusted_host_middleware.kwargs["allowed_hosts"] == ["*"]
