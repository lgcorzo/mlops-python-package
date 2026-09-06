---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: models"
source_path: "src/regression_model_template/core/models.py"
description: "Define trainable machine learning models."
tags: ["module", "models"]
timestamp: "2026-09-06T06:26:18Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: models

* **Source Reference:** [src/regression_model_template/core/models.py](../../../../src/regression_model_template/core/models.py)

# Module Overview

## Purpose

Define trainable machine learning models.

## Responsibilities

Define trainable machine learning models.

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

# Each File Documentation

## Imported modules

* `abc`

* `typing`

* `pydantic`

* `shap`

* `sklearn.compose`

* `sklearn.ensemble`

* `sklearn.pipeline`

* `sklearn.preprocessing`

* `regression_model_template.core.schemas`

## Exported classes

* `Model`

* `BaselineSklearnModel`

## Exported interfaces

_Dependent on implementation_

## Public API

_Dependent on implementation_

## Internal architecture

_Dependent on implementation_

## Execution flow

_Dependent on implementation_

## Sequence explanation

_Dependent on implementation_

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

## Examples

_Dependent on implementation_

## 3. Class & Method Specifications

# Public Classes

### `Model`

## Overview

Base class for a project model.

Use a model to adapt AI/ML frameworks.
e.g., to swap easily one model with another.

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`get_params(self: Any, deep: bool) -> Params`**

### Description

Get the model params.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `deep`

  - **type**: bool

  - **meaning**: ignored.

  - **valid values**: _Dependent on implementation_

  - **optional?**: Yes

  - **default value**: True

### Output

* **return type**: Params

* **semantic meaning**: Params: internal model parameters.

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

* **`set_params(self: Any, **params: ParamValue) -> T.Self`**

### Description

Set the model params in place.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `**params`

  - **type**: ParamValue

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: T.Self

* **semantic meaning**: T.Self: instance of the model.

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

* **`fit(self: Any, inputs: schemas.Inputs, targets: schemas.Targets) -> T.Self`**

### Description

Fit the model on the given inputs and targets.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: model training inputs.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: model training targets.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: T.Self

* **semantic meaning**: T.Self: instance of the model.

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

* **`predict(self: Any, inputs: T.Any) -> schemas.Outputs`**

### Description

Generate outputs with the model for the given inputs.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: T.Any

  - **meaning**: model prediction inputs.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: schemas.Outputs

* **semantic meaning**: schemas.Outputs: model prediction outputs.

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

* **`explain_model(self: Any) -> schemas.FeatureImportances`**

### Description

Explain the internal model structure.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: schemas.FeatureImportances

* **semantic meaning**: schemas.FeatureImportances: feature importances.

* **possible null values**: _Dependent on implementation_

* **exceptions**: NotImplementedError: method not implemented.

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

* **`explain_samples(self: Any, inputs: schemas.Inputs) -> schemas.SHAPValues`**

### Description

Explain model outputs on input samples.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: schemas.SHAPValues

* **semantic meaning**: schemas.SHAPValues: SHAP values.

* **possible null values**: _Dependent on implementation_

* **exceptions**: NotImplementedError: method not implemented.

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

* **`get_internal_model(self: Any) -> T.Any`**

### Description

Return the internal model in the object.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: T.Any

* **semantic meaning**: T.Any: any internal model (either empty or fitted).

* **possible null values**: _Dependent on implementation_

* **exceptions**: NotImplementedError: method not implemented.

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

# Private Methods

* **`__sklearn_tags__(self: Any) -> T.Any`**

### Purpose

Get the model tags for scikit-learn.

### Parameters

* `self` (`Any`)

### Return value

* `T.Any`

### `BaselineSklearnModel`

## Overview

Simple baseline model based on scikit-learn.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[BaselineSklearnModel]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`max_depth`**

  - **Type**: int

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`n_estimators`**

  - **Type**: int

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`random_state`**

  - **Type**: int | None

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`_pipeline`**

  - **Type**: pipeline.Pipeline | None

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`_numericals`**

  - **Type**: list[str]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`_categoricals`**

  - **Type**: list[str]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`fit(self: Any, inputs: schemas.Inputs, targets: schemas.Targets) -> BaselineSklearnModel`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: BaselineSklearnModel

* **semantic meaning**: _Dependent on implementation_

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

* **`predict(self: Any, inputs: T.Any) -> schemas.Outputs`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: T.Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: schemas.Outputs

* **semantic meaning**: _Dependent on implementation_

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

* **`explain_model(self: Any) -> schemas.FeatureImportances`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: schemas.FeatureImportances

* **semantic meaning**: _Dependent on implementation_

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

* **`explain_samples(self: Any, inputs: schemas.Inputs) -> schemas.SHAPValues`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: schemas.SHAPValues

* **semantic meaning**: _Dependent on implementation_

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

* **`get_internal_model(self: Any) -> pipeline.Pipeline`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: pipeline.Pipeline

* **semantic meaning**: _Dependent on implementation_

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

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
