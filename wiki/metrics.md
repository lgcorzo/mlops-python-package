---
type: script
title: "metrics"
source_path: "src/regression_model_template/core/metrics.py"
description: "Evaluate model performances with metrics."
tags: [script, regression_model_template]
last_verified_commit: "c0c5dbc"
---

# metrics

Source File: `src/regression_model_template/core/metrics.py`

Evaluate model performances with metrics.

```mermaid
classDiagram
    class Metric {
        +KIND
        +name
        +greater_is_better
        +score(targets, outputs) : float
        +scorer(model, inputs, targets) : float
        +to_mlflow() : MlflowMetric
    }
    class SklearnMetric {
        +KIND
        +name
        +greater_is_better
        +score(targets, outputs) : float
    }
    Metric <|-- SklearnMetric
    class Threshold {
        +threshold
        +greater_is_better
        +to_mlflow() : MlflowThreshold
    }
```

```mermaid
flowchart TD

    metrics --> __future__
    metrics --> abc
    metrics --> mlflow
    metrics --> mlflow_metrics
    metrics --> pandas
    metrics --> pydantic
    metrics --> regression_model_template_core
    metrics --> sklearn
    metrics --> typing
```
