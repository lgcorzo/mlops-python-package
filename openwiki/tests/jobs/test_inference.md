---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_inference Documentation"
description: "Documentation for tests/jobs/test_inference.py"
tags: ["module", "test_inference"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/jobs/test_inference.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Infrastructure

**Dependencies**:
- `pytest`
- `_pytest.capture`
- `regression_model_template.io`
- `regression_model_template`

**Exported Symbols**:
- `test_inference_job`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
test_inference_job --> parametrize
test_inference_job --> isinstance
test_inference_job --> InferenceJob
test_inference_job --> get
test_inference_job --> run
test_inference_job --> set
test_inference_job --> str
test_inference_job --> readouterr
@enduml
```

## Classes
## Functions
### Function `test_inference_job`
- **Description**: No description available.
- **Inputs**:
  - `alias_or_version`: str | int
  - `mlflow_service`: services.MlflowService
  - `alerts_service`: services.AlertsService
  - `logger_service`: services.LoggerService
  - `inputs_reader`: datasets.Reader
  - `tmp_outputs_writer`: datasets.Writer
  - `model_alias`: registries.Version
  - `loader`: registries.Loader
  - `capsys`: pc.CaptureFixture[str]
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
