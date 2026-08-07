---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: training"
source_path: "src/regression_model_template/jobs/training.py"
description: "Define a job for training and registring a single AI/ML model."
tags: ["module", "training"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: training

* **Source Reference:** [src/regression_model_template/jobs/training.py](../../../src/regression_model_template/jobs/training.py)

## 1. Architectural Role & Responsibilities
Define a job for training and registring a single AI/ML model.

## 2. UML 2.0 Class Diagram
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

## 3. Class & Method Specifications

### `TrainingJob`

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

#### Attributes
* **`KIND`** (`T.Literal[TrainingJob]`)
* **`run_config`** (`services.MlflowService.RunConfig`)
* **`inputs`** (`datasets.ReaderKind`)
* **`targets`** (`datasets.ReaderKind`)
* **`model`** (`models.ModelKind`)
* **`metrics`** (`metrics_.MetricsKind`)
* **`splitter`** (`splitters.SplitterKind`)
* **`saver`** (`registries.SaverKind`)
* **`signer`** (`signers.SignerKind`)
* **`registry`** (`registries.RegisterKind`)

#### Public Methods
* **`run(self: Any) -> base.Locals`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `base.Locals`

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

## Used By

* [__init__.py](../../regression_model_template/jobs/__init__.md)
