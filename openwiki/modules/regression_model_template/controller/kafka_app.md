---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: kafka_app"
source_path: "src/regression_model_template/controller/kafka_app.py"
description: "FastAPI and Kafka Service for Predictions with Logging."
tags: ["module", "kafka_app"]
timestamp: "2026-09-05T05:14:17Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: kafka_app

* **Source Reference:** [src/regression_model_template/controller/kafka_app.py](../../../../src/regression_model_template/controller/kafka_app.py)

# Module Overview

## Purpose

FastAPI and Kafka Service for Predictions with Logging.

## Responsibilities

FastAPI and Kafka Service for Predictions with Logging.

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

# Each File Documentation

## Imported modules

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

## Exported classes

* `RateLimiter`

* `PredictionRequest`

* `PredictionResponse`

* `FastAPIKafkaService`

* `PredictionService`

## Exported functions

* `default_input_payload`

* `main`

## Exported interfaces

_No interfaces found._

## Public API

_See exported classes and functions._

## Internal architecture

_See architectural detected patterns and UML._

## Execution flow

_Execution flow depends on public API usage._

## Sequence explanation

_See sequence diagram._

## UML

_See diagrams below._

## Examples

_No module level examples available._

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
    PredictionService ..> PredictionRequest : Usage
    PredictionService ..> PredictionResponse : Usage
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

# Public Classes

### `RateLimiter`

## Overview

In-memory sliding window rate limiter backed by OrderedDict.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Constructor

* **`__init__(self: Any, max_requests: int, window_seconds: int, max_tracked_ips: int)`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `max_requests`

  - **type**: int

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: 100

* `window_seconds`

  - **type**: int

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: 60

* `max_tracked_ips`

  - **type**: int

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: MAX_TRACKED_IPS

### Output

* **return type**: None

* **semantic meaning**: Initialization

* **possible null values**: None

* **exceptions**: Unspecified

## Public Methods

### `is_allowed(self: Any, ip: str) -> bool`

### Description

Check if the given IP is allowed to make a request.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `ip`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: bool

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for is_allowed

```

### `PredictionRequest`

## Overview

Request model for prediction.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`input_data`**

  - **Type**: Dict[(str, Any)]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `validate_schema(self: Any) -> pd.DataFrame`

### Description

Validates the input data against InputsSchema.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: pd.DataFrame

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for validate_schema

```

### `check_input_size(cls: Any, v: Dict[(str, Any)]) -> Dict[(str, Any)]`

### Description

Check if the input data size is within limits.

### Inputs

* `cls`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `v`

  - **type**: Dict[(str, Any)]

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: Dict[(str, Any)]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for check_input_size

```

### `PredictionResponse`

## Overview

Response model for prediction.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`result`**

  - **Type**: Dict[(str, Any)]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

### `FastAPIKafkaService`

## Overview

Service for deploying a FastAPI application with a Kafka producer and consumer.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Constructor

* **`__init__(self: Any, prediction_callback: Callable[([PredictionRequest], PredictionResponse)], kafka_config: Dict[(str, Any)], input_topic: str, output_topic: str)`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `prediction_callback`

  - **type**: Callable[([PredictionRequest], PredictionResponse)]

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `kafka_config`

  - **type**: Dict[(str, Any)]

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `input_topic`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `output_topic`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: None

* **semantic meaning**: Initialization

* **possible null values**: None

* **exceptions**: Unspecified

## Public Methods

### `delivery_report(self: Any, err: KafkaError | None, msg: Message) -> None`

### Description

Called once for each message produced to indicate delivery result.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `err`

  - **type**: KafkaError | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `msg`

  - **type**: Message

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: None

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for delivery_report

```

### `start(self: Any) -> None`

### Description

Start the FastAPI application and Kafka consumer.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: None

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for start

```

### `stop(self: Any) -> None`

### Description

Stop the FastAPI application and Kafka consumer.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: None

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for stop

```

# Private Methods

* **`_initialize_kafka_producer(self: Any) -> None`**

### Purpose

Initialize Kafka producer.

### Parameters

* `self` (`Any`)

### Return value

* `None`

* **`_initialize_kafka_consumer(self: Any) -> None`**

### Purpose

Initialize Kafka consumer.

### Parameters

* `self` (`Any`)

### Return value

* `None`

* **`_ensure_topics_exist(self: Any) -> None`**

### Purpose

Ensure input and output Kafka topics exist on the broker.

### Parameters

* `self` (`Any`)

### Return value

* `None`

* **`_run_server(self: Any) -> None`**

### Purpose

Run the FastAPI server.

### Parameters

* `self` (`Any`)

### Return value

* `None`

* **`_consume_messages(self: Any) -> None`**

### Purpose

Consume messages from Kafka topic and produce predictions.

### Parameters

* `self` (`Any`)

### Return value

* `None`

* **`_poll_message(self: Any) -> Message | None`**

### Purpose

Poll message from Kafka consumer.

### Parameters

* `self` (`Any`)

### Return value

* `Message | None`

* **`_handle_message_error(self: Any, msg: Message) -> bool`**

### Purpose

Handle errors in polled messages.

### Parameters

* `self` (`Any`)

* `msg` (`Message`)

### Return value

* `bool`

* **`_process_message(self: Any, msg: Message) -> None`**

### Purpose

Process a valid Kafka message.

### Parameters

* `self` (`Any`)

* `msg` (`Message`)

### Return value

* `None`

* **`_close_consumer(self: Any) -> None`**

### Purpose

Close the Kafka consumer.

### Parameters

* `self` (`Any`)

### Return value

* `None`

### `PredictionService`

## Overview

Service to handle prediction logic securely.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Constructor

* **`__init__(self: Any, model: Any)`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `model`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: None

* **semantic meaning**: Initialization

* **possible null values**: None

* **exceptions**: Unspecified

## Public Methods

### `predict(self: Any, input_data: PredictionRequest) -> PredictionResponse`

### Description

Make a prediction using the model.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `input_data`

  - **type**: PredictionRequest

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: PredictionResponse

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for predict

```

## Standalone Functions

### `default_input_payload() -> Dict[(str, Any)]`

### Description

Generate a fresh default input payload with current timestamps.

### Inputs

### Output

* **return type**: Dict[(str, Any)]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for default_input_payload

```

### `main() -> None`

### Description

No description available.

### Inputs

### Output

* **return type**: None

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for main

```

## Used By

* [test_kafka_app.py](../../tests/controller/test_kafka_app.md)

* [test_kafka_app_dos.py](../../tests/controller/test_kafka_app_dos.md)

* [test_kafka_app_leakage.py](../../tests/controller/test_kafka_app_leakage.md)

* [test_kafka_app_logging.py](../../tests/controller/test_kafka_app_logging.md)

* [test_kafka_app_security.py](../../tests/controller/test_kafka_app_security.md)

* [test_log_leakage.py](../../tests/controller/test_log_leakage.md)

* [test_middleware_config.py](../../tests/controller/test_middleware_config.md)

* [test_rate_limiter.py](../../tests/controller/test_rate_limiter.md)
