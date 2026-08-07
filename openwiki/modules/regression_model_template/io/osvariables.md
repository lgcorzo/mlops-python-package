---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: osvariables"
source_path: "src/regression_model_template/io/osvariables.py"
description: "No description available."
tags: ["module", "osvariables"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: osvariables

* **Source Reference:** [src/regression_model_template/io/osvariables.py](../../../src/regression_model_template/io/osvariables.py)

## 1. Architectural Role & Responsibilities
No description available.

## 2. UML 2.0 Class Diagram
```plantuml
classDiagram
    direction BT
    class Singleton {
        +_instances: dict~(type, Singleton)~
        +__new__(cls: type~Singleton~, *args: tuple~(Any, Ellipsis)~, **kwargs: dict~(str, Any)~) Singleton
    }
    object <|-- Singleton : Generalization
    class Env {
        +mlflow_tracking_uri: str
        +mlflow_registry_uri: str
        +mlflow_experiment_name: str
        +mlflow_registered_model_name: str
    }
    Singleton <|-- Env : Generalization
    BaseSettings <|-- Env : Generalization
```

## 3. Class & Method Specifications

### `Singleton`

No description available.

#### Attributes
* **`_instances`** (`dict[(type, Singleton)]`)

#### Private Methods
* **`__new__(cls: type[Singleton], *args: tuple[(Any, Ellipsis)], **kwargs: dict[(str, Any)]) -> Singleton`**
  - **Purpose**: No description available.

### `Env`

No description available.

#### Attributes
* **`mlflow_tracking_uri`** (`str`)
* **`mlflow_registry_uri`** (`str`)
* **`mlflow_experiment_name`** (`str`)
* **`mlflow_registered_model_name`** (`str`)

## Dependencies

* `typing.Any`
* `pydantic_settings.BaseSettings`

## Used By

* [services.py](../../regression_model_template/io/services.md)
