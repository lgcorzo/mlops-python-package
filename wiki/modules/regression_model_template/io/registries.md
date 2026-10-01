---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::io::registries — Model Registry & Loaders"
source_path: "src/regression_model_template/io/registries.py"
description: "Abstract Loader/Register interfaces and MLflow model registry integration."
tags: ["iso42010", "okf", "component_view", "registry", "mlflow"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::io::registries — Model Registry & Loaders

> **Source**: `src/regression_model_template/io/registries.py` (Lines: L1-L317)  
> **Layer**: Infrastructure  
> **Role**: Interfaces for registering trained model artifacts in MLflow and resolving model versions or aliases into callable prediction adapters.

---

## 1. Class Diagram

```mermaid
classDiagram
    class Loader {
        <<abstract>>
        +str KIND
        +load(uri: str) Loader.Adapter*
    }
    class CustomLoader {
        +load(uri: str) CustomLoader.Adapter
    }
    class BuiltinLoader {
        +load(uri: str) BuiltinLoader.Adapter
    }
    CustomLoader --|> Loader : implements
    BuiltinLoader --|> Loader : implements

    class Register {
        <<abstract>>
        +str KIND
        +dict tags
        +register(name: str, model_uri: str) Version*
    }
    class MlflowRegister {
        +register(name: str, model_uri: str) Version
    }
    MlflowRegister --|> Register : implements
```

---

> *Related: [Services](services.md) · [Promotion Job](../jobs/promotion.md)*
