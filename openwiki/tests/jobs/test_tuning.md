---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_tuning Documentation"
description: "Documentation for tests/jobs/test_tuning.py"
tags: ["module", "test_tuning"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/jobs/test_tuning.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Infrastructure

**Dependencies**:
- `_pytest.capture`
- `regression_model_template`
- `regression_model_template.core`
- `regression_model_template.io`
- `regression_model_template.utils`

**Exported Symbols**:
- `test_tuning_job`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
test_tuning_job --> RunConfig
test_tuning_job --> client
test_tuning_job --> TuningJob
test_tuning_job --> get_experiment_by_name
test_tuning_job --> search_runs
test_tuning_job --> run
test_tuning_job --> set
test_tuning_job --> values
test_tuning_job --> items
test_tuning_job --> items
test_tuning_job --> float
test_tuning_job --> float
test_tuning_job --> keys
test_tuning_job --> keys
test_tuning_job --> len
test_tuning_job --> len
test_tuning_job --> readouterr
@enduml
```

## Classes
## Functions
### Function `test_tuning_job`
- **Description**: No description available.
- **Inputs**:
  - `mlflow_service`: services.MlflowService
  - `alerts_service`: services.AlertsService
  - `logger_service`: services.LoggerService
  - `inputs_reader`: datasets.ParquetReader
  - `targets_reader`: datasets.ParquetReader
  - `model`: models.Model
  - `metric`: metrics.Metric
  - `time_series_splitter`: splitters.Splitter
  - `searcher`: searchers.Searcher
  - `capsys`: pc.CaptureFixture[str]
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
