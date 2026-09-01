---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: metrics"
source_path: "src/regression_model_template/core/metrics.py"
description: "Evaluate model performances with metrics."
tags: ["module", "metrics"]
timestamp: "2026-09-01T16:59:35Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "193029c"
---
# Module Specification: metrics

* **Source Reference:** [src/regression_model_template/core/metrics.py](../../../../src/regression_model_template/core/metrics.py)

# Module Overview

## Purpose

Evaluate model performances with metrics.

## Responsibilities

Evaluate model performances with metrics.

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

# Each File Documentation

## Imported modules

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

## Exported classes

* `Metric`

* `SklearnMetric`

* `Threshold`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

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

### Sequence Diagram

```plantuml
sequenceDiagram
    Metric.scorer->>predict: invoke
    Metric.scorer->>score: invoke
    Metric.to_mlflow->>make_metric: invoke
    Metric.to_mlflow->>Targets: invoke
    Metric.to_mlflow->>Outputs: invoke
    Metric.to_mlflow->>score: invoke
    Metric.to_mlflow->>MlflowMetric: invoke
    SklearnMetric.score->>getattr: invoke
    SklearnMetric.score->>float: invoke
    SklearnMetric.score->>metric: invoke
    Threshold.to_mlflow->>MlflowThreshold: invoke
```

### Component Diagram

```plantuml
component [metrics] as Comp
Comp --> [annotations]
Comp --> [abc]
Comp --> [typing]
Comp --> [mlflow]
Comp --> [pandas]
Comp --> [pydantic]
Comp --> [MetricValue]
Comp --> [metrics]
Comp --> [models]
Comp --> [schemas]
```

## 3. Class & Method Specifications

# Public Classes

### `Metric`

## Overview

Base class for a project metric.

Use metrics to evaluate model performance.
e.g., accuracy, precision, recall, MAE, F1, ...

Parameters:
    name (str): name of the metric for the reporting.
    greater_is_better (bool): maximize or minimize result.

## Attributes

* **`KIND`**

  - **Type**: str

* **`name`**

  - **Type**: str

* **`greater_is_better`**

  - **Type**: bool

## Public Methods

* **`score(self: Any, targets: schemas.Targets, outputs: schemas.Outputs) -> float`**

### Description

Score the outputs against the targets.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

* `outputs`

  - **type**: schemas.Outputs

  - **optional?**: No

### Output

* **return type**: float

* **`scorer(self: Any, model: models.Model, inputs: schemas.Inputs, targets: schemas.Targets) -> float`**

### Description

Score model outputs against targets.

### Inputs

* `self`

  - **type**: Any

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

### Output

* **return type**: float

* **`to_mlflow(self: Any) -> MlflowMetric`**

### Description

Convert the metric to an Mlflow metric.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

### Output

* **return type**: MlflowMetric

### `SklearnMetric`

## Overview

Compute metrics with sklearn.

Parameters:
    name (str): name of the sklearn metric.
    greater_is_better (bool): maximize or minimize.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[SklearnMetric]

* **`name`**

  - **Type**: str

* **`greater_is_better`**

  - **Type**: bool

## Public Methods

* **`score(self: Any, targets: schemas.Targets, outputs: schemas.Outputs) -> float`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **optional?**: No

* `outputs`

  - **type**: schemas.Outputs

  - **optional?**: No

### Output

* **return type**: float

### `Threshold`

## Overview

A project threshold for a metric.

Use thresholds to monitor model performances.
e.g., to trigger an alert when a threshold is met.

Parameters:
    threshold (int | float): absolute threshold value.
    greater_is_better (bool): maximize or minimize result.

## Attributes

* **`threshold`**

  - **Type**: int | float

* **`greater_is_better`**

  - **Type**: bool

## Public Methods

* **`to_mlflow(self: Any) -> MlflowThreshold`**

### Description

Convert the threshold to an mlflow threshold.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

### Output

* **return type**: MlflowThreshold

## Used By

* [evaluations.py](../../regression_model_template/jobs/evaluations.md)

* [training.py](../../regression_model_template/jobs/training.md)

* [tuning.py](../../regression_model_template/jobs/tuning.md)

* [searchers.py](../../regression_model_template/utils/searchers.md)

* [conftest.py](../../tests/conftest.md)

* [test_metrics.py](../../tests/core/test_metrics.md)

* [test_evaluations.py](../../tests/jobs/test_evaluations.md)

* [test_training.py](../../tests/jobs/test_training.md)

* [test_tuning.py](../../tests/jobs/test_tuning.md)

* [test_searchers.py](../../tests/utils/test_searchers.md)
