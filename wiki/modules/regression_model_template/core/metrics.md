---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::core::metrics — Metric Evaluation Abstractions"
source_path: "src/regression_model_template/core/metrics.py"
description: "Abstract Metric base class, Scikit-Learn metric wrapper, and MLflow threshold evaluators."
tags: ["iso42010", "okf", "component_view", "metrics", "sklearn"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::core::metrics — Metric Evaluation Abstractions

> **Source**: `src/regression_model_template/core/metrics.py` (Lines: L1-L148)  
> **Layer**: Domain  
> **Role**: Encapsulates regression evaluation scoring functions, threshold criteria, and MLflow serialization.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Metric {
        <<abstract>>
        +str KIND
        +str name
        +bool greater_is_better
        +score(targets: Targets, outputs: Outputs) float*
        +scorer(model: Model, inputs: Inputs, targets: Targets) float
        +to_mlflow() MlflowMetric
    }

    class SklearnMetric {
        +str KIND = "SklearnMetric"
        +str name
        +bool greater_is_better
        +score(targets: Targets, outputs: Outputs) float
    }
    SklearnMetric --|> Metric : implements

    class Threshold {
        +float threshold
        +bool greater_is_better
        +to_mlflow() MlflowThreshold
    }
```

---

## 2. Method Contracts

### `Metric.score(self, targets: schemas.Targets, outputs: schemas.Outputs) -> float`
- **Source Citation**: `src/regression_model_template/core/metrics.py:L44-L53`
- **Visibility**: Public (`+`)
- **Behavior**: Evaluates predictive quality between true targets and model predictions.

---

> *Related: [Models](models.md) · [Evaluations Job](../jobs/evaluations.md)*
