from regression_model_template.controller.kafka_app import app
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware


def test_security_middleware_configured():
    """Verify that CORSMiddleware and TrustedHostMiddleware are added to the app."""
    middleware_classes = [m.cls for m in app.user_middleware]

    assert CORSMiddleware in middleware_classes, "CORSMiddleware is missing"
    assert TrustedHostMiddleware in middleware_classes, "TrustedHostMiddleware is missing"

    # Verify configuration
    for middleware in app.user_middleware:
        if middleware.cls == CORSMiddleware:
            # Check kwargs as per Starlette version in this environment
            assert middleware.kwargs["allow_credentials"] is False, "CORSMiddleware should have allow_credentials=False"
            # We expect these to be set to defaults if env vars are not set
            assert middleware.kwargs["allow_origins"] == ["*"], "CORSMiddleware should have default allow_origins=['*']"

        if middleware.cls == TrustedHostMiddleware:
            assert middleware.kwargs["allowed_hosts"] == [
                "*"
            ], "TrustedHostMiddleware should have default allowed_hosts=['*']"
