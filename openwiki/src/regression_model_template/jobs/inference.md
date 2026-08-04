---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "inference Documentation"
description: "Documentation for src/regression_model_template/jobs/inference.py"
tags: ["module", "inference"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `src/regression_model_template/jobs/inference.py`

## Overview
**Purpose**: Define a job for generating batch predictions from a registered model.

**Architecture Role**: Domain Models

**Dependencies**:
- `pydantic`
- `regression_model_template.core`
- `typing`
- `regression_model_template.jobs`
- `pandas`
- `regression_model_template.io`

**Exported Symbols**:
- `InferenceJob`

## UML Class Diagram
```plantuml
@startuml
class InferenceJob {
  +KIND : T.Literal['InferenceJob']
  +inputs : datasets.ReaderKind
  +outputs : datasets.WriterKind
  +alias_or_version : str | int
  +loader : registries.LoaderKind
  +run(self:Any) : base.Locals
}
base.Job <|-- InferenceJob
@enduml
```

## Call Graph
```plantuml
@startuml
InferenceJob::run --> logger
InferenceJob::run --> info
InferenceJob::run --> info
InferenceJob::run --> read
InferenceJob::run --> check
InferenceJob::run --> debug
InferenceJob::run --> info
InferenceJob::run --> uri_for_model_alias_or_version
InferenceJob::run --> debug
InferenceJob::run --> info
InferenceJob::run --> load
InferenceJob::run --> debug
InferenceJob::run --> info
InferenceJob::run --> predict
InferenceJob::run --> debug
InferenceJob::run --> info
InferenceJob::run --> write
InferenceJob::run --> notify
InferenceJob::run --> locals
InferenceJob::run --> len
InferenceJob::run --> DataFrame
@enduml
```

## Classes
### Class `InferenceJob`
**Overview**: Generate batch predictions from a registered model.

Parameters:
    inputs (datasets.ReaderKind): reader for the inputs data.
    outputs (datasets.WriterKind): writer for the outputs data.
    alias_or_version (str | int): alias or version for the  model.
    loader (registries.LoaderKind): registry loader for the model.

#### Attributes
- `KIND`: T.Literal['InferenceJob']
- `inputs`: datasets.ReaderKind
- `outputs`: datasets.WriterKind
- `alias_or_version`: str | int
- `loader`: registries.LoaderKind
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
