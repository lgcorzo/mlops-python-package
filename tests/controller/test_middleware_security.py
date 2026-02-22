from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller.kafka_app import app
import os


def test_middleware_security_configuration():
    """Test that CORSMiddleware and TrustedHostMiddleware are configured."""
    middleware_types = [m.cls for m in app.user_middleware]

    # Check if CORSMiddleware is present
    assert CORSMiddleware in middleware_types, "CORSMiddleware should be added to the app."

    # Check if TrustedHostMiddleware is present
    assert TrustedHostMiddleware in middleware_types, "TrustedHostMiddleware should be added to the app."

    # Check configuration (using defaults if env vars are not set)
    # Note: Env vars might affect these checks if set in the test environment.
    # We assume defaults here or modify the test to mock env vars if needed.

    for middleware in app.user_middleware:
        if middleware.cls == CORSMiddleware:
            # Check options - assuming defaults are set to ["*"] if not overridden
            assert middleware.kwargs["allow_origins"] == os.getenv("ALLOWED_ORIGINS", "*").split(
                ","
            ), "CORSMiddleware allow_origins mismatch"
            assert middleware.kwargs["allow_credentials"] is True, "CORSMiddleware allow_credentials mismatch"
            assert middleware.kwargs["allow_methods"] == ["*"], "CORSMiddleware allow_methods mismatch"
            assert middleware.kwargs["allow_headers"] == ["*"], "CORSMiddleware allow_headers mismatch"
        elif middleware.cls == TrustedHostMiddleware:
            # Check options - assuming defaults are set to ["*"] if not overridden
            assert middleware.kwargs["allowed_hosts"] == os.getenv("ALLOWED_HOSTS", "*").split(
                ","
            ), "TrustedHostMiddleware allowed_hosts mismatch"
