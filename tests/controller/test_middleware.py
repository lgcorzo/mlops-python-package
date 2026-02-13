from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller.kafka_app import app


def test_middleware_configuration():
    """Test that CORS and TrustedHost middlewares are configured."""
    middlewares = [m.cls for m in app.user_middleware]

    # Check for CORSMiddleware
    assert CORSMiddleware in middlewares, "CORSMiddleware is missing"

    # Check for TrustedHostMiddleware
    assert TrustedHostMiddleware in middlewares, "TrustedHostMiddleware is missing"


def test_cors_middleware_options():
    """Test CORSMiddleware configuration details."""
    cors_middleware = next((m for m in app.user_middleware if m.cls == CORSMiddleware), None)
    assert cors_middleware is not None

    # We can inspect the options passed to the middleware
    # Note: In Starlette/FastAPI, middleware options are stored in .kwargs or .options
    # For CORSMiddleware, we expect allow_origins, allow_credentials, etc.

    options = cors_middleware.kwargs
    assert "allow_origins" in options
    assert "allow_methods" in options
    assert "allow_headers" in options
