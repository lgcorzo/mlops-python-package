---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: tuning"
source_path: "src/regression_model_template/jobs/tuning.py"
description: "Define a job for finding the best hyperparameters for a model."
tags: ["module", "tuning", "regression_model_template"]
timestamp: "2026-08-01T09:57:53Z"
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "8f9670a"
---

# Module Specification: tuning

* **Source Reference:** [src/regression_model_template/jobs/tuning.py](../../../src/regression_model_template/jobs/tuning.py) (Lines: L1-L104)

## 1. Architectural Role & Responsibilities
Define a job for finding the best hyperparameters for a model.

## 2. UML 2.0 Class Diagram
```mermaid
classDiagram
    direction BT
    class TuningJob {
        +KIND: T.Literal['TuningJob']
        +run_config: services.MlflowService.RunConfig
        +inputs: datasets.ReaderKind
        +targets: datasets.ReaderKind
        +model: models.ModelKind
        +metric: metrics.MetricKind
        +splitter: splitters.SplitterKind
        +searcher: searchers.SearcherKind
        +run(self: Any) base.Locals
    }
```

## 2b. Execution Flow (Sequence Diagram)
```mermaid
sequenceDiagram
    autonumber
    participant User as Runner
    participant Job as TuningJob
    
    User->>Job: run()
    activate Job
    Note over Job: Reads inputs and performs workflow steps
    Job-->>User: Locals (dict)
    deactivate Job
```

## 3. Class & Method Specifications

### `TuningJob` ([`src/regression_model_template/jobs/tuning.py:L18-L104`](../../../src/regression_model_template/jobs/tuning.py#L18-L104))

Find the best hyperparameters for a model.

Parameters:
    run_config (services.MlflowService.RunConfig): mlflow run config.
    inputs (datasets.ReaderKind): reader for the inputs data.
    targets (datasets.ReaderKind): reader for the targets data.
    model (models.ModelKind): machine learning model to tune.
    metric (metrics.MetricKind): tuning metric to optimize.
    splitter (splitters.SplitterKind): data sets splitter.
    searcher: (searchers.SearcherKind): hparams searcher.

#### Methods

* **`run(self: Any) -> base.Locals`** (L54-L104)
  - **Purpose**: Run the tuning job in context.
  - **Inputs**:
    - `self` (`Any`): Parameter description.
  - **Outputs**:
    - `base.Locals`: Return value description.
