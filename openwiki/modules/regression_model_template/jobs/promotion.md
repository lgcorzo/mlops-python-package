---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: promotion"
source_path: "src/regression_model_template/jobs/promotion.py"
description: "Define a job for promoting a registered model version with an alias."
tags: ["module", "promotion", "regression_model_template"]
timestamp: "2026-08-01T09:57:53Z"
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "8f9670a"
---

# Module Specification: promotion

* **Source Reference:** [src/regression_model_template/jobs/promotion.py](../../../src/regression_model_template/jobs/promotion.py) (Lines: L1-L57)

## 1. Architectural Role & Responsibilities
Define a job for promoting a registered model version with an alias.

## 2. UML 2.0 Class Diagram
```mermaid
classDiagram
    direction BT
    class PromotionJob {
        +KIND: T.Literal['PromotionJob']
        +alias: str
        +version: int | None
        +run(self: Any) base.Locals
    }
```

## 2b. Execution Flow (Sequence Diagram)
```mermaid
sequenceDiagram
    autonumber
    participant User as Runner
    participant Job as PromotionJob
    
    User->>Job: run()
    activate Job
    Note over Job: Reads inputs and performs workflow steps
    Job-->>User: Locals (dict)
    deactivate Job
```

## 3. Class & Method Specifications

### `PromotionJob` ([`src/regression_model_template/jobs/promotion.py:L12-L57`](../../../src/regression_model_template/jobs/promotion.py#L12-L57))

Define a job for promoting a registered model version with an alias.

https://mlflow.org/docs/latest/model-registry.html#concepts

Parameters:
    alias (str): the mlflow alias to transition the registered model version.
    version (int | None): the model version to transition (use None for latest).

#### Methods

* **`run(self: Any) -> base.Locals`** (L27-L57)
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`): Parameter description.
  - **Outputs**:
    - `base.Locals`: Return value description.
