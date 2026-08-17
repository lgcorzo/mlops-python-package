---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: promotion"
source_path: "src/regression_model_template/jobs/promotion.py"
description: "Define a job for promoting a registered model version with an alias."
tags: ["module", "promotion"]
timestamp: "2026-08-17T05:34:56Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "73b4d7b"
---
# Module Specification: promotion

* **Source Reference:** [src/regression_model_template/jobs/promotion.py](../../../../src/regression_model_template/jobs/promotion.py)

## 1. Architectural Role & Responsibilities

Define a job for promoting a registered model version with an alias.

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

```plantuml
classDiagram
    direction BT
    class PromotionJob {
        +KIND: T.Literal~PromotionJob~
        +alias: str
        +version: int | None
        +run(self: Any) base.Locals
    }
    Job <|-- PromotionJob : Generalization
```


### Sequence Diagram

```plantuml
sequenceDiagram
    PromotionJob.run->>logger: invoke
    PromotionJob.run->>info: invoke
    PromotionJob.run->>client: invoke
    PromotionJob.run->>set_registered_model_alias: invoke
    PromotionJob.run->>get_model_version_by_alias: invoke
    PromotionJob.run->>debug: invoke
    PromotionJob.run->>notify: invoke
    PromotionJob.run->>locals: invoke
    PromotionJob.run->>str: invoke
    PromotionJob.run->>search_model_versions: invoke
```

### Component Diagram

```plantuml
component [promotion] as Comp
Comp --> [typing]
Comp --> [base]
```


## 3. Class & Method Specifications

### `PromotionJob`


Define a job for promoting a registered model version with an alias.

https://mlflow.org/docs/latest/model-registry.html#concepts

Parameters:
    alias (str): the mlflow alias to transition the registered model version.
    version (int | None): the model version to transition (use None for latest).

#### Attributes

* **`KIND`** (`T.Literal[PromotionJob]`)

* **`alias`** (`str`)

* **`version`** (`int | None`)

#### Public Methods

* **`run(self: Any) -> base.Locals`**

  - **Purpose**: No description available.

  - **Inputs**:

    - `self` (`Any`)

  - **Outputs**: `base.Locals`

## Dependencies

* `typing`

* `regression_model_template.jobs.base`


## Used By

* [__init__.py](../../regression_model_template/jobs/__init__.md)
