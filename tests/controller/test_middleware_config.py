from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller import kafka_app
import importlib
import pytest
import os


@pytest.fixture(autouse=True)
def reset_module():
    """Reset module and env vars after each test to prevent state leakage."""
    orig_origins = os.environ.get("ALLOWED_ORIGINS")
    orig_hosts = os.environ.get("ALLOWED_HOSTS")
    yield
    if orig_origins is None:
        os.environ.pop("ALLOWED_ORIGINS", None)
    else:
        os.environ["ALLOWED_ORIGINS"] = orig_origins

    if orig_hosts is None:
        os.environ.pop("ALLOWED_HOSTS", None)
    else:
        os.environ["ALLOWED_HOSTS"] = orig_hosts

    importlib.reload(kafka_app)


def test_middleware_presence():
    """Verify that CORSMiddleware and TrustedHostMiddleware are present."""
    middleware_types = [m.cls for m in kafka_app.app.user_middleware]
    assert CORSMiddleware in middleware_types
    assert TrustedHostMiddleware in middleware_types


def test_cors_default_config():
    """Verify default CORS configuration."""
    # Ensure we are testing with default env vars (which are unset or *)

    # We reload to ensure fresh state
    importlib.reload(kafka_app)

    cors_middleware = next(m for m in kafka_app.app.user_middleware if m.cls == CORSMiddleware)
    kwargs = cors_middleware.kwargs
    print(
        f"DEBUG: kwargs = {kwargs}, env ALLOWED_ORIGINS = {os.environ.get('ALLOWED_ORIGINS')}, kafka_app ALLOWED_ORIGINS = {kafka_app.ALLOWED_ORIGINS}"
    )
    assert kwargs["allow_origins"] == ["*"]
    assert kwargs["allow_credentials"] is False
    assert kwargs["allow_methods"] == ["*"]
    assert kwargs["allow_headers"] == ["*"]


def test_trusted_host_default_config():
    """Verify default TrustedHost configuration."""
    importlib.reload(kafka_app)
    trusted_host_middleware = next(m for m in kafka_app.app.user_middleware if m.cls == TrustedHostMiddleware)
    kwargs = trusted_host_middleware.kwargs
    assert kwargs["allowed_hosts"] == ["*"]


def test_custom_cors_config(monkeypatch):
    """Verify custom CORS configuration via environment variables."""
    monkeypatch.setenv("ALLOWED_ORIGINS", "https://example.com,https://test.com")

    # Reload the module to pick up new env vars
    importlib.reload(kafka_app)

    cors_middleware = next(m for m in kafka_app.app.user_middleware if m.cls == CORSMiddleware)
    kwargs = cors_middleware.kwargs

    assert set(kwargs["allow_origins"]) == {"https://example.com", "https://test.com"}
    # Logic: allow_credentials=True if "*" not in ALLOWED_ORIGINS else False
    assert kwargs["allow_credentials"] is True


def test_custom_trusted_host_config(monkeypatch):
    """Verify custom TrustedHost configuration via environment variables."""
    monkeypatch.setenv("ALLOWED_HOSTS", "api.example.com,localhost")

    # Reload the module to pick up new env vars
    importlib.reload(kafka_app)

    trusted_host_middleware = next(m for m in kafka_app.app.user_middleware if m.cls == TrustedHostMiddleware)
    kwargs = trusted_host_middleware.kwargs

    assert set(kwargs["allowed_hosts"]) == {"api.example.com", "localhost"}
