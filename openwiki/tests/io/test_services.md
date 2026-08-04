---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_services Documentation"
description: "Documentation for tests/io/test_services.py"
tags: ["module", "test_services"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/io/test_services.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Services

**Dependencies**:
- `_pytest.capture`
- `plyer`
- `_pytest.logging`
- `pytest_mock`
- `mlflow`
- `pytest`
- `regression_model_template.io`

**Exported Symbols**:
- `test_logger_service`
- `test_alerts_service`
- `test_mlflow_service`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
test_logger_service --> logger
test_logger_service --> debug
test_logger_service --> error
test_alerts_service --> parametrize
test_alerts_service --> AlertsService
test_alerts_service --> patch
test_alerts_service --> notify
test_alerts_service --> assert_called_once
test_alerts_service --> assert_not_called
test_alerts_service --> readouterr
test_alerts_service --> readouterr
test_mlflow_service --> RunConfig
test_mlflow_service --> client
test_mlflow_service --> get_run
test_mlflow_service --> get_experiment_by_name
test_mlflow_service --> get_experiment_by_name
test_mlflow_service --> run_context
test_mlflow_service --> get_tracking_uri
test_mlflow_service --> get_registry_uri
test_mlflow_service --> values
test_mlflow_service --> items
test_mlflow_service --> items
@enduml
```

## Classes
## Functions
### Function `test_logger_service`
- **Description**: No description available.
- **Inputs**:
  - `logger_service`: services.LoggerService
  - `logger_caplog`: pl.LogCaptureFixture
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_alerts_service`
- **Description**: No description available.
- **Inputs**:
  - `enable`: bool
  - `mocker`: pm.MockerFixture
  - `capsys`: pc.CaptureFixture[str]
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_mlflow_service`
- **Description**: No description available.
- **Inputs**:
  - `mlflow_service`: services.MlflowService
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
