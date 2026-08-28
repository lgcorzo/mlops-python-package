---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: training"
source_path: "src/regression_model_template/jobs/training.py"
description: "Define a job for training and registring a single AI/ML model."
tags: ["module", "training"]
timestamp: "2026-08-28T06:13:58Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "3029bb6"
---
# Module Specification: training

* **Source Reference:** [src/regression_model_template/jobs/training.py](../../../../src/regression_model_template/jobs/training.py)

# Module Overview

## Purpose

Define a job for training and registring a single AI/ML model.

## Responsibilities

Define a job for training and registring a single AI/ML model.

## Dependencies

* `time`

* `typing`

* `mlflow`

* `pydantic`

* `mlflow.entities.Metric`

* `regression_model_template.core.metrics`

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

* `regression_model_template.io.registries`

* `regression_model_template.io.services`

* `regression_model_template.jobs.base`

* `regression_model_template.utils.signers`

* `regression_model_template.utils.splitters`

# Each File Documentation

## Imported modules

* `time`

* `typing`

* `mlflow`

* `pydantic`

* `mlflow.entities.Metric`

* `regression_model_template.core.metrics`

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

* `regression_model_template.io.registries`

* `regression_model_template.io.services`

* `regression_model_template.jobs.base`

* `regression_model_template.utils.signers`

* `regression_model_template.utils.splitters`

## Exported classes

* `TrainingJob`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

```plantuml
classDiagram
    direction BT
    class TrainingJob {
        +KIND: T.Literal~TrainingJob~
        +run_config: services.MlflowService.RunConfig
        +inputs: datasets.ReaderKind
        +targets: datasets.ReaderKind
        +model: models.ModelKind
        +metrics: metrics_.MetricsKind
        +splitter: splitters.SplitterKind
        +saver: registries.SaverKind
        +signer: signers.SignerKind
        +registry: registries.RegisterKind
        +run(self: Any) base.Locals
    }
    Job <|-- TrainingJob : Generalization
```

### Sequence Diagram

```plantuml
sequenceDiagram
    TrainingJob.run->>logger: invoke
    TrainingJob.run->>info: invoke
    TrainingJob.run->>client: invoke
    TrainingJob.run->>locals: invoke
    TrainingJob.run->>run_context: invoke
    TrainingJob.run->>read: invoke
    TrainingJob.run->>check: invoke
    TrainingJob.run->>debug: invoke
    TrainingJob.run->>lineage: invoke
    TrainingJob.run->>log_input: invoke
    TrainingJob.run->>next: invoke
    TrainingJob.run->>fit: invoke
    TrainingJob.run->>predict: invoke
    TrainingJob.run->>enumerate: invoke
    TrainingJob.run->>len: invoke
    TrainingJob.run->>log_batch: invoke
    TrainingJob.run->>sign: invoke
    TrainingJob.run->>save: invoke
    TrainingJob.run->>register: invoke
    TrainingJob.run->>notify: invoke
    TrainingJob.run->>to_dict: invoke
    TrainingJob.run->>split: invoke
    TrainingJob.run->>score: invoke
    TrainingJob.run->>head: invoke
    TrainingJob.run->>Metric: invoke
    TrainingJob.run->>items: invoke
    TrainingJob.run->>int: invoke
    TrainingJob.run->>time: invoke
```

### Component Diagram

```plantuml
component [training] as Comp
Comp --> [time]
Comp --> [typing]
Comp --> [mlflow]
Comp --> [pydantic]
Comp --> [Metric]
Comp --> [metrics]
Comp --> [models]
Comp --> [schemas]
Comp --> [datasets]
Comp --> [registries]
Comp --> [services]
Comp --> [base]
Comp --> [signers]
Comp --> [splitters]
```

## 3. Class & Method Specifications

# Public Classes

### `TrainingJob`

## Overview

Train and register a single AI/ML model.

Parameters:
    run_config (services.MlflowService.RunConfig): mlflow run config.
    inputs (datasets.ReaderKind): reader for the inputs data.
    targets (datasets.ReaderKind): reader for the targets data.
    model (models.ModelKind): machine learning model to train.
    metrics (metrics_.MetricKind): metrics for the reporting.
    splitter (splitters.SplitterKind): data sets splitter.
    saver (registries.SaverKind): model saver.
    signer (signers.SignerKind): model signer.
    registry (registries.RegisterKind): model register.

## Attributes

* **`KIND`**

  - **Type**: T.Literal[TrainingJob]

* **`run_config`**

  - **Type**: services.MlflowService.RunConfig

* **`inputs`**

  - **Type**: datasets.ReaderKind

* **`targets`**

  - **Type**: datasets.ReaderKind

* **`model`**

  - **Type**: models.ModelKind

* **`metrics`**

  - **Type**: metrics_.MetricsKind

* **`splitter`**

  - **Type**: splitters.SplitterKind

* **`saver`**

  - **Type**: registries.SaverKind

* **`signer`**

  - **Type**: signers.SignerKind

* **`registry`**

  - **Type**: registries.RegisterKind

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
