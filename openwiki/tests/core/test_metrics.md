---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "test_metrics Documentation"
description: "Documentation for tests/core/test_metrics.py"
tags: ["module", "test_metrics"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/core/test_metrics.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Infrastructure

**Dependencies**:
- `pandas`
- `pytest`
- `mlflow`
- `regression_model_template.core`

**Exported Symbols**:
- `test_sklearn_metric`
- `test_threshold`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
test_sklearn_metric --> parametrize
test_sklearn_metric --> concat
test_sklearn_metric --> SklearnMetric
test_sklearn_metric --> score
test_sklearn_metric --> scorer
test_sklearn_metric --> to_mlflow
test_sklearn_metric --> evaluate
test_sklearn_metric --> float
test_sklearn_metric --> float
test_threshold --> Threshold
test_threshold --> to_mlflow
@enduml
```

## Classes
## Functions
### Function `test_sklearn_metric`
- **Description**: No description available.
- **Inputs**:
  - `name`: str
  - `interval`: tuple[int, int]
  - `greater_is_better`: bool
  - `model`: models.Model
  - `inputs`: schemas.Inputs
  - `targets`: schemas.Targets
  - `outputs`: schemas.Outputs
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `test_threshold`
- **Description**: No description available.
- **Inputs**:
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
