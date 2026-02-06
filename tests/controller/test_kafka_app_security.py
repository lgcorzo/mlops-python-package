import pytest
from unittest.mock import MagicMock, patch
from fastapi import HTTPException
from regression_model_template.controller.kafka_app import (
    PredictionRequest,
    PredictionService,
    predict,
)
import asyncio


def test_prediction_service_sanitization():
    """Test that PredictionService sanitizes exceptions."""

    # Mock model that raises a sensitive exception
    mock_model = MagicMock()
    sensitive_error = "Connection failed to database at 192.168.1.5 with user admin"
    mock_model.predict.side_effect = Exception(sensitive_error)

    service = PredictionService(model=mock_model)
    request = PredictionRequest()  # Use default values

    # Call predict
    response = service.predict(request)

    # Verify
    assert response.result["error"] == "An error occurred during prediction processing."
    assert sensitive_error not in response.result["error"]
    assert response.result["quality"] == 0
    assert response.result["inference"] == 0


def test_predict_endpoint_exception_leak():
    """Test that the predict endpoint does NOT leak exception details."""

    async def run_async_test():
        with patch(
            "regression_model_template.controller.kafka_app.fastapi_kafka_service", create=True
        ) as mock_fastapi_kafka_service:
            # Simulate a sensitive internal error raised by callback (unlikely now with PredictionService, but possible if something else fails)
            sensitive_error_message = "Database connection failed at 192.168.1.100:5432"
            mock_fastapi_kafka_service.prediction_callback.side_effect = Exception(sensitive_error_message)

            # Expect an HTTPException
            with pytest.raises(HTTPException) as excinfo:
                await predict(PredictionRequest())

            # Verify that the sensitive message is leaked in the detail
            assert excinfo.value.status_code == 500
            assert excinfo.value.detail == "Internal Server Error"
            assert excinfo.value.detail != sensitive_error_message

    asyncio.run(run_async_test())
