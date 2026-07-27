---
type: script
title: "osvariables"
source_path: "src/regression_model_template/io/osvariables.py"
description: "Documentation for regression_model_template.io.osvariables"
tags: [script, regression_model_template]
last_verified_commit: "c0c5dbc"
---

# osvariables

Source File: `src/regression_model_template/io/osvariables.py`

Documentation for regression_model_template.io.osvariables

```mermaid
classDiagram
    class Singleton {
        #_instances
        -__new__(cls) : Any
    }
    object <|-- Singleton
    class Env {
        +mlflow_tracking_uri
        +mlflow_registry_uri
        +mlflow_experiment_name
        +mlflow_registered_model_name
    }
    Singleton <|-- Env
    BaseSettings <|-- Env
    class Env.Config {
        +case_sensitive
        +env_file
        +env_file_encoding
        +extra
    }
```

```mermaid
flowchart TD

    osvariables --> pydantic_settings
    osvariables --> typing
```
