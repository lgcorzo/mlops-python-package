---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_log_leakage"
source_path: "tests/controller/test_log_leakage.py"
description: "No description available."
tags: ["module", "test_log_leakage"]
timestamp: "2026-08-13T05:18:56Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: test_log_leakage

* **Source Reference:** [tests/controller/test_log_leakage.py](../../../../tests/controller/test_log_leakage.py)

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
    test_kafka_consumer_log_leakage->>MagicMock: invoke
    test_kafka_consumer_log_leakage->>FastAPIKafkaService: invoke
    test_kafka_consumer_log_leakage->>encode: invoke
    test_kafka_consumer_log_leakage->>set_level: invoke
    test_kafka_consumer_log_leakage->>_process_message: invoke
    test_kafka_consumer_log_leakage->>dumps: invoke
    test_kafka_consumer_prediction_result_leakage->>MagicMock: invoke
    test_kafka_consumer_prediction_result_leakage->>FastAPIKafkaService: invoke
    test_kafka_consumer_prediction_result_leakage->>encode: invoke
    test_kafka_consumer_prediction_result_leakage->>set_level: invoke
    test_kafka_consumer_prediction_result_leakage->>_process_message: invoke
    test_kafka_consumer_prediction_result_leakage->>dumps: invoke
```

### Component Diagram
```plantuml
component [test_log_leakage] as Comp
Comp --> [pytest]
Comp --> [logging]
Comp --> [MagicMock]
Comp --> [PredictionRequest]
Comp --> [predict]
Comp --> [FastAPIKafkaService]
Comp --> [pandas]
```

## 3. Class & Method Specifications

## Standalone Functions

### `test_kafka_consumer_log_leakage(caplog: Any) -> Any`
Test that the Kafka consumer processing does not log sensitive information at INFO level.

#### Inputs
* `caplog` (`Any`)

#### Outputs
* `Any`

### `test_kafka_consumer_prediction_result_leakage(caplog: Any) -> Any`
Test that the Kafka consumer processing does not log raw prediction result values (inference)
at any log level, and instead uses a masked/summarized format.

#### Inputs
* `caplog` (`Any`)

#### Outputs
* `Any`

## Dependencies

* `pytest`
* `logging`
* `unittest.mock.MagicMock`
* `regression_model_template.controller.kafka_app.PredictionRequest`
* `regression_model_template.controller.kafka_app.predict`
* `regression_model_template.controller.kafka_app.FastAPIKafkaService`
* `pandas`

## Used By

_Not used by any other module._
