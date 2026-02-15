from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller.kafka_app import app


def test_middleware_presence():
    """Test that security middlewares are present in the FastAPI app."""
    middleware_types = [m.cls for m in app.user_middleware]

    # Check for CORSMiddleware
    has_cors = CORSMiddleware in middleware_types

    # Check for TrustedHostMiddleware
    has_trusted_host = TrustedHostMiddleware in middleware_types

    assert has_cors, "CORSMiddleware is missing"
    assert has_trusted_host, "TrustedHostMiddleware is missing"
