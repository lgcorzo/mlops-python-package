---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: models"
source_path: "src/regression_model_template/core/models.py"
description: "Define trainable machine learning models."
tags: ["module", "models"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: models

* **Source Reference:** [src/regression_model_template/core/models.py](../../../src/regression_model_template/core/models.py)

## 1. Architectural Role & Responsibilities
Define trainable machine learning models.

## 2. UML 2.0 Class Diagram
```plantuml
classDiagram
    direction BT
    class Model {
        +KIND: str
        +get_params(self: Any, deep: bool) Params
        +set_params(self: Any, **params: ParamValue) T.Self
        +__sklearn_tags__(self: Any) T.Any
        +fit(self: Any, inputs: schemas.Inputs, targets: schemas.Targets) T.Self
        +predict(self: Any, inputs: T.Any) schemas.Outputs
        +explain_model(self: Any) schemas.FeatureImportances
        +explain_samples(self: Any, inputs: schemas.Inputs) schemas.SHAPValues
        +get_internal_model(self: Any) T.Any
    }
    ABC <|-- Model : Generalization
    BaseModel <|-- Model : Generalization
    class BaselineSklearnModel {
        +KIND: T.Literal~BaselineSklearnModel~
        +max_depth: int
        +n_estimators: int
        +random_state: int | None
        +_pipeline: pipeline.Pipeline | None
        +_numericals: list~str~
        +_categoricals: list~str~
        +fit(self: Any, inputs: schemas.Inputs, targets: schemas.Targets) BaselineSklearnModel
        +predict(self: Any, inputs: T.Any) schemas.Outputs
        +explain_model(self: Any) schemas.FeatureImportances
        +explain_samples(self: Any, inputs: schemas.Inputs) schemas.SHAPValues
        +get_internal_model(self: Any) pipeline.Pipeline
    }
    Model <|-- BaselineSklearnModel : Generalization
```

## 3. Class & Method Specifications

### `Model`

Base class for a project model.

Use a model to adapt AI/ML frameworks.
e.g., to swap easily one model with another.

#### Attributes
* **`KIND`** (`str`)

#### Public Methods
* **`get_params(self: Any, deep: bool) -> Params`**
  - **Purpose**: Get the model params.
  - **Inputs**:
    - `self` (`Any`)
    - `deep` (`bool`)
  - **Outputs**: `Params`
* **`set_params(self: Any, **params: ParamValue) -> T.Self`**
  - **Purpose**: Set the model params in place.
  - **Inputs**:
    - `self` (`Any`)
    - `**params` (`ParamValue`)
  - **Outputs**: `T.Self`
* **`fit(self: Any, inputs: schemas.Inputs, targets: schemas.Targets) -> T.Self`**
  - **Purpose**: Fit the model on the given inputs and targets.
  - **Inputs**:
    - `self` (`Any`)
    - `inputs` (`schemas.Inputs`)
    - `targets` (`schemas.Targets`)
  - **Outputs**: `T.Self`
* **`predict(self: Any, inputs: T.Any) -> schemas.Outputs`**
  - **Purpose**: Generate outputs with the model for the given inputs.
  - **Inputs**:
    - `self` (`Any`)
    - `inputs` (`T.Any`)
  - **Outputs**: `schemas.Outputs`
* **`explain_model(self: Any) -> schemas.FeatureImportances`**
  - **Purpose**: Explain the internal model structure.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `schemas.FeatureImportances`
* **`explain_samples(self: Any, inputs: schemas.Inputs) -> schemas.SHAPValues`**
  - **Purpose**: Explain model outputs on input samples.
  - **Inputs**:
    - `self` (`Any`)
    - `inputs` (`schemas.Inputs`)
  - **Outputs**: `schemas.SHAPValues`
* **`get_internal_model(self: Any) -> T.Any`**
  - **Purpose**: Return the internal model in the object.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `T.Any`

#### Private Methods
* **`__sklearn_tags__(self: Any) -> T.Any`**
  - **Purpose**: Get the model tags for scikit-learn.

### `BaselineSklearnModel`

Simple baseline model based on scikit-learn.

Parameters:
    max_depth (int): maximum depth of the random forest.
    n_estimators (int): number of estimators in the random forest.
    random_state (int, optional): random state of the machine learning pipeline.

#### Attributes
* **`KIND`** (`T.Literal[BaselineSklearnModel]`)
* **`max_depth`** (`int`)
* **`n_estimators`** (`int`)
* **`random_state`** (`int | None`)
* **`_pipeline`** (`pipeline.Pipeline | None`)
* **`_numericals`** (`list[str]`)
* **`_categoricals`** (`list[str]`)

#### Public Methods
* **`fit(self: Any, inputs: schemas.Inputs, targets: schemas.Targets) -> BaselineSklearnModel`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `inputs` (`schemas.Inputs`)
    - `targets` (`schemas.Targets`)
  - **Outputs**: `BaselineSklearnModel`
* **`predict(self: Any, inputs: T.Any) -> schemas.Outputs`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `inputs` (`T.Any`)
  - **Outputs**: `schemas.Outputs`
* **`explain_model(self: Any) -> schemas.FeatureImportances`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `schemas.FeatureImportances`
* **`explain_samples(self: Any, inputs: schemas.Inputs) -> schemas.SHAPValues`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `inputs` (`schemas.Inputs`)
  - **Outputs**: `schemas.SHAPValues`
* **`get_internal_model(self: Any) -> pipeline.Pipeline`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `pipeline.Pipeline`

## Dependencies

* `abc`
* `typing`
* `pydantic`
* `shap`
* `sklearn.compose`
* `sklearn.ensemble`
* `sklearn.pipeline`
* `sklearn.preprocessing`
* `regression_model_template.core.schemas`

## Used By

* [metrics.py](../../regression_model_template/core/metrics.md)
* [registries.py](../../regression_model_template/io/registries.md)
* [training.py](../../regression_model_template/jobs/training.md)
* [tuning.py](../../regression_model_template/jobs/tuning.md)
* [searchers.py](../../regression_model_template/utils/searchers.md)
