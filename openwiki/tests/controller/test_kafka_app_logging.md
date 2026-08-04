---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_kafka_app_logging Documentation"
description: "Documentation for tests/controller/test_kafka_app_logging.py"
tags: ["module", "test_kafka_app_logging"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/controller/test_kafka_app_logging.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Controllers

**Dependencies**:
- `pytest`
- `regression_model_template.controller.kafka_app`
- `json`
- `unittest.mock`

**Exported Symbols**:
- `mock_kafka_service`
- `test_kafka_process_message_logging`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
mock_kafka_service --> MagicMock
mock_kafka_service --> MagicMock
mock_kafka_service --> patch
mock_kafka_service --> patch
mock_kafka_service --> FastAPIKafkaService
test_kafka_process_message_logging --> patch
test_kafka_process_message_logging --> MagicMock
test_kafka_process_message_logging --> encode
test_kafka_process_message_logging --> MagicMock
test_kafka_process_message_logging --> PredictionRequest
test_kafka_process_message_logging --> patch
test_kafka_process_message_logging --> _process_message
test_kafka_process_message_logging --> assert_any_call
test_kafka_process_message_logging --> len
test_kafka_process_message_logging --> assert_any_call
test_kafka_process_message_logging --> dumps
@enduml
```

## Classes
## Functions
### Function `mock_kafka_service`
- **Description**: Mock the FastAPIKafkaService and its dependencies.
- **Inputs**:
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_kafka_process_message_logging`
- **Description**: Test that Kafka consumer logs correctly using debug and safe info logs.
- **Inputs**:
  - `mock_logger`: Any
  - `mock_kafka_service`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented
