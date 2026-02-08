from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller.kafka_app import app


def test_middleware_configuration():
    """Test that security middleware is correctly configured in the app."""

    # Get all middleware classes
    middleware_classes = [m.cls for m in app.user_middleware]

    # Verify CORSMiddleware is present
    assert CORSMiddleware in middleware_classes, "CORSMiddleware should be present"

    # Verify TrustedHostMiddleware is present
    assert TrustedHostMiddleware in middleware_classes, "TrustedHostMiddleware should be present"

    # Inspect CORSMiddleware configuration
    cors_middleware = next(m for m in app.user_middleware if m.cls == CORSMiddleware)
    # The 'kwargs' dict contains the kwargs passed to the middleware
    assert cors_middleware.kwargs["allow_origins"] == ["*"]
    assert cors_middleware.kwargs["allow_methods"] == ["*"]
    assert cors_middleware.kwargs["allow_headers"] == ["*"]
    assert cors_middleware.kwargs["allow_credentials"] is True

    # Inspect TrustedHostMiddleware configuration
    trusted_host_middleware = next(m for m in app.user_middleware if m.cls == TrustedHostMiddleware)
    assert trusted_host_middleware.kwargs["allowed_hosts"] == ["*"]
