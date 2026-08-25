---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: models"
source_path: "src/regression_model_template/core/models.py"
description: "Define trainable machine learning models."
tags: ["module", "models"]
timestamp: "2026-08-25T05:40:20Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "74a428a"
---
# Module Specification: models

* **Source Reference:** [src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)

## 1. Architectural Role & Responsibilities

Define trainable machine learning models.

### Detected Architecture Patterns

Detected roles: Entity / Domain Model

## 2. UML Diagrams

### Class Diagram

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

### Sequence Diagram

```plantuml
sequenceDiagram
    Model.get_params->>items: invoke
    Model.get_params->>model_dump: invoke
    Model.get_params->>startswith: invoke
    Model.get_params->>isupper: invoke
    Model.set_params->>items: invoke
    Model.set_params->>setattr: invoke
    Model.__sklearn_tags__->>__sklearn_tags__: invoke
    Model.__sklearn_tags__->>BaseEstimator: invoke
    Model.explain_model->>NotImplementedError: invoke
    Model.explain_samples->>NotImplementedError: invoke
    Model.get_internal_model->>NotImplementedError: invoke
    BaselineSklearnModel.fit->>OneHotEncoder: invoke
    BaselineSklearnModel.fit->>ColumnTransformer: invoke
    BaselineSklearnModel.fit->>RandomForestRegressor: invoke
    BaselineSklearnModel.fit->>Pipeline: invoke
    BaselineSklearnModel.fit->>fit: invoke
    BaselineSklearnModel.predict->>get_internal_model: invoke
    BaselineSklearnModel.predict->>predict: invoke
    BaselineSklearnModel.predict->>Outputs: invoke
    BaselineSklearnModel.explain_model->>get_internal_model: invoke
    BaselineSklearnModel.explain_model->>get_feature_names_out: invoke
    BaselineSklearnModel.explain_model->>FeatureImportances: invoke
    BaselineSklearnModel.explain_samples->>get_internal_model: invoke
    BaselineSklearnModel.explain_samples->>transform: invoke
    BaselineSklearnModel.explain_samples->>TreeExplainer: invoke
    BaselineSklearnModel.explain_samples->>SHAPValues: invoke
    BaselineSklearnModel.explain_samples->>shap_values: invoke
    BaselineSklearnModel.explain_samples->>get_feature_names_out: invoke
    BaselineSklearnModel.get_internal_model->>ValueError: invoke
```

### Component Diagram

```plantuml
component [models] as Comp
Comp --> [abc]
Comp --> [typing]
Comp --> [pydantic]
Comp --> [shap]
Comp --> [compose]
Comp --> [ensemble]
Comp --> [pipeline]
Comp --> [preprocessing]
Comp --> [schemas]
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

* [conftest.py](../../tests/conftest.md)

* [test_metrics.py](../../tests/core/test_metrics.md)

* [test_models.py](../../tests/core/test_models.md)

* [test_schemas.py](../../tests/core/test_schemas.md)

* [test_registries.py](../../tests/io/test_registries.md)

* [test_explanations.py](../../tests/jobs/test_explanations.md)

* [test_training.py](../../tests/jobs/test_training.md)

* [test_tuning.py](../../tests/jobs/test_tuning.md)

* [test_searchers.py](../../tests/utils/test_searchers.md)
