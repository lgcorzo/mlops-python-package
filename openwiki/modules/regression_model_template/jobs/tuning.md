---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: tuning"
source_path: "src/regression_model_template/jobs/tuning.py"
description: "Define a job for finding the best hyperparameters for a model."
tags: ["module", "tuning"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: tuning

* **Source Reference:** [src/regression_model_template/jobs/tuning.py](../../../src/regression_model_template/jobs/tuning.py)

## 1. Architectural Role & Responsibilities
Define a job for finding the best hyperparameters for a model.

## 2. UML 2.0 Class Diagram
```plantuml
classDiagram
    direction BT
    class TuningJob {
        +KIND: T.Literal~TuningJob~
        +run_config: services.MlflowService.RunConfig
        +inputs: datasets.ReaderKind
        +targets: datasets.ReaderKind
        +model: models.ModelKind
        +metric: metrics.MetricKind
        +splitter: splitters.SplitterKind
        +searcher: searchers.SearcherKind
        +run(self: Any) base.Locals
    }
    Job <|-- TuningJob : Generalization
```

## 3. Class & Method Specifications

### `TuningJob`

Find the best hyperparameters for a model.

Parameters:
    run_config (services.MlflowService.RunConfig): mlflow run config.
    inputs (datasets.ReaderKind): reader for the inputs data.
    targets (datasets.ReaderKind): reader for the targets data.
    model (models.ModelKind): machine learning model to tune.
    metric (metrics.MetricKind): tuning metric to optimize.
    splitter (splitters.SplitterKind): data sets splitter.
    searcher: (searchers.SearcherKind): hparams searcher.

#### Attributes
* **`KIND`** (`T.Literal[TuningJob]`)
* **`run_config`** (`services.MlflowService.RunConfig`)
* **`inputs`** (`datasets.ReaderKind`)
* **`targets`** (`datasets.ReaderKind`)
* **`model`** (`models.ModelKind`)
* **`metric`** (`metrics.MetricKind`)
* **`splitter`** (`splitters.SplitterKind`)
* **`searcher`** (`searchers.SearcherKind`)

#### Public Methods
* **`run(self: Any) -> base.Locals`**
  - **Purpose**: Run the tuning job in context.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `base.Locals`

## Dependencies

* `typing`
* `mlflow`
* `pydantic`
* `regression_model_template.core.metrics`
* `regression_model_template.core.models`
* `regression_model_template.core.schemas`
* `regression_model_template.io.datasets`
* `regression_model_template.io.services`
* `regression_model_template.jobs.base`
* `regression_model_template.utils.searchers`
* `regression_model_template.utils.splitters`

## Used By

* [__init__.py](../../regression_model_template/jobs/__init__.md)
