---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: models"
source_path: "src/regression_model_template/core/models.py"
description: "Define trainable machine learning models."
tags: ["module", "models"]
timestamp: "2026-09-05T05:14:18Z"
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

_No interfaces found._

## Public API

_See exported classes and functions._

## Internal architecture

_See architectural detected patterns and UML._

## Execution flow

_Execution flow depends on public API usage._

## Sequence explanation

_See sequence diagram._

## UML

_See diagrams below._

## Examples

_No module level examples available._

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

# Public Classes

### `Model`

## Overview

Base class for a project model.

Use a model to adapt AI/ML frameworks.
e.g., to swap easily one model with another.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `get_params(self: Any, deep: bool) -> Params`

### Description

Get the model params.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `deep`

  - **type**: bool

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: True

### Output

* **return type**: Params

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for get_params

```

### `set_params(self: Any, **params: ParamValue) -> T.Self`

### Description

Set the model params in place.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `**params`

  - **type**: ParamValue

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: T.Self

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for set_params

```

### `fit(self: Any, inputs: schemas.Inputs, targets: schemas.Targets) -> T.Self`

### Description

Fit the model on the given inputs and targets.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: T.Self

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for fit

```

### `predict(self: Any, inputs: T.Any) -> schemas.Outputs`

### Description

Generate outputs with the model for the given inputs.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: T.Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: schemas.Outputs

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for predict

```

### `explain_model(self: Any) -> schemas.FeatureImportances`

### Description

Explain the internal model structure.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: schemas.FeatureImportances

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for explain_model

```

### `explain_samples(self: Any, inputs: schemas.Inputs) -> schemas.SHAPValues`

### Description

Explain model outputs on input samples.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: schemas.SHAPValues

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for explain_samples

```

### `get_internal_model(self: Any) -> T.Any`

### Description

Return the internal model in the object.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: T.Any

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for get_internal_model

```

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

Parameters:
    max_depth (int): maximum depth of the random forest.
    n_estimators (int): number of estimators in the random forest.
    random_state (int, optional): random state of the machine learning pipeline.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[BaselineSklearnModel]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`max_depth`**

  - **Type**: int

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`n_estimators`**

  - **Type**: int

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`random_state`**

  - **Type**: int | None

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`_pipeline`**

  - **Type**: pipeline.Pipeline | None

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`_numericals`**

  - **Type**: list[str]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`_categoricals`**

  - **Type**: list[str]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `fit(self: Any, inputs: schemas.Inputs, targets: schemas.Targets) -> BaselineSklearnModel`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets`

  - **type**: schemas.Targets

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: BaselineSklearnModel

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for fit

```

### `predict(self: Any, inputs: T.Any) -> schemas.Outputs`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: T.Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: schemas.Outputs

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for predict

```

### `explain_model(self: Any) -> schemas.FeatureImportances`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: schemas.FeatureImportances

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for explain_model

```

### `explain_samples(self: Any, inputs: schemas.Inputs) -> schemas.SHAPValues`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: schemas.SHAPValues

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for explain_samples

```

### `get_internal_model(self: Any) -> pipeline.Pipeline`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: pipeline.Pipeline

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for get_internal_model

```

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
