---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: registries"
source_path: "src/regression_model_template/io/registries.py"
description: "Savers, loaders, and registers for model registries."
tags: ["module", "registries"]
timestamp: "2026-09-05T05:14:18Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: registries

* **Source Reference:** [src/regression_model_template/io/registries.py](../../../../src/regression_model_template/io/registries.py)

# Module Overview

## Purpose

Savers, loaders, and registers for model registries.

## Responsibilities

Savers, loaders, and registers for model registries.

## Dependencies

* `abc`

* `typing`

* `mlflow`

* `pydantic`

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

* `regression_model_template.utils.signers`

# Each File Documentation

## Imported modules

* `abc`

* `typing`

* `mlflow`

* `pydantic`

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

* `regression_model_template.utils.signers`

## Exported classes

* `Saver`

* `CustomSaver`

* `BuiltinSaver`

* `Loader`

* `CustomLoader`

* `BuiltinLoader`

* `Register`

* `MlflowRegister`

## Exported functions

* `uri_for_model_alias`

* `uri_for_model_version`

* `uri_for_model_alias_or_version`

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

# Public Classes

### `Saver`

## Overview

Base class for saving models in registry.

Separate model definition from serialization.
e.g., to switch between serialization flavors.

Parameters:
    path (str): model path inside the Mlflow store.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`path`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `save(self: Any, model: models.Model, signature: signers.Signature, input_example: schemas.Inputs) -> Info`

### Description

Save a model in the model registry.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `model`

  - **type**: models.Model

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `signature`

  - **type**: signers.Signature

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `input_example`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: Info

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for save

```

### `CustomSaver`

## Overview

Saver for project models using the Mlflow PyFunc module.

https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[CustomSaver]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `save(self: Any, model: models.Model, signature: signers.Signature, input_example: schemas.Inputs) -> Info`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `model`

  - **type**: models.Model

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `signature`

  - **type**: signers.Signature

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `input_example`

  - **type**: schemas.Inputs

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: Info

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for save

```

### `BuiltinSaver`

## Overview

Saver for built-in models using an Mlflow flavor module.

https://mlflow.org/docs/latest/models.html#built-in-model-flavors

Parameters:
    flavor (str): Mlflow flavor module to use for the serialization.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[BuiltinSaver]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`flavor`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `save(self: Any, model: models.Model, signature: signers.Signature, input_example: schemas.Inputs | None) -> Info`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `model`

  - **type**: models.Model

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `signature`

  - **type**: signers.Signature

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `input_example`

  - **type**: schemas.Inputs | None

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: Info

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for save

```

### `Loader`

## Overview

Base class for loading models from registry.

Separate model definition from deserialization.
e.g., to switch between deserialization flavors.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `load(self: Any, uri: str) -> Loader.Adapter`

### Description

Load a model from the model registry.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `uri`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: Loader.Adapter

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for load

```

### `CustomLoader`

## Overview

Loader for custom models using the Mlflow PyFunc module.

https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[CustomLoader]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `load(self: Any, uri: str) -> CustomLoader.Adapter`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `uri`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: CustomLoader.Adapter

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for load

```

### `BuiltinLoader`

## Overview

Loader for built-in models using the Mlflow PyFunc module.

Note: use Mlflow PyFunc instead of flavors to use standard API.

https://mlflow.org/docs/latest/models.html#built-in-model-flavors

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[BuiltinLoader]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `load(self: Any, uri: str) -> BuiltinLoader.Adapter`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `uri`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: BuiltinLoader.Adapter

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for load

```

### `Register`

## Overview

Base class for registring models to a location.

Separate model definition from its registration.
e.g., to change the model registry backend.

Parameters:
    tags (dict[str, T.Any]): tags for the model.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`tags`**

  - **Type**: dict[(str, T.Any)]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `register(self: Any, name: str, model_uri: str) -> Version`

### Description

Register a model given its name and URI.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `name`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `model_uri`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: Version

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for register

```

### `MlflowRegister`

## Overview

Register for models in the Mlflow Model Registry.

https://mlflow.org/docs/latest/model-registry.html

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[MlflowRegister]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `register(self: Any, name: str, model_uri: str) -> Version`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `name`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `model_uri`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: Version

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for register

```

## Standalone Functions

### `uri_for_model_alias(name: str, alias: str) -> str`

### Description

Create a model URI from a model name and an alias.

Args:
    name (str): name of the mlflow registered model.
    alias (str): alias of the registered model.

Returns:
    str: model URI as "models:/name@alias".

### Inputs

* `name`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `alias`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for uri_for_model_alias

```

### `uri_for_model_version(name: str, version: int) -> str`

### Description

Create a model URI from a model name and a version.

Args:
    name (str): name of the mlflow registered model.
    version (int): version of the registered model.

Returns:
    str: model URI as "models:/name/version."

### Inputs

* `name`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `version`

  - **type**: int

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for uri_for_model_version

```

### `uri_for_model_alias_or_version(name: str, alias_or_version: str | int) -> str`

### Description

Create a model URi from a model name and an alias or version.

Args:
    name (str): name of the mlflow registered model.
    alias_or_version (str | int): alias or version of the registered model.

Returns:
    str: model URI as "models:/name@alias" or "models:/name/version" based on input.

### Inputs

* `name`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `alias_or_version`

  - **type**: str | int

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: str

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for uri_for_model_alias_or_version

```

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
