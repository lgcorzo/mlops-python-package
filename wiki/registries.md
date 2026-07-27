---
type: script
title: "registries"
source_path: "src/regression_model_template/io/registries.py"
description: "Savers, loaders, and registers for model registries."
tags: [script, regression_model_template]
last_verified_commit: "c0c5dbc"
---

# registries

Source File: `src/regression_model_template/io/registries.py`

Savers, loaders, and registers for model registries.

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

```mermaid
flowchart TD

    registries --> abc
    registries --> mlflow
    registries --> pydantic
    registries --> regression_model_template_core
    registries --> regression_model_template_utils
    registries --> typing
```
