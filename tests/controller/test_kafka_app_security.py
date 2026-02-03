import pytest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from regression_model_template.controller.kafka_app import (
    PredictionRequest,
    predict,
)
import asyncio
import regression_model_template.controller.kafka_app as kafka_app


def test_predict_endpoint_exception_leak():
    """Test that the predict endpoint does NOT leak exception details."""

    async def run_async_test():
        # Initialize the global variable if it's missing, or patch it.
        # Since it might not be initialized, patch with create=True might work,
        # or we can manually set it.

        with patch(
            "regression_model_template.controller.kafka_app.fastapi_kafka_service", create=True
        ) as mock_fastapi_kafka_service:
            # Simulate a sensitive internal error
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
