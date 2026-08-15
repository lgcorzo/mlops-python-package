---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_metrics"
source_path: "tests/core/test_metrics.py"
description: "No description available."
tags: ["module", "test_metrics"]
timestamp: "2026-08-15T05:57:16Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: test_metrics

* **Source Reference:** [tests/core/test_metrics.py](../../../../tests/core/test_metrics.py)

## 1. Architectural Role & Responsibilities
No description available.

### Detected Architecture Patterns
Detected roles: General Subsystem

## 2. UML Diagrams
### Class Diagram
_No classes found._

### Sequence Diagram
```plantuml
sequenceDiagram
    test_sklearn_metric->>parametrize: invoke
    test_sklearn_metric->>concat: invoke
    test_sklearn_metric->>SklearnMetric: invoke
    test_sklearn_metric->>score: invoke
    test_sklearn_metric->>scorer: invoke
    test_sklearn_metric->>to_mlflow: invoke
    test_sklearn_metric->>evaluate: invoke
    test_sklearn_metric->>float: invoke
    test_threshold->>Threshold: invoke
    test_threshold->>to_mlflow: invoke
```

### Component Diagram
```plantuml
component [test_metrics] as Comp
Comp --> [mlflow]
Comp --> [pandas]
Comp --> [pytest]
Comp --> [metrics]
Comp --> [models]
Comp --> [schemas]
```

## 3. Class & Method Specifications

## Standalone Functions

### `test_sklearn_metric(name: str, interval: tuple[(int, int)], greater_is_better: bool, model: models.Model, inputs: schemas.Inputs, targets: schemas.Targets, outputs: schemas.Outputs) -> None`
No description available.

#### Inputs
* `name` (`str`)
* `interval` (`tuple[(int, int)]`)
* `greater_is_better` (`bool`)
* `model` (`models.Model`)
* `inputs` (`schemas.Inputs`)
* `targets` (`schemas.Targets`)
* `outputs` (`schemas.Outputs`)

#### Outputs
* `None`

### `test_threshold() -> None`
No description available.

#### Inputs

#### Outputs
* `None`

## Dependencies

* `mlflow`
* `pandas`
* `pytest`
* `regression_model_template.core.metrics`
* `regression_model_template.core.models`
* `regression_model_template.core.schemas`

## Used By

_Not used by any other module._
