---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: promotion"
source_path: "src/regression_model_template/jobs/promotion.py"
description: "Define a job for promoting a registered model version with an alias."
tags: ["module", "promotion"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: promotion

* **Source Reference:** [src/regression_model_template/jobs/promotion.py](../../../src/regression_model_template/jobs/promotion.py)

## 1. Architectural Role & Responsibilities
Define a job for promoting a registered model version with an alias.

## 2. UML 2.0 Class Diagram
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
