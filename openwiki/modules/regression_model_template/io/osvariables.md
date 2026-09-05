---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: osvariables"
source_path: "src/regression_model_template/io/osvariables.py"
description: "No description available."
tags: ["module", "osvariables"]
timestamp: "2026-09-05T11:29:30Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: osvariables

* **Source Reference:** [src/regression_model_template/io/osvariables.py](../../../../src/regression_model_template/io/osvariables.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `typing.Any`

* `pydantic_settings.BaseSettings`

# Each File Documentation

## Imported modules

* `typing.Any`

* `pydantic_settings.BaseSettings`

## Exported classes

* `Singleton`

* `Env`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

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

### Sequence Diagram

```plantuml
sequenceDiagram
    Singleton.__new__->>__new__: invoke
    Singleton.__new__->>super: invoke
```

### Component Diagram

```plantuml
component [osvariables] as Comp
Comp --> [Any]
Comp --> [BaseSettings]
```

## 3. Class & Method Specifications

# Public Classes

### `Singleton`

## Overview

No description available.

## Attributes

* **`_instances`**

  - **Type**: dict[(type, Singleton)]

# Private Methods

* **`__new__(cls: type[Singleton], *args: tuple[(Any, Ellipsis)], **kwargs: dict[(str, Any)]) -> Singleton`**

### Purpose

No description available.

### Parameters

* `cls` (`type[Singleton]`)

* `*args` (`tuple[(Any, Ellipsis)]`)

* `**kwargs` (`dict[(str, Any)]`)

### Return value

* `Singleton`

### `Env`

## Overview

No description available.

## Attributes

* **`mlflow_tracking_uri`**

  - **Type**: str

* **`mlflow_registry_uri`**

  - **Type**: str

* **`mlflow_experiment_name`**

  - **Type**: str

* **`mlflow_registered_model_name`**

  - **Type**: str

## Used By

* [services.py](../../regression_model_template/io/services.md)
