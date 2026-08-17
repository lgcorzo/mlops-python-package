---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_kafka_app"
source_path: "tests/controller/test_kafka_app.py"
description: "No description available."
tags: ["module", "test_kafka_app"]
timestamp: "2026-08-17T05:34:56Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "73b4d7b"
---
# Module Specification: test_kafka_app

* **Source Reference:** [tests/controller/test_kafka_app.py](../../../../tests/controller/test_kafka_app.py)

## 1. Architectural Role & Responsibilities

No description available.

### Detected Architecture Patterns

Detected roles: Controller

## 2. UML Diagrams

### Class Diagram

_No classes found._


### Sequence Diagram

```plantuml
sequenceDiagram
    mock_kafka_service->>patch: invoke
    mock_kafka_service->>MagicMock: invoke
    mock_kafka_service->>FastAPIKafkaService: invoke
    mock_kafka_service->>PredictionResponse: invoke
    test_delivery_report->>MagicMock: invoke
    test_delivery_report->>patch: invoke
    test_delivery_report->>delivery_report: invoke
    test_delivery_report->>assert_called_once: invoke
    test_start->>start: invoke
    test_start->>assert_called_once_with: invoke
    test_start_producer_failure->>Exception: invoke
    test_start_producer_failure->>raises: invoke
    test_start_producer_failure->>start: invoke
    test_start_consumer_failure->>Exception: invoke
    test_start_consumer_failure->>raises: invoke
    test_start_consumer_failure->>start: invoke
    test_run_server->>patch: invoke
    test_run_server->>_run_server: invoke
    test_run_server->>assert_called_once_with: invoke
    test_run_server_failure->>patch: invoke
    test_run_server_failure->>Exception: invoke
    test_run_server_failure->>_run_server: invoke
    test_consume_messages->>MagicMock: invoke
    test_consume_messages->>_consume_messages: invoke
    test_consume_messages->>assert_called_once: invoke
    test_consume_messages_with_error->>MagicMock: invoke
    test_consume_messages_with_error->>_consume_messages: invoke
    test_consume_messages_with_error->>assert_called_once: invoke
    test_consume_messages_with_error->>assert_not_called: invoke
    test_poll_message->>MagicMock: invoke
    test_poll_message->>_poll_message: invoke
    test_poll_message->>assert_called_once_with: invoke
    test_poll_message_no_consumer->>patch: invoke
    test_poll_message_no_consumer->>_poll_message: invoke
    test_poll_message_no_consumer->>assert_called_once: invoke
    test_handle_message_error_partition_eof->>MagicMock: invoke
    test_handle_message_error_partition_eof->>patch: invoke
    test_handle_message_error_partition_eof->>_handle_message_error: invoke
    test_handle_message_error_partition_eof->>assert_called_once: invoke
    test_handle_message_error_other_error->>MagicMock: invoke
    test_handle_message_error_other_error->>patch: invoke
    test_handle_message_error_other_error->>_handle_message_error: invoke
    test_handle_message_error_other_error->>assert_called_once: invoke
    test_handle_message_error_unknown_topic->>MagicMock: invoke
    test_handle_message_error_unknown_topic->>patch: invoke
    test_handle_message_error_unknown_topic->>_handle_message_error: invoke
    test_handle_message_error_unknown_topic->>assert_called_once: invoke
    test_process_message->>patch: invoke
    test_process_message->>MagicMock: invoke
    test_process_message->>encode: invoke
    test_process_message->>dumps: invoke
    test_process_message->>PredictionResponse: invoke
    test_process_message->>_process_message: invoke
    test_process_message->>assert_called_once: invoke
    test_process_message->>assert_called_once_with: invoke
    test_process_message->>PredictionRequest: invoke
    test_process_message_json_decode_error->>patch: invoke
    test_process_message_json_decode_error->>JSONDecodeError: invoke
    test_process_message_json_decode_error->>MagicMock: invoke
    test_process_message_json_decode_error->>assert_not_called: invoke
    test_process_message_json_decode_error->>assert_called_once: invoke
    test_process_message_json_decode_error->>_process_message: invoke
    test_process_message_json_decode_error->>assert_called: invoke
    test_process_message_prediction_error->>patch: invoke
    test_process_message_prediction_error->>MagicMock: invoke
    test_process_message_prediction_error->>encode: invoke
    test_process_message_prediction_error->>dumps: invoke
    test_process_message_prediction_error->>Exception: invoke
    test_process_message_prediction_error->>assert_called_once: invoke
    test_process_message_prediction_error->>PredictionRequest: invoke
    test_process_message_prediction_error->>_process_message: invoke
    test_process_message_prediction_error->>assert_called: invoke
    test_close_consumer->>MagicMock: invoke
    test_close_consumer->>_close_consumer: invoke
    test_close_consumer->>assert_called_once: invoke
    test_close_consumer->>patch: invoke
    test_close_consumer->>assert_called: invoke
    test_stop->>MagicMock: invoke
    test_stop->>stop: invoke
    test_stop->>assert_called_once: invoke
    test_stop->>is_set: invoke
    test_stop->>patch: invoke
    test_main_function->>patch: invoke
    test_main_function->>MagicMock: invoke
    test_main_function->>main: invoke
    test_main_function->>assert_called_once: invoke
    test_main_function->>assert_called_once_with: invoke
    test_main_function->>assert_called: invoke
```

### Component Diagram

```plantuml
component [test_kafka_app] as Comp
Comp --> [json]
Comp --> [MagicMock]
Comp --> [patch]
Comp --> [pytest]
Comp --> [KafkaError]
Comp --> [HTTPException]
Comp --> [DEFAULT_FASTAPI_HOST]
Comp --> [DEFAULT_FASTAPI_PORT]
Comp --> [FastAPIKafkaService]
Comp --> [PredictionRequest]
Comp --> [PredictionResponse]
Comp --> [app]
Comp --> [health_check]
Comp --> [predict]
```


## 3. Class & Method Specifications

## Standalone Functions

### `mock_kafka_service() -> Any`

Fixture to create a mocked FastAPIKafkaService.

#### Inputs


#### Outputs
* `Any`

### `test_initialization(mock_kafka_service: Any) -> Any`

Test FastAPIKafkaService initialization.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_delivery_report(mock_kafka_service: Any) -> Any`

Test delivery report logging.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_start(mock_kafka_service: Any) -> Any`

Test the start method.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_start_producer_failure(mock_kafka_service: Any) -> Any`

Test start method when producer initialization fails.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_start_consumer_failure(mock_kafka_service: Any) -> Any`

Test start method when consumer initialization fails.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_run_server(mock_kafka_service: Any) -> Any`

Test the _run_server method.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_run_server_failure(mock_kafka_service: Any) -> Any`

Test the _run_server method when uvicorn fails.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_consume_messages(mock_kafka_service: Any) -> Any`

Test the _consume_messages method.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_consume_messages_with_error(mock_kafka_service: Any) -> Any`

Test _consume_messages handles message errors.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_poll_message(mock_kafka_service: Any) -> Any`

Test the _poll_message method.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_poll_message_no_consumer(mock_kafka_service: Any) -> Any`

Test _poll_message handles missing consumer.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_handle_message_error_partition_eof(mock_kafka_service: Any) -> Any`

Test _handle_message_error handles partition EOF.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_handle_message_error_other_error(mock_kafka_service: Any) -> Any`

Test _handle_message_error handles other Kafka errors.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_handle_message_error_unknown_topic(mock_kafka_service: Any) -> Any`

Test _handle_message_error handles transient UNKNOWN_TOPIC_OR_PART errors without breaking loop.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_process_message(mock_json_loads: Any, mock_kafka_service: Any) -> Any`

Test the _process_message method.

#### Inputs

* `mock_json_loads` (`Any`)

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_process_message_json_decode_error(mock_json_loads: Any, mock_kafka_service: Any) -> Any`

Test _process_message handles JSON decoding errors.

#### Inputs

* `mock_json_loads` (`Any`)

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_process_message_prediction_error(mock_json_loads: Any, mock_kafka_service: Any) -> Any`

Test _process_message handles prediction callback errors.

#### Inputs

* `mock_json_loads` (`Any`)

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_close_consumer(mock_kafka_service: Any) -> Any`

Test the _close_consumer method.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_stop(mock_kafka_service: Any) -> Any`

Test the stop method.

#### Inputs

* `mock_kafka_service` (`Any`)


#### Outputs
* `Any`

### `test_main_function() -> Any`

Test the main function.

#### Inputs


#### Outputs
* `Any`

### `test_middleware_configuration() -> Any`

Test that security middlewares are configured.

#### Inputs


#### Outputs
* `Any`

## Dependencies

* `json`

* `unittest.mock.MagicMock`

* `unittest.mock.patch`

* `pytest`

* `confluent_kafka.KafkaError`

* `fastapi.HTTPException`

* `regression_model_template.controller.kafka_app.DEFAULT_FASTAPI_HOST`

* `regression_model_template.controller.kafka_app.DEFAULT_FASTAPI_PORT`

* `regression_model_template.controller.kafka_app.FastAPIKafkaService`

* `regression_model_template.controller.kafka_app.PredictionRequest`

* `regression_model_template.controller.kafka_app.PredictionResponse`

* `regression_model_template.controller.kafka_app.app`

* `regression_model_template.controller.kafka_app.health_check`

* `regression_model_template.controller.kafka_app.predict`


## Used By

_Not used by any other module._
