---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: metrics"
source_path: "src/regression_model_template/core/metrics.py"
description: "Evaluate model performances with metrics."
tags: ["module", "metrics"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: metrics

* **Source Reference:** [src/regression_model_template/core/metrics.py](../../../src/regression_model_template/core/metrics.py)

## 1. Architectural Role & Responsibilities
Evaluate model performances with metrics.

## 2. UML 2.0 Class Diagram
```plantuml
classDiagram
    direction BT
    class Metric {
        +KIND: str
        +name: str
        +greater_is_better: bool
        +score(self: Any, targets: schemas.Targets, outputs: schemas.Outputs) float
        +scorer(self: Any, model: models.Model, inputs: schemas.Inputs, targets: schemas.Targets) float
        +to_mlflow(self: Any) MlflowMetric
    }
    ABC <|-- Metric : Generalization
    BaseModel <|-- Metric : Generalization
    class SklearnMetric {
        +KIND: T.Literal~SklearnMetric~
        +name: str
        +greater_is_better: bool
        +score(self: Any, targets: schemas.Targets, outputs: schemas.Outputs) float
    }
    Metric <|-- SklearnMetric : Generalization
    class Threshold {
        +threshold: int | float
        +greater_is_better: bool
        +to_mlflow(self: Any) MlflowThreshold
    }
    ABC <|-- Threshold : Generalization
    BaseModel <|-- Threshold : Generalization
```

## 3. Class & Method Specifications

### `Metric`

Base class for a project metric.

Use metrics to evaluate model performance.
e.g., accuracy, precision, recall, MAE, F1, ...

Parameters:
    name (str): name of the metric for the reporting.
    greater_is_better (bool): maximize or minimize result.

#### Attributes
* **`KIND`** (`str`)
* **`name`** (`str`)
* **`greater_is_better`** (`bool`)

#### Public Methods
* **`score(self: Any, targets: schemas.Targets, outputs: schemas.Outputs) -> float`**
  - **Purpose**: Score the outputs against the targets.
  - **Inputs**:
    - `self` (`Any`)
    - `targets` (`schemas.Targets`)
    - `outputs` (`schemas.Outputs`)
  - **Outputs**: `float`
* **`scorer(self: Any, model: models.Model, inputs: schemas.Inputs, targets: schemas.Targets) -> float`**
  - **Purpose**: Score model outputs against targets.
  - **Inputs**:
    - `self` (`Any`)
    - `model` (`models.Model`)
    - `inputs` (`schemas.Inputs`)
    - `targets` (`schemas.Targets`)
  - **Outputs**: `float`
* **`to_mlflow(self: Any) -> MlflowMetric`**
  - **Purpose**: Convert the metric to an Mlflow metric.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `MlflowMetric`

### `SklearnMetric`

Compute metrics with sklearn.

Parameters:
    name (str): name of the sklearn metric.
    greater_is_better (bool): maximize or minimize.

#### Attributes
* **`KIND`** (`T.Literal[SklearnMetric]`)
* **`name`** (`str`)
* **`greater_is_better`** (`bool`)

#### Public Methods
* **`score(self: Any, targets: schemas.Targets, outputs: schemas.Outputs) -> float`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `targets` (`schemas.Targets`)
    - `outputs` (`schemas.Outputs`)
  - **Outputs**: `float`

### `Threshold`

A project threshold for a metric.

Use thresholds to monitor model performances.
e.g., to trigger an alert when a threshold is met.

Parameters:
    threshold (int | float): absolute threshold value.
    greater_is_better (bool): maximize or minimize result.

#### Attributes
* **`threshold`** (`int | float`)
* **`greater_is_better`** (`bool`)

#### Public Methods
* **`to_mlflow(self: Any) -> MlflowThreshold`**
  - **Purpose**: Convert the threshold to an mlflow threshold.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `MlflowThreshold`

## Dependencies

* `__future__.annotations`
* `abc`
* `typing`
* `mlflow`
* `pandas`
* `pydantic`
* `mlflow.metrics.MetricValue`
* `sklearn.metrics`
* `regression_model_template.core.models`
* `regression_model_template.core.schemas`

## Used By

* [evaluations.py](../../regression_model_template/jobs/evaluations.md)
* [training.py](../../regression_model_template/jobs/training.md)
* [tuning.py](../../regression_model_template/jobs/tuning.md)
* [searchers.py](../../regression_model_template/utils/searchers.md)
