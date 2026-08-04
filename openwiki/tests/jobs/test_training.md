---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_training Documentation"
description: "Documentation for tests/jobs/test_training.py"
tags: ["module", "test_training"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/jobs/test_training.py`

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
- `test_training_job`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
test_training_job --> RunConfig
test_training_job --> client
test_training_job --> TrainingJob
test_training_job --> get_experiment_by_name
test_training_job --> search_runs
test_training_job --> get_model_version
test_training_job --> run
test_training_job --> set
test_training_job --> values
test_training_job --> items
test_training_job --> items
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> float
test_training_job --> float
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> len
test_training_job --> readouterr
@enduml
```

## Classes
## Functions
### Function `test_training_job`
- **Description**: No description available.
- **Inputs**:
  - `mlflow_service`: services.MlflowService
  - `alerts_service`: services.AlertsService
  - `logger_service`: services.LoggerService
  - `inputs_reader`: datasets.ParquetReader
  - `targets_reader`: datasets.ParquetReader
  - `model`: models.Model
  - `metric`: metrics.Metric
  - `train_test_splitter`: splitters.Splitter
  - `saver`: registries.Saver
  - `signer`: signers.Signer
  - `register`: registries.Register
  - `capsys`: pc.CaptureFixture[str]
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
