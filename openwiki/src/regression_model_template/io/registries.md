---
type: "module-architecture"
title: "registries"
description: "Technical architecture and class hierarchy for registries"
tags: ["architecture", "uml", "pyreverse", "openwiki"]
timestamp: "2026-07-30T19:10:46Z"
---

# Module Name: registries

Source File: `src/regression_model_template/io/registries.py`
* **Source Directory Reference:** `src/regression_model_template/io/`
* **Package Dependency:** Upstream: `pydantic`, `mlflow`, `regression_model_template.utils`, `abc`, `typing`, `regression_model_template.core` | Downstream: None

## 1. Executive Summary & Purpose
Deterministic architectural model extracted via AST parsing for module `registries`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)
The following class diagram models the object-oriented structure, explicit inheritance hierarchies, and polymorphic interface implementations derived from local AST analysis:

```mermaid
classDiagram
    class Saver {
        +KIND
        +path
        +save(model, signature, input_example) : Info
    }
    class CustomSaver {
        +KIND
        +save(model, signature, input_example) : Info
    }
    Saver <|-- CustomSaver
    class CustomSaver.Adapter {
        -__init__(model)
        +predict(context, model_input, params) : Any
    }
    class BuiltinSaver {
        +KIND
        +flavor
        +save(model, signature, input_example) : Info
    }
    Saver <|-- BuiltinSaver
    class Loader {
        +KIND
        +load(uri) : Any
    }
    class Loader.Adapter {
        +predict(inputs) : Any
    }
    class CustomLoader {
        +KIND
        +load(uri) : Any
    }
    Loader <|-- CustomLoader
    class CustomLoader.Adapter {
        -__init__(model) : None
        +predict(inputs) : Any
    }
    class BuiltinLoader {
        +KIND
        +load(uri) : Any
    }
    Loader <|-- BuiltinLoader
    class BuiltinLoader.Adapter {
        -__init__(model) : None
        +predict(inputs) : Any
    }
    class Register {
        +KIND
        +tags
        +register(name, model_uri) : Version
    }
    class MlflowRegister {
        +KIND
        +register(name, model_uri) : Version
    }
    Register <|-- MlflowRegister
```

## 3. Package & Class Relations

The following diagram defines the package boundaries and directional inter-package dependencies:

```mermaid
classDiagram
    class Saver {
        +KIND
        +path
        +save(model, signature, input_example) : Info
    }
    class CustomSaver {
        +KIND
        +save(model, signature, input_example) : Info
    }
    Saver <|-- CustomSaver
    class CustomSaver.Adapter {
        -__init__(model)
        +predict(context, model_input, params) : Any
    }
    class BuiltinSaver {
        +KIND
        +flavor
        +save(model, signature, input_example) : Info
    }
    Saver <|-- BuiltinSaver
    class Loader {
        +KIND
        +load(uri) : Any
    }
    class Loader.Adapter {
        +predict(inputs) : Any
    }
    class CustomLoader {
        +KIND
        +load(uri) : Any
    }
    Loader <|-- CustomLoader
    class CustomLoader.Adapter {
        -__init__(model) : None
        +predict(inputs) : Any
    }
    class BuiltinLoader {
        +KIND
        +load(uri) : Any
    }
    Loader <|-- BuiltinLoader
    class BuiltinLoader.Adapter {
        -__init__(model) : None
        +predict(inputs) : Any
    }
    class Register {
        +KIND
        +tags
        +register(name, model_uri) : Version
    }
    class MlflowRegister {
        +KIND
        +register(name, model_uri) : Version
    }
    Register <|-- MlflowRegister
```

* **Inheritance & Polymorphism:** Detailed breakdown of abstract base classes, interfaces, and concrete overrides.
* **Dependencies:** How classes within this package collaborate externally.

## 4. Execution Flow & Runtime Behavior

The following sequence diagram outlines the execution lifecycle and message passing during core operations:

```mermaid
sequenceDiagram
    autonumber
    participant Caller as Client Interface
    participant Saver as Saver
    Caller->>Saver: save()
    Note over Saver: Execution of save
    Saver-->>Caller: Returns status
    participant CustomSaver as CustomSaver
    Caller->>CustomSaver: save()
    Note over CustomSaver: Execution of save
    CustomSaver->>CustomSaver: internal log_model()
    CustomSaver->>CustomSaver: internal Adapter()
    CustomSaver-->>Caller: Returns status
    participant BuiltinSaver as BuiltinSaver
    Caller->>BuiltinSaver: save()
    Note over BuiltinSaver: Execution of save
    BuiltinSaver->>BuiltinSaver: internal get_internal_model()
    BuiltinSaver->>BuiltinSaver: internal getattr()
    BuiltinSaver-->>Caller: Returns status
    participant Loader as Loader
    Caller->>Loader: load()
    Note over Loader: Execution of load
    Loader-->>Caller: Returns status
    participant CustomLoader as CustomLoader
    Caller->>CustomLoader: load()
    Note over CustomLoader: Execution of load
    CustomLoader->>CustomLoader: internal Adapter()
    CustomLoader->>CustomLoader: internal load_model()
    CustomLoader-->>Caller: Returns status
    participant BuiltinLoader as BuiltinLoader
    Caller->>BuiltinLoader: load()
    Note over BuiltinLoader: Execution of load
    BuiltinLoader->>BuiltinLoader: internal Adapter()
    BuiltinLoader->>BuiltinLoader: internal load_model()
    BuiltinLoader-->>Caller: Returns status
    participant Register as Register
    Caller->>Register: register()
    Note over Register: Execution of register
    Register-->>Caller: Returns status
    participant MlflowRegister as MlflowRegister
    Caller->>MlflowRegister: register()
    Note over MlflowRegister: Execution of register
    MlflowRegister->>MlflowRegister: internal register_model()
    MlflowRegister-->>Caller: Returns status
    participant Adapter as Adapter
    Caller->>Adapter: __init__()
    Note over Adapter: Execution of __init__
    Adapter-->>Caller: Returns status
    participant Adapter as Adapter
    Caller->>Adapter: predict()
    Note over Adapter: Execution of predict
    Adapter-->>Caller: Returns status
    participant Adapter as Adapter
    Caller->>Adapter: __init__()
    Note over Adapter: Execution of __init__
    Adapter-->>Caller: Returns status
    participant Adapter as Adapter
    Caller->>Adapter: __init__()
    Note over Adapter: Execution of __init__
    Adapter-->>Caller: Returns status
```

---

* **Source Citations:**
  - Class `Saver`: `src/regression_model_template/io/registries.py:69`
  - Method `save`: `src/regression_model_template/io/registries.py:84`
  - Class `CustomSaver`: `src/regression_model_template/io/registries.py:97`
  - Method `save`: `src/regression_model_template/io/registries.py:138`
  - Class `BuiltinSaver`: `src/regression_model_template/io/registries.py:148`
  - Method `save`: `src/regression_model_template/io/registries.py:161`
  - Class `Loader`: `src/regression_model_template/io/registries.py:179`
  - Method `load`: `src/regression_model_template/io/registries.py:203`
  - Class `CustomLoader`: `src/regression_model_template/io/registries.py:214`
  - Method `load`: `src/regression_model_template/io/registries.py:238`
  - Class `BuiltinLoader`: `src/regression_model_template/io/registries.py:244`
  - Method `load`: `src/regression_model_template/io/registries.py:270`
  - Class `Register`: `src/regression_model_template/io/registries.py:281`
  - Method `register`: `src/regression_model_template/io/registries.py:296`
  - Class `MlflowRegister`: `src/regression_model_template/io/registries.py:308`
  - Method `register`: `src/regression_model_template/io/registries.py:316`
  - Class `Adapter`: `src/regression_model_template/io/registries.py:105`
  - Method `__init__`: `src/regression_model_template/io/registries.py:111`
  - Method `predict`: `src/regression_model_template/io/registries.py:119`
  - Class `Adapter`: `src/regression_model_template/io/registries.py:188`
  - Method `predict`: `src/regression_model_template/io/registries.py:192`
  - Class `Adapter`: `src/regression_model_template/io/registries.py:222`
  - Method `__init__`: `src/regression_model_template/io/registries.py:225`
  - Method `predict`: `src/regression_model_template/io/registries.py:233`
  - Class `Adapter`: `src/regression_model_template/io/registries.py:254`
  - Method `__init__`: `src/regression_model_template/io/registries.py:257`
  - Method `predict`: `src/regression_model_template/io/registries.py:265`

```mermaid
flowchart TD
    registries --> abc
    registries --> mlflow
    registries --> pydantic
    registries --> regression_model_template_core
    registries --> regression_model_template_utils
    registries --> typing
```
