---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: inference"
source_path: "src/regression_model_template/jobs/inference.py"
description: "Define a job for generating batch predictions from a registered model."
tags: ["module", "inference"]
timestamp: "2026-09-05T11:29:30Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: inference

* **Source Reference:** [src/regression_model_template/jobs/inference.py](../../../../src/regression_model_template/jobs/inference.py)

# Module Overview

## Purpose

Define a job for generating batch predictions from a registered model.

## Responsibilities

Define a job for generating batch predictions from a registered model.

## Dependencies

* `typing`

* `pandas`

* `pydantic`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

* `regression_model_template.io.registries`

* `regression_model_template.jobs.base`

# Each File Documentation

## Imported modules

* `typing`

* `pandas`

* `pydantic`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

* `regression_model_template.io.registries`

* `regression_model_template.jobs.base`

## Exported classes

* `InferenceJob`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

```plantuml
classDiagram
    direction BT
    class InferenceJob {
        +KIND: T.Literal~InferenceJob~
        +inputs: datasets.ReaderKind
        +outputs: datasets.WriterKind
        +alias_or_version: str | int
        +loader: registries.LoaderKind
        +run(self: Any) base.Locals
    }
    Job <|-- InferenceJob : Generalization
```

### Sequence Diagram

```plantuml
sequenceDiagram
    InferenceJob.run->>logger: invoke
    InferenceJob.run->>info: invoke
    InferenceJob.run->>read: invoke
    InferenceJob.run->>check: invoke
    InferenceJob.run->>debug: invoke
    InferenceJob.run->>uri_for_model_alias_or_version: invoke
    InferenceJob.run->>load: invoke
    InferenceJob.run->>predict: invoke
    InferenceJob.run->>write: invoke
    InferenceJob.run->>notify: invoke
    InferenceJob.run->>locals: invoke
    InferenceJob.run->>len: invoke
    InferenceJob.run->>DataFrame: invoke
```

### Component Diagram

```plantuml
component [inference] as Comp
Comp --> [typing]
Comp --> [pandas]
Comp --> [pydantic]
Comp --> [schemas]
Comp --> [datasets]
Comp --> [registries]
Comp --> [base]
```

## 3. Class & Method Specifications

# Public Classes

### `InferenceJob`

## Overview

Generate batch predictions from a registered model.

Parameters:
    inputs (datasets.ReaderKind): reader for the inputs data.
    outputs (datasets.WriterKind): writer for the outputs data.
    alias_or_version (str | int): alias or version for the  model.
    loader (registries.LoaderKind): registry loader for the model.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[InferenceJob]

* **`inputs`**

  - **Type**: datasets.ReaderKind

* **`outputs`**

  - **Type**: datasets.WriterKind

* **`alias_or_version`**

  - **Type**: str | int

* **`loader`**

  - **Type**: registries.LoaderKind

## Public Methods

* **`run(self: Any) -> base.Locals`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

### Output

* **return type**: base.Locals

## Used By

* [__init__.py](../../regression_model_template/jobs/__init__.md)
