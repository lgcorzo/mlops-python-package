---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Model Wrappers"
source_path: "src/regression_model_template/core/models.py"
description: "Abstract model wrapper interface and Scikit-Learn baseline model implementation with SHAP explainability."
tags: ["core", "models", "sklearn", "shap", "wrapper"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
---

# Module Specification: Model Wrappers

* **Source File Reference:** `src/regression_model_template/core/models.py` (Lines: L1-L220)
* **Upstream Dependencies:** `scikit-learn`, `shap`, `pandas`, `numpy`
* **Downstream Consumers:** [[Modules/RegressionModelTemplate/Jobs/Training]], [[Modules/RegressionModelTemplate/Jobs/Inference]], [[Modules/RegressionModelTemplate/Jobs/Explanations]]

## 1. Architectural Role & Responsibilities
`models.py` defines the abstract base `Model` contract and `BaselineSklearnModel` wrapper. Standardizes `fit()`, `predict()`, `explain_model()`, and `explain_samples()` methods across all model architectures.

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Model {
        <<abstract>>
        +get_params(deep: bool) Dict
        +set_params()
        +fit(inputs, targets)* Model
        +predict(inputs)* ndarray
        +explain_model()*
        +explain_samples(inputs)*
        +get_internal_model()* Any
    }
    class BaselineSklearnModel {
        -model: Pipeline
        +fit(inputs, targets) BaselineSklearnModel
        +predict(inputs) ndarray
        +explain_model() SHAPExplanation
        +explain_samples(inputs) SHAPExplanation
        +get_internal_model() Pipeline
    }

    Model <|-- BaselineSklearnModel : Realization
```

## 3. Class & Method Specifications

### `Model` (`src/regression_model_template/core/models.py:L24-L122`)
* `get_params(self, deep=True)` (L33-L46): Returns model hyperparameters dictionary.
* `fit(self, inputs, targets)` (L69-L78): Abstract fitting method.
* `predict(self, inputs)` (L81-L89): Abstract prediction method.
* `explain_model(self)` (L91-L100): Abstract global model explainability method.

### `BaselineSklearnModel` (`src/regression_model_template/core/models.py:L125-L220`)
* `fit(self, inputs, targets) -> BaselineSklearnModel` (L161-L183): Trains underlying Scikit-Learn Pipeline on feature matrix.
* `predict(self, inputs) -> np.ndarray` (L185-L189): Generates numerical regression predictions.
* `explain_model(self)` (L191-L202): Computes SHAP TreeExplainer/LinearExplainer global feature importances.
* `explain_samples(self, inputs)` (L204-L214): Computes local SHAP explanations for specific sample rows.
