---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "specification"
title: "ISO 15289 Specification — Public API & Interface Specification"
description: "Complete API specification detailing CLI entry points, class constructors, method parameters, return types, and exceptions."
tags: ["iso15289", "api", "contracts", "interface"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# ISO 15289 Specification: Public API & Interface Specification

## 1. CLI Commands ([`src/regression_model_template/scripts.py:L1-L55`](/src/regression_model_template/scripts.py#L1-L55))

The system provides a command-line interface entry point registered in `pyproject.toml` as `regression_model_template`:

```bash
regression_model_template [JOB_NAME] --config-path [PATH] --config-name [NAME]
```

### Available CLI Commands:
* `train` — Executes `TrainingJob` ([`src/regression_model_template/jobs/training.py:L21-L145`](/src/regression_model_template/jobs/training.py#L21-L145)).
* `tune` — Executes `TuningJob` ([`src/regression_model_template/jobs/tuning.py:L18-L104`](/src/regression_model_template/jobs/tuning.py#L18-L104)).
* `evaluate` — Executes `EvaluationsJob` ([`src/regression_model_template/jobs/evaluations.py:L19-L125`](/src/regression_model_template/jobs/evaluations.py#L19-L125)).
* `explain` — Executes `ExplanationsJob` ([`src/regression_model_template/jobs/explanations.py:L16-L78`](/src/regression_model_template/jobs/explanations.py#L16-L78)).
* `promote` — Executes `PromotionJob` ([`src/regression_model_template/jobs/promotion.py:L12-L57`](/src/regression_model_template/jobs/promotion.py#L12-L57)).
* `infer` — Executes `InferenceJob` ([`src/regression_model_template/jobs/inference.py:L17-L66`](/src/regression_model_template/jobs/inference.py#L17-L66)).

---

## 2. Core Class Interface Specifications

### A. `Model` Interface ([`src/regression_model_template/core/models.py:L24-L122`](/src/regression_model_template/core/models.py#L24-L122))

```python
class Model:
    def fit(self, inputs: pd.DataFrame, targets: pd.Series) -> "Model": ...
    def predict(self, inputs: pd.DataFrame) -> np.ndarray: ...
    def explain_model((self) -> Any: ...
    def explain_samples(self, inputs: pd.DataFrame) -> Any: ...
    def get_internal_model(self) -> Any: ...
```

#### Method Specifications:
* `fit(inputs: pd.DataFrame, targets: pd.Series) -> Model`
  * **Line Citation:** [`src/regression_model_template/core/models.py:L69-L78`](/src/regression_model_template/core/models.py#L69-L78)
  * **Description:** Fits underlying regression estimator on input feature matrix and target values.
  * **Throws:** `ValueError` if feature shapes mismatch schema bounds.

* `predict(inputs: pd.DataFrame) -> np.ndarray`
  * **Line Citation:** [`src/regression_model_template/core/models.py:L81-L89`](/src/regression_model_template/core/models.py#L81-L89)
  * **Description:** Computes regression predictions for provided input features.
  * **Returns:** 1D or 2D `np.ndarray` of predicted continuous values.

---

### B. `FastAPIKafkaService` ([`src/regression_model_template/controller/kafka_app.py:L184-L386`](/src/regression_model_template/controller/kafka_app.py#L184-L386))

```python
class FastAPIKafkaService:
    def __init__(self, prediction_callback: Callable, kafka_config: dict, input_topic: str, output_topic: str): ...
    def start(self): ...
    def stop(self): ...
```

#### Parameters:
| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `prediction_callback` | `Callable` | Required | Callback function invoking `PredictionService.predict()`. |
| `kafka_config` | `dict` | Required | Kafka consumer/producer bootstrap configuration. |
| `input_topic` | `str` | Required | Kafka topic to consume input records from. |
| `output_topic` | `str` | Required | Kafka topic to publish inference responses to. |
