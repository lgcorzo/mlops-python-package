---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: kafka_app"
source_path: "src/regression_model_template/controller/kafka_app.py"
description: "FastAPI and Kafka Service for Predictions with Logging."
tags: ["module", "kafka_app"]
timestamp: "2026-08-15T05:57:16Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: kafka_app

* **Source Reference:** [src/regression_model_template/controller/kafka_app.py](../../../../src/regression_model_template/controller/kafka_app.py)

## 1. Architectural Role & Responsibilities
FastAPI and Kafka Service for Predictions with Logging.

### Detected Architecture Patterns
Detected roles: Controller

## 2. UML Diagrams
### Class Diagram
```plantuml
classDiagram
    direction BT
    class RateLimiter {
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
        +predict(self: Any, input_data: PredictionRequest) PredictionResponse
    }
```

### Sequence Diagram
```plantuml
sequenceDiagram
    RateLimiter.is_allowed->>time: invoke
    RateLimiter.is_allowed->>move_to_end: invoke
    RateLimiter.is_allowed->>append: invoke
    RateLimiter.is_allowed->>deque: invoke
    RateLimiter.is_allowed->>popleft: invoke
    RateLimiter.is_allowed->>len: invoke
    RateLimiter.is_allowed->>popitem: invoke
    PredictionRequest.validate_schema->>validate: invoke
    PredictionRequest.validate_schema->>DataFrame: invoke
    PredictionRequest.check_input_size->>field_validator: invoke
    PredictionRequest.check_input_size->>values: invoke
    PredictionRequest.check_input_size->>ValueError: invoke
    PredictionRequest.check_input_size->>len: invoke
    PredictionRequest.check_input_size->>isinstance: invoke
    FastAPIKafkaService.delivery_report->>error: invoke
    FastAPIKafkaService.delivery_report->>info: invoke
    FastAPIKafkaService.delivery_report->>topic: invoke
    FastAPIKafkaService.delivery_report->>partition: invoke
    FastAPIKafkaService.start->>clear: invoke
    FastAPIKafkaService.start->>_initialize_kafka_producer: invoke
    FastAPIKafkaService.start->>_initialize_kafka_consumer: invoke
    FastAPIKafkaService.start->>Thread: invoke
    FastAPIKafkaService.start->>start: invoke
    FastAPIKafkaService.start->>info: invoke
    FastAPIKafkaService._initialize_kafka_producer->>Producer: invoke
    FastAPIKafkaService._initialize_kafka_producer->>info: invoke
    FastAPIKafkaService._initialize_kafka_producer->>error: invoke
    FastAPIKafkaService._initialize_kafka_producer->>items: invoke
    FastAPIKafkaService._initialize_kafka_consumer->>_ensure_topics_exist: invoke
    FastAPIKafkaService._initialize_kafka_consumer->>Consumer: invoke
    FastAPIKafkaService._initialize_kafka_consumer->>subscribe: invoke
    FastAPIKafkaService._initialize_kafka_consumer->>info: invoke
    FastAPIKafkaService._initialize_kafka_consumer->>error: invoke
    FastAPIKafkaService._ensure_topics_exist->>AdminClient: invoke
    FastAPIKafkaService._ensure_topics_exist->>create_topics: invoke
    FastAPIKafkaService._ensure_topics_exist->>items: invoke
    FastAPIKafkaService._ensure_topics_exist->>NewTopic: invoke
    FastAPIKafkaService._ensure_topics_exist->>warning: invoke
    FastAPIKafkaService._ensure_topics_exist->>result: invoke
    FastAPIKafkaService._ensure_topics_exist->>info: invoke
    FastAPIKafkaService._ensure_topics_exist->>debug: invoke
    FastAPIKafkaService._run_server->>run: invoke
    FastAPIKafkaService._run_server->>error: invoke
    FastAPIKafkaService._consume_messages->>_close_consumer: invoke
    FastAPIKafkaService._consume_messages->>is_set: invoke
    FastAPIKafkaService._consume_messages->>_poll_message: invoke
    FastAPIKafkaService._consume_messages->>error: invoke
    FastAPIKafkaService._consume_messages->>_process_message: invoke
    FastAPIKafkaService._consume_messages->>info: invoke
    FastAPIKafkaService._consume_messages->>flush: invoke
    FastAPIKafkaService._consume_messages->>_handle_message_error: invoke
    FastAPIKafkaService._poll_message->>poll: invoke
    FastAPIKafkaService._poll_message->>error: invoke
    FastAPIKafkaService._handle_message_error->>error: invoke
    FastAPIKafkaService._handle_message_error->>code: invoke
    FastAPIKafkaService._handle_message_error->>debug: invoke
    FastAPIKafkaService._handle_message_error->>warning: invoke
    FastAPIKafkaService._process_message->>PredictionResponse: invoke
    FastAPIKafkaService._process_message->>value: invoke
    FastAPIKafkaService._process_message->>loads: invoke
    FastAPIKafkaService._process_message->>debug: invoke
    FastAPIKafkaService._process_message->>PredictionRequest: invoke
    FastAPIKafkaService._process_message->>error: invoke
    FastAPIKafkaService._process_message->>decode: invoke
    FastAPIKafkaService._process_message->>get: invoke
    FastAPIKafkaService._process_message->>len: invoke
    FastAPIKafkaService._process_message->>info: invoke
    FastAPIKafkaService._process_message->>prediction_callback: invoke
    FastAPIKafkaService._process_message->>exception: invoke
    FastAPIKafkaService._process_message->>isinstance: invoke
    FastAPIKafkaService._process_message->>copy: invoke
    FastAPIKafkaService._process_message->>produce: invoke
    FastAPIKafkaService._process_message->>poll: invoke
    FastAPIKafkaService._process_message->>commit: invoke
    FastAPIKafkaService._process_message->>next: invoke
    FastAPIKafkaService._process_message->>dumps: invoke
    FastAPIKafkaService._process_message->>iter: invoke
    FastAPIKafkaService._process_message->>values: invoke
    FastAPIKafkaService._close_consumer->>info: invoke
    FastAPIKafkaService._close_consumer->>close: invoke
    FastAPIKafkaService.stop->>set: invoke
    FastAPIKafkaService.stop->>info: invoke
    FastAPIKafkaService.stop->>close: invoke
    PredictionService.predict->>PredictionResponse: invoke
    PredictionService.predict->>predict: invoke
    PredictionService.predict->>tolist: invoke
    PredictionService.predict->>exception: invoke
    PredictionService.predict->>check: invoke
    PredictionService.predict->>to_numpy: invoke
    PredictionService.predict->>DataFrame: invoke
    default_input_payload->>strftime: invoke
    default_input_payload->>now: invoke
    default_input_payload->>weekday: invoke
    main->>MlflowService: invoke
    main->>start: invoke
    main->>uri_for_model_alias_or_version: invoke
    main->>CustomLoader: invoke
    main->>load: invoke
    main->>PredictionService: invoke
    main->>FastAPIKafkaService: invoke
    main->>print: invoke
```

### Component Diagram
```plantuml
component [kafka_app] as Comp
Comp --> [json]
Comp --> [logging]
Comp --> [os]
Comp --> [threading]
Comp --> [time]
Comp --> [collections]
Comp --> [Any]
Comp --> [Callable]
Comp --> [Dict]
Comp --> [cast]
Comp --> [pandas]
Comp --> [uvicorn]
Comp --> [Consumer]
Comp --> [KafkaError]
Comp --> [Message]
Comp --> [Producer]
Comp --> [AdminClient]
Comp --> [NewTopic]
Comp --> [FastAPI]
Comp --> [HTTPException]
Comp --> [Request]
Comp --> [run_in_threadpool]
Comp --> [CORSMiddleware]
Comp --> [TrustedHostMiddleware]
Comp --> [ProxyHeadersMiddleware]
Comp --> [BaseModel]
Comp --> [Field]
Comp --> [field_validator]
Comp --> [InputsSchema]
Comp --> [Outputs]
Comp --> [registries]
Comp --> [services]
Comp --> [CustomLoader]
```

## 3. Class & Method Specifications

### `RateLimiter`

In-memory sliding window rate limiter backed by OrderedDict.

#### Constructor
* **`__init__(self: Any, max_requests: int, window_seconds: int, max_tracked_ips: int)`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `max_requests` (`int`)
    - `window_seconds` (`int`)
    - `max_tracked_ips` (`int`)

#### Public Methods
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

#### Constructor
* **`__init__(self: Any, prediction_callback: Callable[([PredictionRequest], PredictionResponse)], kafka_config: Dict[(str, Any)], input_topic: str, output_topic: str)`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `prediction_callback` (`Callable[([PredictionRequest], PredictionResponse)]`)
    - `kafka_config` (`Dict[(str, Any)]`)
    - `input_topic` (`str`)
    - `output_topic` (`str`)

#### Public Methods
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

#### Constructor
* **`__init__(self: Any, model: Any)`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `model` (`Any`)

#### Public Methods
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

* [test_kafka_app.py](../../tests/controller/test_kafka_app.md)
* [test_kafka_app_dos.py](../../tests/controller/test_kafka_app_dos.md)
* [test_kafka_app_leakage.py](../../tests/controller/test_kafka_app_leakage.md)
* [test_kafka_app_logging.py](../../tests/controller/test_kafka_app_logging.md)
* [test_kafka_app_security.py](../../tests/controller/test_kafka_app_security.md)
* [test_log_leakage.py](../../tests/controller/test_log_leakage.md)
* [test_middleware_config.py](../../tests/controller/test_middleware_config.md)
* [test_rate_limiter.py](../../tests/controller/test_rate_limiter.md)
