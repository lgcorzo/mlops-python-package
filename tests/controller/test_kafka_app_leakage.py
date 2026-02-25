import json
from unittest.mock import MagicMock

from regression_model_template.controller.kafka_app import FastAPIKafkaService


def test_process_message_exception_leakage():
    # Mock dependencies
    mock_producer = MagicMock()
    mock_consumer = MagicMock()

    # Mock callback that raises an exception with sensitive info
    def sensitive_callback(request):
        raise ValueError("Sensitive Database Error: Connection failed with user 'admin'")

    service = FastAPIKafkaService(
        prediction_callback=sensitive_callback, kafka_config={}, input_topic="in", output_topic="out"
    )
    service.producer = mock_producer
    service.consumer = mock_consumer

    # Mock a Kafka message
    mock_msg = MagicMock()
    mock_msg.error.return_value = None
    mock_msg.value.return_value = json.dumps({"input_data": {}}).encode("utf-8")

    # Call _process_message
    service._process_message(mock_msg)

    # Verify what was produced
    assert mock_producer.produce.called
    args, kwargs = mock_producer.produce.call_args
    value = json.loads(kwargs["value"])

    # Check if error is present
    assert "error" in value

    # Check that sensitive info is NOT leaked and generic message is used
    assert "Sensitive Database Error" not in value["error"]
    assert value["error"] == "An error occurred during prediction processing."
