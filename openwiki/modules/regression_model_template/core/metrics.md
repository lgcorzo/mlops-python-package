---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Metrics & Evaluation Scorers"
source_path: "[[src/regression_model_template/core/metrics.py](../../../../src/regression_model_template/core/metrics.py)](../../../../[src/regression_model_template/core/metrics.py](../../../../src/regression_model_template/core/metrics.py))"
description: "Abstract metric definition, Scikit-Learn evaluation wrappers (RMSE, MAE, R2), and MLflow scorer exporters."
tags: ["core", "metrics", "rmse", "mae", "r2", "mlflow"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# Module Specification: Metrics & Evaluation Scorers

* **Source File Reference:** `[[src/regression_model_template/core/metrics.py](../../../../src/regression_model_template/core/metrics.py)](../../../../[src/regression_model_template/core/metrics.py](../../../../src/regression_model_template/core/metrics.py))` (Lines: L1-L148)
* **Upstream Dependencies:** `scikit-learn`, `mlflow`
* **Downstream Consumers:** [Modules/RegressionModelTemplate/Jobs/Evaluations](../jobs/evaluations.md), [Modules/RegressionModelTemplate/Jobs/Training](../jobs/training.md), [Modules/RegressionModelTemplate/Jobs/Tuning](../jobs/tuning.md)

## 1. Architectural Role & Responsibilities
`metrics.py` provides uniform metric wrappers for regression evaluation. Supports calculating RMSE, MAE, R2 scores, generating Scikit-Learn custom scorers, and logging evaluation metrics directly to MLflow.

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Metric {
        <<abstract>>
        +name: str
        +score(targets, outputs)* float
        +scorer(model, inputs, targets) float
        +to_mlflow()
    }
    class SklearnMetric {
        -metric_fn: Callable
        +score(targets, outputs) float
    }
    class Threshold {
        +metric: Metric
        +operator: str
        +value: float
        +to_mlflow()
    }

    Metric <|-- SklearnMetric : Inheritance
```

## 3. Class & Method Specifications

### `Metric` (`[[src/regression_model_template/core/metrics.py:L27-L95](../../../../src/regression_model_template/core/metrics.py#L27-L95)](../../../../[src/regression_model_template/core/metrics.py](../../../../src/regression_model_template/core/metrics.py)#L27-L95)`)
* `score(self, targets: np.ndarray, outputs: np.ndarray) -> float` (L44-L53): Abstract method computing metric score.
* `scorer(self, model, inputs, targets) -> float` (L55-L68): Generates Scikit-Learn compatible scoring function.
* `to_mlflow(self)` (L70-L95): Logs metric name and value to active MLflow run.

### `SklearnMetric` (`[[src/regression_model_template/core/metrics.py:L98-L117](../../../../src/regression_model_template/core/metrics.py#L98-L117)](../../../../[src/regression_model_template/core/metrics.py](../../../../src/regression_model_template/core/metrics.py)#L98-L117)`)
* `score(self, targets: np.ndarray, outputs: np.ndarray) -> float` (L111-L117): Wraps Scikit-Learn loss metrics (e.g. `root_mean_squared_error`).

### `Threshold` (`[[src/regression_model_template/core/metrics.py:L126-L148](../../../../src/regression_model_template/core/metrics.py#L126-L148)](../../../../[src/regression_model_template/core/metrics.py](../../../../src/regression_model_template/core/metrics.py)#L126-L148)`)
* `to_mlflow(self)` (L140-L148): Compares metric score against threshold constraint for model promotion gate checks.
