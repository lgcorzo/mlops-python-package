import json
import pytest
from unittest.mock import MagicMock, patch
from regression_model_template.controller.kafka_app import (
    PredictionRequest,
    PredictionResponse,
    predict,
    FastAPIKafkaService,
)


@pytest.fixture
def mock_kafka_service():
    """Mock the FastAPIKafkaService and its dependencies."""
    mock_prediction_callback = MagicMock()
    # Add valid result structure directly for the callback return
    mock_prediction_callback.return_value = MagicMock(result={"inference": [1.0], "quality": 1.0, "error": None})
    mock_kafka_config = {
        "bootstrap.servers": "test_server:9092",
        "group.id": "test_group",
        "auto.offset.reset": "earliest",
    }
    input_topic = "test_input_topic"
    output_topic = "test_output_topic"

    with patch("regression_model_template.controller.kafka_app.Producer") as mock_producer_class:
        with patch("regression_model_template.controller.kafka_app.Consumer") as mock_consumer_class:
            # Set up the mock producer
            mock_producer = mock_producer_class.return_value

            # Set up the mock consumer
            mock_consumer = mock_consumer_class.return_value

            service = FastAPIKafkaService(
                prediction_callback=mock_prediction_callback,
                kafka_config=mock_kafka_config,
                input_topic=input_topic,
                output_topic=output_topic,
            )

            yield service, mock_producer, mock_consumer


@pytest.mark.asyncio
@patch("regression_model_template.controller.kafka_app.logger")
async def test_predict_endpoint_logging(mock_logger):
    """Test that the HTTP predict endpoint logs correctly using debug and safe info logs."""

    with patch("regression_model_template.controller.kafka_app.fastapi_kafka_service") as mock_fastapi_kafka_service:
        # Provide a valid prediction response
        mock_response = PredictionResponse(result={"inference": [1.0], "quality": 1.0, "error": None})
        mock_fastapi_kafka_service.prediction_callback.return_value = mock_response

        request = PredictionRequest()
        response = await predict(request)

        # Verify the response is returned
        assert response == mock_response

        # Verify debug log was called with the request
        mock_logger.debug.assert_any_call(f"Received HTTP prediction request: {request}")

        # Verify safe info log was called
        expected_cols = len(request.input_data)
        mock_logger.info.assert_any_call(f"Received HTTP prediction request with {expected_cols} columns")

        # Verify debug log was called with the result
        mock_logger.debug.assert_any_call(f"HTTP prediction result: {mock_response}")

        # Verify safe result info log was called
        mock_logger.info.assert_any_call("HTTP prediction request processed successfully with status: success")


@patch("regression_model_template.controller.kafka_app.logger")
def test_kafka_process_message_logging(mock_logger, mock_kafka_service):
    """Test that Kafka consumer logs correctly using debug and safe info logs."""
    service, *_ = mock_kafka_service

    # Create valid input data for PredictionRequest
    valid_input = PredictionRequest().input_data
    kafka_msg_dict = {"input_data": valid_input}

    # Create mock Kafka message
    msg = MagicMock()
    msg.value.return_value = json.dumps(kafka_msg_dict).encode("utf-8")

    # Also set prediction callback result so it doesn't fail on .result access
    service.prediction_callback.return_value = MagicMock(result={"inference": [1.0], "quality": 1.0, "error": None})

    # Mock json.loads directly in the test to avoid complex byte decoding issues
    with patch("json.loads", return_value=kafka_msg_dict):
        service._process_message(msg)

        # Verify debug log was called with the message payload
        mock_logger.debug.assert_any_call(f"kafka Received input  {kafka_msg_dict}")

        # Verify safe info log was called
        expected_cols = len(valid_input)
        mock_logger.info.assert_any_call(f"Kafka received input with {expected_cols} columns")
