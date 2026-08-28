---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_metrics"
source_path: "tests/core/test_metrics.py"
description: "No description available."
tags: ["module", "test_metrics"]
timestamp: "2026-08-28T06:13:58Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "3029bb6"
---
# Module Specification: test_metrics

* **Source Reference:** [tests/core/test_metrics.py](../../../../tests/core/test_metrics.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `mlflow`

* `pandas`

* `pytest`

* `regression_model_template.core.metrics`

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

# Each File Documentation

## Imported modules

* `mlflow`

* `pandas`

* `pytest`

* `regression_model_template.core.metrics`

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

## Exported functions

* `test_sklearn_metric`

* `test_threshold`

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

### Description

No description available.

### Inputs

* `name`

  - **type**: str

  - **optional?**: No

* `interval`

  - **type**: tuple[(int, int)]

  - **optional?**: No

* `greater_is_better`

  - **type**: bool

  - **optional?**: No

* `model`

  - **type**: models.Model

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

* `outputs`

  - **type**: schemas.Outputs

  - **optional?**: No

### Output

* **return type**: None

### `test_threshold() -> None`

### Description

No description available.

### Inputs

### Output

* **return type**: None

## Used By

_Not used by any other module._
