import pytest
import logging
from unittest.mock import MagicMock
from regression_model_template.controller.kafka_app import PredictionRequest, predict, FastAPIKafkaService
import pandas as pd

# We use the caplog fixture directly, assuming the project configuration for logging doesn't interfere too much.
# If it does, we might need to adjust the logging configuration in the test.


@pytest.mark.asyncio
async def test_predict_log_leakage(caplog):
    """
    Test that the predict endpoint does not log sensitive information at INFO level.
    """
    # Setup sensitive data
    sensitive_value = "SUPER_SECRET_VALUE"
    request_data = {
        "input_data": {
            "dteday": [pd.Timestamp.now().strftime("%Y-%m-%d")],
            "season": [1],
            "yr": [0],
            "mnth": [1],
            "hr": [0],
            "holiday": [False],
            "weekday": [0],
            "workingday": [True],
            "weathersit": [1],
            "temp": [0.5],
            "atemp": [0.5],
            "hum": [0.5],
            "windspeed": [0.2],
            "casual": [0],
            "registered": [0],
            # This field mimics a sensitive field that might be accidentally included
            "password": [sensitive_value],
        }
    }

    # We construct the request manually to bypass potential validation if possible,
    # or just use it as is if Pydantic allows extra fields (it might ignore them or we might be testing what arrives before validation).
    # However, if PredictionRequest is strict, this might raise a validation error.
    # Let's assume for this test we can pass it, or we patch the validation.
    # Actually, Pydantic v2 by default ignores extra fields unless Config.extra is 'forbid'.
    # Let's see if we can instantiate it.

    try:
        request = PredictionRequest(**request_data)
    except Exception:
        # If validation fails, we can't test the logging of the request object inside the function
        # unless we mock the request object itself to look like it has the sensitive data
        # but is valid enough to pass type checking.
        request = MagicMock(spec=PredictionRequest)
        request.input_data = request_data["input_data"]
        request.__str__.return_value = str(request_data)  # Ensure str(request) leaks it
        request.__repr__.return_value = str(request_data)

    # Mock the service
    from regression_model_template.controller.kafka_app import app

    mock_prediction_service = MagicMock()
    mock_prediction_service.predict.return_value = MagicMock(result={"inference": [0.0], "quality": 1.0, "error": ""})
    app.state.prediction_service = mock_prediction_service

    # Configure logging capture
    caplog.set_level(logging.INFO)

    # Call the endpoint
    mock_request = MagicMock()
    mock_request.app = app
    mock_request.client.host = "127.0.0.1"
    await predict(request, mock_request)

    # Check logs for leakage
    # If the sensitive value appears in the INFO logs, this assertion will fail
    # confirming the vulnerability.
    found_leak = False
    for record in caplog.records:
        if sensitive_value in record.message and record.levelno == logging.INFO:
            found_leak = True
            break

    assert not found_leak, f"Sensitive value '{sensitive_value}' was found in INFO logs!"


def test_kafka_consumer_log_leakage(caplog):
    """
    Test that the Kafka consumer processing does not log sensitive information at INFO level.
    """
    # Setup sensitive data
    sensitive_value = "KAFKA_SECRET_VALUE"
    kafka_msg_value = {
        "input_data": {
            "dteday": ["2024-01-01"],
            "season": [1],
            # ... other fields omitted for brevity as we just check if the whole msg is logged
            "password": [sensitive_value],
        }
    }

    # Mock dependencies
    mock_prediction_callback = MagicMock()
    mock_prediction_callback.return_value = MagicMock(result={"inference": [0.0]})

    service = FastAPIKafkaService(
        prediction_callback=mock_prediction_callback, kafka_config={}, input_topic="test", output_topic="test"
    )

    # Mock Kafka message
    mock_msg = MagicMock()
    mock_msg.error.return_value = None
    import json

    mock_msg.value.return_value = json.dumps(kafka_msg_value).encode("utf-8")

    # Configure logging capture
    caplog.set_level(logging.INFO)

    # Call the processing method
    # We mock producer/consumer to avoid network calls, but we want _process_message logic
    service.producer = MagicMock()
    service.consumer = MagicMock()

    service._process_message(mock_msg)

    # Check logs for leakage
    found_leak = False
    for record in caplog.records:
        if sensitive_value in record.message and record.levelno == logging.INFO:
            found_leak = True
            break

    assert not found_leak, f"Sensitive value '{sensitive_value}' was found in Kafka consumer INFO logs!"


def test_kafka_consumer_prediction_result_leakage(caplog):
    """
    Test that the Kafka consumer processing does not log raw prediction result values (inference)
    at any log level, and instead uses a masked/summarized format.
    """
    # Setup prediction result with sensitive mock inference data
    sensitive_inference = [999.88, 777.66, 555.44]

    # Mock dependencies
    mock_prediction_callback = MagicMock()
    mock_prediction_callback.return_value = MagicMock(
        result={"inference": sensitive_inference, "quality": 1.0, "error": None}
    )

    service = FastAPIKafkaService(
        prediction_callback=mock_prediction_callback, kafka_config={}, input_topic="test", output_topic="test"
    )

    # Mock Kafka message with some valid input_data structure
    mock_msg = MagicMock()
    mock_msg.error.return_value = None
    import json

    kafka_msg_value = {
        "input_data": {
            "dteday": ["2024-01-01"],
            "season": [1],
        }
    }
    mock_msg.value.return_value = json.dumps(kafka_msg_value).encode("utf-8")

    # Set log level to DEBUG so we catch all debug log statements
    caplog.set_level(logging.DEBUG)

    # Mock producer/consumer to avoid network calls
    service.producer = MagicMock()
    service.consumer = MagicMock()

    # Process the message
    service._process_message(mock_msg)

    # Check logs for raw inference leakage vs masked logging
    found_raw_leak = False
    found_masked_log = False

    for record in caplog.records:
        # Check if the raw sensitive values are present in any log message
        msg_str = record.message
        if "999.88" in msg_str or "777.66" in msg_str or "555.44" in msg_str:
            found_raw_leak = True

        # Check if our expected masked log message is present
        if "Prediction result:" in msg_str and "<masked_list_len_3>" in msg_str:
            found_masked_log = True

    assert not found_raw_leak, "Sensitive inference values were leaked in the logs!"
    assert found_masked_log, "Masked/summarized prediction log was not found!"
