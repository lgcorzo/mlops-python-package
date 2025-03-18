"""FastAPI and Kafka Service for Predictions with Logging."""

# %% IMPORTS
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict, Callable
import threading
import uvicorn
import signal
import os
from confluent_kafka import Producer, Consumer, KafkaError
import logging
import json
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


app: FastAPI = FastAPI()

# Define Pydantic models *outside* the class AND before it.
class PredictionRequest(BaseModel):
    """Request model for prediction."""
    input_: Dict[str, Any]

class PredictionResponse(BaseModel):
    """Response model for prediction."""
    result: Any

# %% FASTAPI AND KAFKA SERVICE CLASS
class FastAPIKafkaService():
    """Service for deploying a FastAPI application with a Kafka producer and consumer."""

    def __init__(
        self,
        prediction_callback: Callable[[Dict[str, Any]], Any],
        kafka_config: Dict[str, Any],
        input_topic: str,
        output_topic: str,
    ):
        self.server_thread: threading.Thread | None = None
        self.stop_event: threading.Event = threading.Event()
        self.prediction_callback = prediction_callback
        self.kafka_config = kafka_config
        self.input_topic = input_topic
        self.output_topic = output_topic
        self.producer: Producer | None = None
        self.consumer: Consumer | None = None
        # No longer needed here:
        # self.PredictionRequest = PredictionRequest
        # self.PredictionResponse = PredictionResponse


    def delivery_report(self, err, msg):
        """Called once for each message produced to indicate delivery result."""
        if err is not None:
            logger.error("Message delivery failed: {}".format(err))
        else:
            logger.info("Message delivered to {} [{}]".format(msg.topic(), msg.partition()))

    def start(self) -> None:
        """Start the FastAPI application and Kafka consumer."""
        self.stop_event.clear()
        # Initialize Kafka producer
        try:
            self.producer = Producer(self.kafka_config)
            logger.info("Kafka producer initialized")
        except Exception as e:
            logger.error(f"Failed to initialize Kafka producer: {e}")
            raise

        # Initialize Kafka consumer
        self.kafka_config['enable.auto.commit'] = False
        try:
            self.consumer = Consumer(self.kafka_config)
            self.consumer.subscribe([self.input_topic])
            logger.info(f"Kafka consumer subscribed to topic: {self.input_topic}")
        except Exception as e:
            logger.error(f"Failed to initialize Kafka consumer: {e}")
            raise

        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.start()
        time.sleep(2)
        threading.Thread(target=self.consume_messages, daemon=True).start()

        logger.info("FastAPI server and Kafka consumer threads started.")

    def run_server(self) -> None:
        """Run the FastAPI server."""
        try:
            uvicorn.run(app, host="0.0.0.0", port=8100, log_level="info")
        except Exception as e:
            logger.error(f"Server error: {e}")

    def consume_messages(self) -> None:
        """Consume messages from Kafka topic and produce predictions."""
        while not self.stop_event.is_set():
            time.sleep(0.1)
            msg = self.poll_message()
            if msg is None:

                continue
            if msg.error():
                if not self.handle_message_error(msg):
                    break
                continue
            self.process_message(msg)
        self.close_consumer()

    def poll_message(self):
        """Poll message from Kafka consumer."""
        if self.consumer:
            return self.consumer.poll(1.0)
        else:
            logger.error("Kafka consumer is not initialized.")
            return None

    def handle_message_error(self, msg) -> bool:
        """Handle errors in polled messages."""
        if msg.error().code() == KafkaError._PARTITION_EOF:
            logger.debug("Reached end of partition.")
            return True
        else:
            logger.error(f"Consumer error: {msg.error()}")
            return False

    def process_message(self, msg) -> None:
        """Process a valid Kafka message."""
        try:
            input_data = json.loads(msg.value().decode("utf-8"))
            logger.debug(f"Received input  {input_data}")
            prediction_result = self.prediction_callback(input_data)
            logger.debug(f"Prediction result: {prediction_result}")

            if self.producer:
                self.producer.produce(
                    self.output_topic,
                    key="prediction",
                    value=json.dumps(prediction_result),
                    callback=self.delivery_report,
                )
                self.producer.flush()
            else:
                logger.error("Kafka producer is not initialized.")

            if self.consumer:
                self.consumer.commit(msg)

        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode JSON message: {e}. Raw message: {msg.value()}")
        except Exception as e:
            logger.exception("Error processing message:")

    def close_consumer(self) -> None:
        """Close the Kafka consumer."""
        if self.consumer:
            self.consumer.close()
        logger.info("Kafka consumer stopped.")

    def stop(self) -> None:
        """Stop the FastAPI application and Kafka consumer."""
        self.stop_event.set()
        if self.consumer:
            self.consumer.close()
            logger.info("Kafka consumer closed.")
        os.kill(os.getpid(), signal.SIGINT)
        logger.info("Service stopped.")

    @app.post("/predict", response_model=PredictionResponse)  # Use global var
    async def predict(self, request: PredictionRequest) -> PredictionResponse:  # Use global var
        """Endpoint for making predictions via HTTP."""
        try:
            logger.info(f"Received HTTP prediction request: {request.input_}")
            prediction_result = self.prediction_callback(request.input_)
            logger.info(f"HTTP prediction result: {prediction_result}")
            return PredictionResponse(result=prediction_result)  # Use the global class
        except Exception as e:
            logger.exception("Error processing HTTP prediction request:")
            raise HTTPException(status_code=500, detail=str(e))


# %% SCRIPT EXECUTION
if __name__ == "__main__":
    # Example prediction callback function
    def my_prediction_function(input_: Dict[str, Any]) -> Any:
        return {"predicted_output": input_}

    # Kafka configuration
    kafka_config = {
        "bootstrap.servers": "kafka_server:9092",
        "group.id": "llmops-regression",
        "auto.offset.reset": "earliest",
    }
    input_topic = "input_topic"
    output_topic = "output_topic"
    fastapi_kafka_service = FastAPIKafkaService(
        prediction_callback=my_prediction_function,
        kafka_config=kafka_config,
        input_topic=input_topic,
        output_topic=output_topic,
    )
    fastapi_kafka_service.start()
    print("FastAPI and Kafka service is running.  Press Ctrl+C to stop.")