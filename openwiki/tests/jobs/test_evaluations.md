---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_evaluations Documentation"
description: "Documentation for tests/jobs/test_evaluations.py"
tags: ["module", "test_evaluations"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/jobs/test_evaluations.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Infrastructure

**Dependencies**:
- `_pytest.capture`
- `regression_model_template`
- `pytest`
- `regression_model_template.core`
- `regression_model_template.io`

**Exported Symbols**:
- `test_evaluations_job`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
test_evaluations_job --> parametrize
test_evaluations_job --> isinstance
test_evaluations_job --> RunConfig
test_evaluations_job --> EvaluationsJob
test_evaluations_job --> get_experiment_by_name
test_evaluations_job --> search_runs
test_evaluations_job --> run
test_evaluations_job --> set
test_evaluations_job --> values
test_evaluations_job --> items
test_evaluations_job --> items
test_evaluations_job --> str
test_evaluations_job --> len
test_evaluations_job --> len
test_evaluations_job --> keys
test_evaluations_job --> keys
test_evaluations_job --> len
test_evaluations_job --> param
test_evaluations_job --> client
test_evaluations_job --> client
test_evaluations_job --> readouterr
test_evaluations_job --> Threshold
test_evaluations_job --> Threshold
test_evaluations_job --> Threshold
test_evaluations_job --> xfail
test_evaluations_job --> float
@enduml
```

## Classes
## Functions
### Function `test_evaluations_job`
- **Description**: No description available.
- **Inputs**:
  - `alias_or_version`: str | int
  - `thresholds`: dict[str, metrics.Threshold]
  - `mlflow_service`: services.MlflowService
  - `alerts_service`: services.AlertsService
  - `logger_service`: services.LoggerService
  - `inputs_reader`: datasets.ParquetReader
  - `targets_reader`: datasets.ParquetReader
  - `model_alias`: registries.Version
  - `metric`: metrics.Metric
  - `capsys`: pc.CaptureFixture[str]
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
