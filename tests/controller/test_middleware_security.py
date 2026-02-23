"""Test middleware security configuration."""

import os
import importlib
from unittest.mock import patch
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import regression_model_template.controller.kafka_app


def test_middleware_configuration():
    """Test that CORSMiddleware and TrustedHostMiddleware are correctly configured."""
    # Ensure we use the default loaded module
    from regression_model_template.controller.kafka_app import app

    middleware_classes = [m.cls for m in app.user_middleware]

    assert TrustedHostMiddleware in middleware_classes
    assert CORSMiddleware in middleware_classes

    for middleware in app.user_middleware:
        if middleware.cls == TrustedHostMiddleware:
            assert middleware.kwargs["allowed_hosts"] == ["*"]
        elif middleware.cls == CORSMiddleware:
            assert middleware.kwargs["allow_origins"] == ["*"]
            assert middleware.kwargs["allow_credentials"] is False
            assert middleware.kwargs["allow_methods"] == ["*"]
            assert middleware.kwargs["allow_headers"] == ["*"]


def test_middleware_env_parsing():
    """Test that environment variables are correctly parsed."""
    with patch.dict(
        os.environ,
        {
            "ALLOWED_HOSTS": "  example.com,  other.com  ",
            "ALLOWED_ORIGINS": "  https://example.com,  https://other.com  ",
        },
    ):
        # Reload the module to pick up new env vars
        importlib.reload(regression_model_template.controller.kafka_app)
        from regression_model_template.controller.kafka_app import app

        for middleware in app.user_middleware:
            if middleware.cls == TrustedHostMiddleware:
                assert middleware.kwargs["allowed_hosts"] == ["example.com", "other.com"]
            elif middleware.cls == CORSMiddleware:
                assert middleware.kwargs["allow_origins"] == ["https://example.com", "https://other.com"]
                assert middleware.kwargs["allow_credentials"] is False

    # Restore the original module state to avoid affecting other tests
    importlib.reload(regression_model_template.controller.kafka_app)
