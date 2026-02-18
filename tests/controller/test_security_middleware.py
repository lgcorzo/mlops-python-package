from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller.kafka_app import app

def test_middleware_presence():
    """Test that security middlewares are present in the FastAPI app."""
    middleware_types = [m.cls for m in app.user_middleware]

    assert CORSMiddleware in middleware_types, "CORSMiddleware should be present"
    assert TrustedHostMiddleware in middleware_types, "TrustedHostMiddleware should be present"

def test_cors_configuration():
    """Test CORS configuration defaults."""
    cors_middleware = next((m for m in app.user_middleware if m.cls == CORSMiddleware), None)
    assert cors_middleware is not None

    # Check .kwargs as per memory instructions (or .options as fallback)
    options = getattr(cors_middleware, "kwargs", getattr(cors_middleware, "options", {}))

    # Default behavior: ALLOWED_ORIGINS env var is "*" (default) -> split(",") -> ["*"]
    assert options["allow_origins"] == ["*"]
    # If origins has "*", allow_credentials should be False
    assert options["allow_credentials"] is False
    assert options["allow_methods"] == ["*"]
    assert options["allow_headers"] == ["*"]

def test_trusted_host_configuration():
    """Test TrustedHost configuration defaults."""
    trusted_host_middleware = next((m for m in app.user_middleware if m.cls == TrustedHostMiddleware), None)
    assert trusted_host_middleware is not None

    options = getattr(trusted_host_middleware, "kwargs", getattr(trusted_host_middleware, "options", {}))
    # Default behavior: ALLOWED_HOSTS env var is "*" (default) -> split(",") -> ["*"]
    assert options["allowed_hosts"] == ["*"]
