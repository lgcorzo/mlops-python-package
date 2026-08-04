---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "promotion Documentation"
description: "Documentation for src/regression_model_template/jobs/promotion.py"
tags: ["module", "promotion"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `src/regression_model_template/jobs/promotion.py`

## Overview
**Purpose**: Define a job for promoting a registered model version with an alias.

**Architecture Role**: Domain Models

**Dependencies**:
- `typing`
- `regression_model_template.jobs`

**Exported Symbols**:
- `PromotionJob`

## UML Class Diagram
```plantuml
@startuml
class PromotionJob {
  +KIND : T.Literal['PromotionJob']
  +alias : str
  +version : int | None
  +run(self:Any) : base.Locals
}
base.Job <|-- PromotionJob
@enduml
```

## Call Graph
```plantuml
@startuml
PromotionJob::run --> logger
PromotionJob::run --> info
PromotionJob::run --> client
PromotionJob::run --> info
PromotionJob::run --> info
PromotionJob::run --> info
PromotionJob::run --> info
PromotionJob::run --> set_registered_model_alias
PromotionJob::run --> get_model_version_by_alias
PromotionJob::run --> debug
PromotionJob::run --> notify
PromotionJob::run --> locals
PromotionJob::run --> str
PromotionJob::run --> search_model_versions
@enduml
```

## Classes
### Class `PromotionJob`
**Overview**: Define a job for promoting a registered model version with an alias.

https://mlflow.org/docs/latest/model-registry.html#concepts

Parameters:
    alias (str): the mlflow alias to transition the registered model version.
    version (int | None): the model version to transition (use None for latest).

#### Attributes
- `KIND`: T.Literal['PromotionJob']
- `alias`: str
- `version`: int | None
#### Public Methods
##### `run`
- **Description**: No description available.
- **Inputs**:
  - `self`: Any
- **Output**: `base.Locals`
- **Side Effects**: Not documented
- **Complexity**: Not documented

#### Private Methods
## Functions
