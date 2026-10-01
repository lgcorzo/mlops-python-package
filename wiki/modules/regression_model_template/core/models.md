---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::core::models — Model Abstraction & Baselines"
source_path: "src/regression_model_template/core/models.py"
description: "Abstract Model interface with Pydantic validation, Scikit-Learn pipeline wrapper, and SHAP explainability hooks."
tags: ["iso42010", "okf", "component_view", "models", "scikit_learn", "shap"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::core::models — Model Abstraction & Baselines

> **Source**: `src/regression_model_template/core/models.py` (Lines: L1-L223)  
> **Layer**: Domain  
> **Role**: Unified model contract ensuring consistent fit, predict, parameter inspection, and SHAP explainability across any regression estimator.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Model {
        <<abstract>>
        +str KIND
        +get_params(deep: bool = True) Params
        +set_params(**params) Self
        +fit(inputs: Inputs, targets: Targets) Self*
        +predict(inputs: Any) Outputs*
        +explain_model() FeatureImportances*
        +explain_samples(inputs: Inputs) SHAPValues*
        +get_internal_model() Any*
    }

    class BaselineSklearnModel {
        +str KIND = "BaselineSklearnModel"
        +int max_depth
        +int n_estimators
        +int random_state
        -Pipeline _pipeline
        +fit(inputs: Inputs, targets: Targets) BaselineSklearnModel
        +predict(inputs: Any) Outputs
        +explain_model() FeatureImportances
        +explain_samples(inputs: Inputs) SHAPValues
        +get_internal_model() Pipeline
    }
    BaselineSklearnModel --|> Model : implements
```

---

## 2. Method Contracts

### `BaselineSklearnModel.fit(self, inputs: schemas.Inputs, targets: schemas.Targets) -> 'BaselineSklearnModel'`
- **Source Citation**: `src/regression_model_template/core/models.py:L161-L183`
- **Visibility**: Public (`+`)
- **Behavior**: Assembles Scikit-Learn preprocessing transformers and Random Forest regressor, fitting estimator on validated inputs and targets.

### `BaselineSklearnModel.explain_samples(self, inputs: schemas.Inputs) -> schemas.SHAPValues`
- **Source Citation**: `src/regression_model_template/core/models.py:L204-L214`
- **Visibility**: Public (`+`)
- **Behavior**: Invokes SHAP `TreeExplainer` on the underlying fitted tree models to calculate local Shapley attribution values.

---

> *Related: [Metrics](metrics.md) · [Schemas](schemas.md) · [Training Job](../jobs/training.md)*
