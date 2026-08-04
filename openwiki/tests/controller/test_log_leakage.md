---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_log_leakage Documentation"
description: "Documentation for tests/controller/test_log_leakage.py"
tags: ["module", "test_log_leakage"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/controller/test_log_leakage.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Controllers

**Dependencies**:
- `regression_model_template.controller.kafka_app`
- `logging`
- `pytest`
- `pandas`
- `unittest.mock`

**Exported Symbols**:
- `test_kafka_consumer_log_leakage`
- `test_kafka_consumer_prediction_result_leakage`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
test_kafka_consumer_log_leakage --> MagicMock
test_kafka_consumer_log_leakage --> MagicMock
test_kafka_consumer_log_leakage --> FastAPIKafkaService
test_kafka_consumer_log_leakage --> MagicMock
test_kafka_consumer_log_leakage --> encode
test_kafka_consumer_log_leakage --> set_level
test_kafka_consumer_log_leakage --> MagicMock
test_kafka_consumer_log_leakage --> MagicMock
test_kafka_consumer_log_leakage --> _process_message
test_kafka_consumer_log_leakage --> dumps
test_kafka_consumer_prediction_result_leakage --> MagicMock
test_kafka_consumer_prediction_result_leakage --> MagicMock
test_kafka_consumer_prediction_result_leakage --> FastAPIKafkaService
test_kafka_consumer_prediction_result_leakage --> MagicMock
test_kafka_consumer_prediction_result_leakage --> encode
test_kafka_consumer_prediction_result_leakage --> set_level
test_kafka_consumer_prediction_result_leakage --> MagicMock
test_kafka_consumer_prediction_result_leakage --> MagicMock
test_kafka_consumer_prediction_result_leakage --> _process_message
test_kafka_consumer_prediction_result_leakage --> dumps
@enduml
```

## Classes
## Functions
### Function `test_kafka_consumer_log_leakage`
- **Description**: Test that the Kafka consumer processing does not log sensitive information at INFO level.
- **Inputs**:
  - `caplog`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_kafka_consumer_prediction_result_leakage`
- **Description**: Test that the Kafka consumer processing does not log raw prediction result values (inference)
at any log level, and instead uses a masked/summarized format.
- **Inputs**:
  - `caplog`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented
