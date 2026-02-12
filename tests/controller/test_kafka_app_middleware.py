from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from regression_model_template.controller.kafka_app import app

def test_middleware_configuration():
    middleware_types = [m.cls for m in app.user_middleware]
    assert TrustedHostMiddleware in middleware_types, "TrustedHostMiddleware missing"
    assert CORSMiddleware in middleware_types, "CORSMiddleware missing"
