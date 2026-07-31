---
type: "module-architecture"
title: "models"
description: "Technical architecture and class hierarchy for models"
tags: ["architecture", "uml", "pyreverse", "openwiki"]
timestamp: "2026-07-30T19:10:46Z"
---

# Module Name: models

Source File: `src/regression_model_template/core/models.py`
* **Source Directory Reference:** `src/regression_model_template/core/`
* **Package Dependency:** Upstream: `sklearn`, `pydantic`, `abc`, `shap`, `typing`, `regression_model_template.core`, `sklearn.base` | Downstream: None

## 1. Executive Summary & Purpose
Deterministic architectural model extracted via AST parsing for module `models`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)
The following class diagram models the object-oriented structure, explicit inheritance hierarchies, and polymorphic interface implementations derived from local AST analysis:

```mermaid
classDiagram
    class Model {
        +KIND
        +get_params(deep) : Params
        +set_params() : Any
        -__sklearn_tags__() : Any
        +fit(inputs, targets) : Any
        +predict(inputs) : Any
        +explain_model() : Any
        +explain_samples(inputs) : Any
        +get_internal_model() : Any
    }
    class BaselineSklearnModel {
        +KIND
        +max_depth
        +n_estimators
        +random_state
        #_pipeline
        #_numericals
        #_categoricals
        +fit(inputs, targets) : Any
        +predict(inputs) : Any
        +explain_model() : Any
        +explain_samples(inputs) : Any
        +get_internal_model() : Any
    }
    Model <|-- BaselineSklearnModel
```

## 3. Package & Class Relations

The following diagram defines the package boundaries and directional inter-package dependencies:

```mermaid
classDiagram
    class Model {
        +KIND
        +get_params(deep) : Params
        +set_params() : Any
        -__sklearn_tags__() : Any
        +fit(inputs, targets) : Any
        +predict(inputs) : Any
        +explain_model() : Any
        +explain_samples(inputs) : Any
        +get_internal_model() : Any
    }
    class BaselineSklearnModel {
        +KIND
        +max_depth
        +n_estimators
        +random_state
        #_pipeline
        #_numericals
        #_categoricals
        +fit(inputs, targets) : Any
        +predict(inputs) : Any
        +explain_model() : Any
        +explain_samples(inputs) : Any
        +get_internal_model() : Any
    }
    Model <|-- BaselineSklearnModel
```

* **Inheritance & Polymorphism:** Detailed breakdown of abstract base classes, interfaces, and concrete overrides.
* **Dependencies:** How classes within this package collaborate externally.

## 4. Execution Flow & Runtime Behavior

The following sequence diagram outlines the execution lifecycle and message passing during core operations:

```mermaid
sequenceDiagram
    autonumber
    participant Caller as Client Interface
    participant Model as Model
    Caller->>Model: get_params()
    Note over Model: Execution of get_params
    Model->>Model: internal isupper()
    Model->>Model: internal startswith()
    Model-->>Caller: Returns status
    participant BaselineSklearnModel as BaselineSklearnModel
    Caller->>BaselineSklearnModel: fit()
    Note over BaselineSklearnModel: Execution of fit
    BaselineSklearnModel->>BaselineSklearnModel: internal ColumnTransformer()
    BaselineSklearnModel->>BaselineSklearnModel: internal OneHotEncoder()
    BaselineSklearnModel-->>Caller: Returns status
```

---

* **Source Citations:**
  - Class `Model`: `src/regression_model_template/core/models.py:24`
  - Method `get_params`: `src/regression_model_template/core/models.py:33`
  - Method `set_params`: `src/regression_model_template/core/models.py:48`
  - Method `__sklearn_tags__`: `src/regression_model_template/core/models.py:58`
  - Method `fit`: `src/regression_model_template/core/models.py:69`
  - Method `predict`: `src/regression_model_template/core/models.py:81`
  - Method `explain_model`: `src/regression_model_template/core/models.py:91`
  - Method `explain_samples`: `src/regression_model_template/core/models.py:102`
  - Method `get_internal_model`: `src/regression_model_template/core/models.py:113`
  - Class `BaselineSklearnModel`: `src/regression_model_template/core/models.py:125`
  - Method `fit`: `src/regression_model_template/core/models.py:161`
  - Method `predict`: `src/regression_model_template/core/models.py:185`
  - Method `explain_model`: `src/regression_model_template/core/models.py:191`
  - Method `explain_samples`: `src/regression_model_template/core/models.py:204`
  - Method `get_internal_model`: `src/regression_model_template/core/models.py:216`

```mermaid
flowchart TD
    models --> abc
    models --> pydantic
    models --> regression_model_template_core
    models --> shap
    models --> sklearn
    models --> sklearn_base
    models --> typing
```
