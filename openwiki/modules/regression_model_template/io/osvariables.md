---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: osvariables"
source_path: "src/regression_model_template/io/osvariables.py"
description: "Documentation for regression_model_template.io.osvariables"
tags: ["module", "osvariables", "regression_model_template"]
timestamp: "2026-08-01T09:57:53Z"
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "8f9670a"
---

# Module Specification: osvariables

* **Source Reference:** [src/regression_model_template/io/osvariables.py](../../../src/regression_model_template/io/osvariables.py) (Lines: L1-L26)

## 1. Architectural Role & Responsibilities
Documentation for regression_model_template.io.osvariables

## 2. UML 2.0 Class Diagram
```mermaid
classDiagram
    direction BT
    class Singleton {
        -_instances: dict[type, 'Singleton']
        -__new__(cls: type['Singleton']) 'Singleton'
    }
    class Env {
        +mlflow_tracking_uri: str
        +mlflow_registry_uri: str
        +mlflow_experiment_name: str
        +mlflow_registered_model_name: str
    }
```

## 3. Class & Method Specifications

### `Singleton` ([`src/regression_model_template/io/osvariables.py:L6-L13`](../../../src/regression_model_template/io/osvariables.py#L6-L13))

No description available.

#### Methods

* **`__new__(cls: type['Singleton']) -> 'Singleton'`** (L10-L13)
  - **Purpose**: No description available.
  - **Inputs**:
    - `cls` (`type['Singleton']`): Parameter description.
  - **Outputs**:
    - `'Singleton'`: Return value description.

### `Env` ([`src/regression_model_template/io/osvariables.py:L16-L26`](../../../src/regression_model_template/io/osvariables.py#L16-L26))

No description available.

#### Methods

*No methods defined.*
