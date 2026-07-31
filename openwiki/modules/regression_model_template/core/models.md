---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Model Wrappers"
source_path: "[[[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)))](../../../../[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))))](../../../../[[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)))](../../../../[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)))))"
description: "Abstract model wrapper interface and Scikit-Learn baseline model implementation with SHAP explainability."
tags: ["core", "models", "sklearn", "shap", "wrapper"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# Module Specification: Model Wrappers

* **Source File Reference:** `[[[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)))](../../../../[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))))](../../../../[[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)))](../../../../[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)))))` (Lines: L1-L220)
* **Upstream Dependencies:** `scikit-learn`, `shap`, `pandas`, `numpy`
* **Downstream Consumers:** [Modules/RegressionModelTemplate/Jobs/Training](../jobs/training.md), [Modules/RegressionModelTemplate/Jobs/Inference](../jobs/inference.md), [Modules/RegressionModelTemplate/Jobs/Explanations](../jobs/explanations.md)

## 1. Architectural Role & Responsibilities
`models.py` defines the abstract base `Model` contract and `BaselineSklearnModel` wrapper. Standardizes `fit()`, `predict()`, `explain_model()`, and `explain_samples()` methods across all model architectures.

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Model {
        <<abstract>>
        +KIND: str
        +get_params(deep: bool) Params
        +set_params(**params) Self
        +__sklearn_tags__() Any
        +fit(inputs: Inputs, targets: Targets)* Self
        +predict(inputs: Any)* Outputs
        +explain_model() FeatureImportances
        +explain_samples(inputs: Inputs) SHAPValues
        +get_internal_model()* Any
    }
    class BaselineSklearnModel {
        +KIND: Literal
        +max_depth: int
        +n_estimators: int
        +random_state: int
        -_pipeline: Pipeline
        -_numericals: list~str~
        -_categoricals: list~str~
        +fit(inputs: Inputs, targets: Targets) BaselineSklearnModel
        +predict(inputs: Any) Outputs
        +explain_model() FeatureImportances
        +explain_samples(inputs: Inputs) SHAPValues
        +get_internal_model() Pipeline
    }

    Model <|-- BaselineSklearnModel : Generalization
```

## 3. Class & Method Specifications

### `Model` (`[[[[[src/regression_model_template/core/models.py:L24-L122](../../../../src/regression_model_template/core/models.py#L24-L122)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)#L24-L122)](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))#L24-L122)](../../../../[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)))#L24-L122)](../../../../[[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)))](../../../../[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))))#L24-L122)`)
* `get_params(self, deep=True)` (L33-L46): Returns model hyperparameters dictionary.
* `fit(self, inputs, targets)` (L69-L78): Abstract fitting method.
* `predict(self, inputs)` (L81-L89): Abstract prediction method.
* `explain_model(self)` (L91-L100): Abstract global model explainability method.

### `BaselineSklearnModel` (`[[[[[src/regression_model_template/core/models.py:L125-L220](../../../../src/regression_model_template/core/models.py#L125-L220)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)#L125-L220)](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))#L125-L220)](../../../../[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)))#L125-L220)](../../../../[[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)))](../../../../[[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))](../../../../[[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)](../../../../[src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py))))#L125-L220)`)
* `fit(self, inputs, targets) -> BaselineSklearnModel` (L161-L183): Trains underlying Scikit-Learn Pipeline on feature matrix.
* `predict(self, inputs) -> np.ndarray` (L185-L189): Generates numerical regression predictions.
* `explain_model(self)` (L191-L202): Computes SHAP TreeExplainer/LinearExplainer global feature importances.
* `explain_samples(self, inputs)` (L204-L214): Computes local SHAP explanations for specific sample rows.

## 4. Execution Workflow Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    participant Job as TrainingJob / InferenceJob
    participant Model as BaselineSklearnModel
    participant Pipeline as scikit-learn Pipeline
    participant Explainer as shap TreeExplainer

    Note over Job, Model: Fitting Flow
    Job->>Model: fit(inputs, targets)
    activate Model
    Model->>Pipeline: fit(X, y)
    activate Pipeline
    Pipeline-->>Model: fitted pipeline
    deactivate Pipeline
    Model-->>Job: self (fitted model)
    deactivate Model

    Note over Job, Model: Inference & Prediction Flow
    Job->>Model: predict(inputs)
    activate Model
    Model->>Model: get_internal_model()
    Model->>Pipeline: predict(inputs)
    activate Pipeline
    Pipeline-->>Model: numpy prediction array
    deactivate Pipeline
    Model-->>Job: Outputs(prediction)
    deactivate Model

    Note over Job, Model: SHAP Sample Explanation Flow
    Job->>Model: explain_samples(inputs)
    activate Model
    Model->>Model: get_internal_model()
    Model->>Pipeline: transform(inputs)
    activate Pipeline
    Pipeline-->>Model: transformed features
    deactivate Pipeline
    Model->>Explainer: TreeExplainer(regressor)
    activate Explainer
    Explainer-->>Model: explainer instance
    deactivate Explainer
    Model->>Explainer: shap_values(transformed)
    activate Explainer
    Explainer-->>Model: array of SHAP values
    deactivate Explainer
    Model-->>Job: SHAPValues(data)
    deactivate Model
```
