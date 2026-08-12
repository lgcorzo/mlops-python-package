---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: registries"
source_path: "src/regression_model_template/io/registries.py"
description: "Savers, loaders, and registers for model registries."
tags: ["module", "registries"]
timestamp: "2026-08-12T05:53:45Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: registries

* **Source Reference:** [src/regression_model_template/io/registries.py](../../../../src/regression_model_template/io/registries.py)

## 1. Architectural Role & Responsibilities
Savers, loaders, and registers for model registries.

### Detected Architecture Patterns
Detected roles: General Subsystem

## 2. UML Diagrams
### Class Diagram
```plantuml
classDiagram
    direction BT
    class Saver {
        +KIND: str
        +path: str
        +save(self: Any, model: models.Model, signature: signers.Signature, input_example: schemas.Inputs) Info
    }
    ABC <|-- Saver : Generalization
    BaseModel <|-- Saver : Generalization
    class CustomSaver {
        +KIND: T.Literal~CustomSaver~
        +save(self: Any, model: models.Model, signature: signers.Signature, input_example: schemas.Inputs) Info
    }
    Saver <|-- CustomSaver : Generalization
    class BuiltinSaver {
        +KIND: T.Literal~BuiltinSaver~
        +flavor: str
        +save(self: Any, model: models.Model, signature: signers.Signature, input_example: schemas.Inputs | None) Info
    }
    Saver <|-- BuiltinSaver : Generalization
    class Loader {
        +KIND: str
        +load(self: Any, uri: str) Loader.Adapter
    }
    ABC <|-- Loader : Generalization
    BaseModel <|-- Loader : Generalization
    class CustomLoader {
        +KIND: T.Literal~CustomLoader~
        +load(self: Any, uri: str) CustomLoader.Adapter
    }
    Loader <|-- CustomLoader : Generalization
    class BuiltinLoader {
        +KIND: T.Literal~BuiltinLoader~
        +load(self: Any, uri: str) BuiltinLoader.Adapter
    }
    Loader <|-- BuiltinLoader : Generalization
    class Register {
        +KIND: str
        +tags: dict~(str, T.Any)~
        +register(self: Any, name: str, model_uri: str) Version
    }
    ABC <|-- Register : Generalization
    BaseModel <|-- Register : Generalization
    class MlflowRegister {
        +KIND: T.Literal~MlflowRegister~
        +register(self: Any, name: str, model_uri: str) Version
    }
    Register <|-- MlflowRegister : Generalization
```

### Sequence Diagram
```plantuml
sequenceDiagram
    CustomSaver.save->>Adapter: invoke
    CustomSaver.save->>log_model: invoke
    BuiltinSaver.save->>get_internal_model: invoke
    BuiltinSaver.save->>getattr: invoke
    BuiltinSaver.save->>log_model: invoke
    CustomLoader.load->>load_model: invoke
    CustomLoader.load->>Adapter: invoke
    BuiltinLoader.load->>load_model: invoke
    BuiltinLoader.load->>Adapter: invoke
    MlflowRegister.register->>register_model: invoke
    uri_for_model_alias_or_version->>isinstance: invoke
    uri_for_model_alias_or_version->>uri_for_model_version: invoke
    uri_for_model_alias_or_version->>uri_for_model_alias: invoke
```

### Component Diagram
```plantuml
component [registries] as Comp
Comp --> [abc]
Comp --> [typing]
Comp --> [mlflow]
Comp --> [pydantic]
Comp --> [models]
Comp --> [schemas]
Comp --> [signers]
```

## 3. Class & Method Specifications

### `Saver`

Base class for saving models in registry.

Separate model definition from serialization.
e.g., to switch between serialization flavors.

Parameters:
    path (str): model path inside the Mlflow store.

#### Attributes
* **`KIND`** (`str`)
* **`path`** (`str`)

#### Public Methods
* **`save(self: Any, model: models.Model, signature: signers.Signature, input_example: schemas.Inputs) -> Info`**
  - **Purpose**: Save a model in the model registry.
  - **Inputs**:
    - `self` (`Any`)
    - `model` (`models.Model`)
    - `signature` (`signers.Signature`)
    - `input_example` (`schemas.Inputs`)
  - **Outputs**: `Info`

### `CustomSaver`

Saver for project models using the Mlflow PyFunc module.

https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html

#### Attributes
* **`KIND`** (`T.Literal[CustomSaver]`)

#### Public Methods
* **`save(self: Any, model: models.Model, signature: signers.Signature, input_example: schemas.Inputs) -> Info`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `model` (`models.Model`)
    - `signature` (`signers.Signature`)
    - `input_example` (`schemas.Inputs`)
  - **Outputs**: `Info`

### `BuiltinSaver`

Saver for built-in models using an Mlflow flavor module.

https://mlflow.org/docs/latest/models.html#built-in-model-flavors

Parameters:
    flavor (str): Mlflow flavor module to use for the serialization.

#### Attributes
* **`KIND`** (`T.Literal[BuiltinSaver]`)
* **`flavor`** (`str`)

#### Public Methods
* **`save(self: Any, model: models.Model, signature: signers.Signature, input_example: schemas.Inputs | None) -> Info`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `model` (`models.Model`)
    - `signature` (`signers.Signature`)
    - `input_example` (`schemas.Inputs | None`)
  - **Outputs**: `Info`

### `Loader`

Base class for loading models from registry.

Separate model definition from deserialization.
e.g., to switch between deserialization flavors.

#### Attributes
* **`KIND`** (`str`)

#### Public Methods
* **`load(self: Any, uri: str) -> Loader.Adapter`**
  - **Purpose**: Load a model from the model registry.
  - **Inputs**:
    - `self` (`Any`)
    - `uri` (`str`)
  - **Outputs**: `Loader.Adapter`

### `CustomLoader`

Loader for custom models using the Mlflow PyFunc module.

https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html

#### Attributes
* **`KIND`** (`T.Literal[CustomLoader]`)

#### Public Methods
* **`load(self: Any, uri: str) -> CustomLoader.Adapter`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `uri` (`str`)
  - **Outputs**: `CustomLoader.Adapter`

### `BuiltinLoader`

Loader for built-in models using the Mlflow PyFunc module.

Note: use Mlflow PyFunc instead of flavors to use standard API.

https://mlflow.org/docs/latest/models.html#built-in-model-flavors

#### Attributes
* **`KIND`** (`T.Literal[BuiltinLoader]`)

#### Public Methods
* **`load(self: Any, uri: str) -> BuiltinLoader.Adapter`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `uri` (`str`)
  - **Outputs**: `BuiltinLoader.Adapter`

### `Register`

Base class for registring models to a location.

Separate model definition from its registration.
e.g., to change the model registry backend.

Parameters:
    tags (dict[str, T.Any]): tags for the model.

#### Attributes
* **`KIND`** (`str`)
* **`tags`** (`dict[(str, T.Any)]`)

#### Public Methods
* **`register(self: Any, name: str, model_uri: str) -> Version`**
  - **Purpose**: Register a model given its name and URI.
  - **Inputs**:
    - `self` (`Any`)
    - `name` (`str`)
    - `model_uri` (`str`)
  - **Outputs**: `Version`

### `MlflowRegister`

Register for models in the Mlflow Model Registry.

https://mlflow.org/docs/latest/model-registry.html

#### Attributes
* **`KIND`** (`T.Literal[MlflowRegister]`)

#### Public Methods
* **`register(self: Any, name: str, model_uri: str) -> Version`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `name` (`str`)
    - `model_uri` (`str`)
  - **Outputs**: `Version`

## Standalone Functions

### `uri_for_model_alias(name: str, alias: str) -> str`
Create a model URI from a model name and an alias.

Args:
    name (str): name of the mlflow registered model.
    alias (str): alias of the registered model.

Returns:
    str: model URI as "models:/name@alias".

#### Inputs
* `name` (`str`)
* `alias` (`str`)

#### Outputs
* `str`

### `uri_for_model_version(name: str, version: int) -> str`
Create a model URI from a model name and a version.

Args:
    name (str): name of the mlflow registered model.
    version (int): version of the registered model.

Returns:
    str: model URI as "models:/name/version."

#### Inputs
* `name` (`str`)
* `version` (`int`)

#### Outputs
* `str`

### `uri_for_model_alias_or_version(name: str, alias_or_version: str | int) -> str`
Create a model URi from a model name and an alias or version.

Args:
    name (str): name of the mlflow registered model.
    alias_or_version (str | int): alias or version of the registered model.

Returns:
    str: model URI as "models:/name@alias" or "models:/name/version" based on input.

#### Inputs
* `name` (`str`)
* `alias_or_version` (`str | int`)

#### Outputs
* `str`

## Dependencies

* `abc`
* `typing`
* `mlflow`
* `pydantic`
* `regression_model_template.core.models`
* `regression_model_template.core.schemas`
* `regression_model_template.utils.signers`

## Used By

* [kafka_app.py](../../regression_model_template/controller/kafka_app.md)
* [evaluations.py](../../regression_model_template/jobs/evaluations.md)
* [explanations.py](../../regression_model_template/jobs/explanations.md)
* [inference.py](../../regression_model_template/jobs/inference.md)
* [training.py](../../regression_model_template/jobs/training.md)
* [conftest.py](../../tests/conftest.md)
* [test_registries.py](../../tests/io/test_registries.md)
* [test_evaluations.py](../../tests/jobs/test_evaluations.md)
* [test_explanations.py](../../tests/jobs/test_explanations.md)
* [test_inference.py](../../tests/jobs/test_inference.md)
* [test_promotion.py](../../tests/jobs/test_promotion.md)
* [test_training.py](../../tests/jobs/test_training.md)
