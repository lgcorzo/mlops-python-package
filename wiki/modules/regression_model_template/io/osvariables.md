---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::io::osvariables — Environment Settings Singleton"
source_path: "src/regression_model_template/io/osvariables.py"
description: "Thread-safe Singleton environment configuration parsing dotenv variables into Pydantic BaseSettings."
tags: ["iso42010", "okf", "component_view", "environment", "singleton"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::io::osvariables — Environment Settings Singleton

> **Source**: `src/regression_model_template/io/osvariables.py` (Lines: L1-L26)  
> **Layer**: Infrastructure / Configuration  
> **Role**: Thread-safe Singleton environment manager providing centralized access to MLflow endpoints and platform variables.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Singleton {
        -_instances: dict
        +__new__(cls, *args, **kwargs) Singleton$
    }

    class Env {
        +str mlflow_tracking_uri
        +str mlflow_registry_uri
        +str mlflow_experiment_name
        +str mlflow_registered_model_name
    }
    Env --|> Singleton : inherits
```

---

> *Related: [Services](services.md) · [Configs](configs.md)*
