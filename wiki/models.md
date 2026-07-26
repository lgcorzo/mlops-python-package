---
type: script
title: "models"
source_path: "src/regression_model_template/core/models.py"
description: "Define trainable machine learning models."
tags: [script, regression_model_template]
last_verified_commit: "abe2ee0"
---

# models

Source File: `src/regression_model_template/core/models.py`

Define trainable machine learning models.

```mermaid
classDiagram
    class Model {
        +KIND
        +get_params(deep)
        +set_params()
        +__sklearn_tags__()
        +fit(inputs, targets)
        +predict(inputs)
        +explain_model()
        +explain_samples(inputs)
        +get_internal_model()
    }
    Model <|-- BaselineSklearnModel
    class BaselineSklearnModel {
        +KIND
        +max_depth
        +n_estimators
        +random_state
        +_pipeline
        +_numericals
        +_categoricals
        +fit(inputs, targets)
        +predict(inputs)
        +explain_model()
        +explain_samples(inputs)
        +get_internal_model()
    }
```

```mermaid
flowchart TD
    models --> abc
    models --> typing
    models --> pydantic
    models --> shap
    models --> sklearn
    models --> regression_model_template_core
```
