---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: kafka_app"
source_path: "src/regression_model_template/controller/kafka_app.py"
description: "FastAPI and Kafka Service for Predictions with Logging."
tags: ["module", "kafka_app"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: kafka_app

* **Source Reference:** [src/regression_model_template/controller/kafka_app.py](../../../src/regression_model_template/controller/kafka_app.py)

## 1. Architectural Role & Responsibilities
FastAPI and Kafka Service for Predictions with Logging.

## 2. UML 2.0 Class Diagram
```plantuml
classDiagram
    direction BT
    class RateLimiter {
        +__init__(self: Any, max_requests: int, window_seconds: int, max_tracked_ips: int) Any
        +is_allowed(self: Any, ip: str) bool
    }
    class PredictionRequest {
        +input_data: Dict~(str, Any)~
        +validate_schema(self: Any) pd.DataFrame
        +check_input_size(cls: Any, v: Dict~(str, Any)~) Dict~(str, Any)~
    }
    BaseModel <|-- PredictionRequest : Generalization
    class PredictionResponse {
        +result: Dict~(str, Any)~
    }
    BaseModel <|-- PredictionResponse : Generalization
    class FastAPIKafkaService {
        +__init__(self: Any, prediction_callback: Callable~(~PredictionRequest~, PredictionResponse)~, kafka_config: Dict~(str, Any)~, input_topic: str, output_topic: str) Any
        +delivery_report(self: Any, err: KafkaError | None, msg: Message) None
        +start(self: Any) None
        +_initialize_kafka_producer(self: Any) None
        +_initialize_kafka_consumer(self: Any) None
        +_ensure_topics_exist(self: Any) None
        +_run_server(self: Any) None
        +_consume_messages(self: Any) None
        +_poll_message(self: Any) Message | None
        +_handle_message_error(self: Any, msg: Message) bool
        +_process_message(self: Any, msg: Message) None
        +_close_consumer(self: Any) None
        +stop(self: Any) None
    }
    class PredictionService {
        +__init__(self: Any, model: Any) Any
        +predict(self: Any, input_data: PredictionRequest) PredictionResponse
    }
```

## 3. Class & Method Specifications

### `RateLimiter`

In-memory sliding window rate limiter backed by OrderedDict.

#### Public Methods
* **`__init__(self: Any, max_requests: int, window_seconds: int, max_tracked_ips: int) -> Any`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `max_requests` (`int`)
    - `window_seconds` (`int`)
    - `max_tracked_ips` (`int`)
  - **Outputs**: `Any`
* **`is_allowed(self: Any, ip: str) -> bool`**
  - **Purpose**: Check if the given IP is allowed to make a request.
  - **Inputs**:
    - `self` (`Any`)
    - `ip` (`str`)
  - **Outputs**: `bool`

### `PredictionRequest`

Request model for prediction.

#### Attributes
* **`input_data`** (`Dict[(str, Any)]`)

#### Public Methods
* **`validate_schema(self: Any) -> pd.DataFrame`**
  - **Purpose**: Validates the input data against InputsSchema.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `pd.DataFrame`
* **`check_input_size(cls: Any, v: Dict[(str, Any)]) -> Dict[(str, Any)]`**
  - **Purpose**: Check if the input data size is within limits.
  - **Inputs**:
    - `cls` (`Any`)
    - `v` (`Dict[(str, Any)]`)
  - **Outputs**: `Dict[(str, Any)]`

### `PredictionResponse`

Response model for prediction.

#### Attributes
* **`result`** (`Dict[(str, Any)]`)

### `FastAPIKafkaService`

Service for deploying a FastAPI application with a Kafka producer and consumer.

#### Public Methods
* **`__init__(self: Any, prediction_callback: Callable[([PredictionRequest], PredictionResponse)], kafka_config: Dict[(str, Any)], input_topic: str, output_topic: str) -> Any`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `prediction_callback` (`Callable[([PredictionRequest], PredictionResponse)]`)
    - `kafka_config` (`Dict[(str, Any)]`)
    - `input_topic` (`str`)
    - `output_topic` (`str`)
  - **Outputs**: `Any`
* **`delivery_report(self: Any, err: KafkaError | None, msg: Message) -> None`**
  - **Purpose**: Called once for each message produced to indicate delivery result.
  - **Inputs**:
    - `self` (`Any`)
    - `err` (`KafkaError | None`)
    - `msg` (`Message`)
  - **Outputs**: `None`
* **`start(self: Any) -> None`**
  - **Purpose**: Start the FastAPI application and Kafka consumer.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `None`
* **`stop(self: Any) -> None`**
  - **Purpose**: Stop the FastAPI application and Kafka consumer.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `None`

#### Private Methods
* **`_initialize_kafka_producer(self: Any) -> None`**
  - **Purpose**: Initialize Kafka producer.
* **`_initialize_kafka_consumer(self: Any) -> None`**
  - **Purpose**: Initialize Kafka consumer.
* **`_ensure_topics_exist(self: Any) -> None`**
  - **Purpose**: Ensure input and output Kafka topics exist on the broker.
* **`_run_server(self: Any) -> None`**
  - **Purpose**: Run the FastAPI server.
* **`_consume_messages(self: Any) -> None`**
  - **Purpose**: Consume messages from Kafka topic and produce predictions.
* **`_poll_message(self: Any) -> Message | None`**
  - **Purpose**: Poll message from Kafka consumer.
* **`_handle_message_error(self: Any, msg: Message) -> bool`**
  - **Purpose**: Handle errors in polled messages.
* **`_process_message(self: Any, msg: Message) -> None`**
  - **Purpose**: Process a valid Kafka message.
* **`_close_consumer(self: Any) -> None`**
  - **Purpose**: Close the Kafka consumer.

### `PredictionService`

Service to handle prediction logic securely.

#### Public Methods
* **`__init__(self: Any, model: Any) -> Any`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `model` (`Any`)
  - **Outputs**: `Any`
* **`predict(self: Any, input_data: PredictionRequest) -> PredictionResponse`**
  - **Purpose**: Make a prediction using the model.
  - **Inputs**:
    - `self` (`Any`)
    - `input_data` (`PredictionRequest`)
  - **Outputs**: `PredictionResponse`

## Standalone Functions

### `default_input_payload() -> Dict[(str, Any)]`
Generate a fresh default input payload with current timestamps.

#### Inputs

#### Outputs
* `Dict[(str, Any)]`

### `main() -> None`
No description available.

#### Inputs

#### Outputs
* `None`

## Dependencies

* `json`
* `logging`
* `os`
* `threading`
* `time`
* `collections`
* `typing.Any`
* `typing.Callable`
* `typing.Dict`
* `typing.cast`
* `pandas`
* `uvicorn`
* `confluent_kafka.Consumer`
* `confluent_kafka.KafkaError`
* `confluent_kafka.Message`
* `confluent_kafka.Producer`
* `confluent_kafka.admin.AdminClient`
* `confluent_kafka.admin.NewTopic`
* `fastapi.FastAPI`
* `fastapi.HTTPException`
* `fastapi.Request`
* `fastapi.concurrency.run_in_threadpool`
* `fastapi.middleware.cors.CORSMiddleware`
* `fastapi.middleware.trustedhost.TrustedHostMiddleware`
* `uvicorn.middleware.proxy_headers.ProxyHeadersMiddleware`
* `pydantic.BaseModel`
* `pydantic.Field`
* `pydantic.field_validator`
* `regression_model_template.core.schemas.InputsSchema`
* `regression_model_template.core.schemas.Outputs`
* `regression_model_template.io.registries`
* `regression_model_template.io.services`
* `regression_model_template.io.registries.CustomLoader`

## Used By

_Not used by any other module._
