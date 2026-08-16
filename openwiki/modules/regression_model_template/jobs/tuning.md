---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: tuning"
source_path: "src/regression_model_template/jobs/tuning.py"
description: "Define a job for finding the best hyperparameters for a model."
tags: ["module", "tuning"]
timestamp: "2026-08-16T06:27:37Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "034727a"
---
# Module Specification: tuning

* **Source Reference:** [src/regression_model_template/jobs/tuning.py](../../../../src/regression_model_template/jobs/tuning.py)

## 1. Architectural Role & Responsibilities

Define a job for finding the best hyperparameters for a model.

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

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


### Sequence Diagram

```plantuml
sequenceDiagram
    TuningJob.run->>logger: invoke
    TuningJob.run->>info: invoke
    TuningJob.run->>locals: invoke
    TuningJob.run->>run_context: invoke
    TuningJob.run->>read: invoke
    TuningJob.run->>check: invoke
    TuningJob.run->>debug: invoke
    TuningJob.run->>lineage: invoke
    TuningJob.run->>log_input: invoke
    TuningJob.run->>search: invoke
    TuningJob.run->>notify: invoke
    TuningJob.run->>to_dict: invoke
```

### Component Diagram

```plantuml
component [tuning] as Comp
Comp --> [typing]
Comp --> [mlflow]
Comp --> [pydantic]
Comp --> [metrics]
Comp --> [models]
Comp --> [schemas]
Comp --> [datasets]
Comp --> [services]
Comp --> [base]
Comp --> [searchers]
Comp --> [splitters]
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
