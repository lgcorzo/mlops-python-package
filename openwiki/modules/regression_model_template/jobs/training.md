---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: training"
source_path: "src/regression_model_template/jobs/training.py"
description: "Define a job for training and registring a single AI/ML model."
tags: ["module", "training", "regression_model_template"]
timestamp: "2026-08-01T09:57:53Z"
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "8f9670a"
---

# Module Specification: training

* **Source Reference:** [src/regression_model_template/jobs/training.py](../../../src/regression_model_template/jobs/training.py) (Lines: L1-L145)

## 1. Architectural Role & Responsibilities
Define a job for training and registring a single AI/ML model.

## 2. UML 2.0 Class Diagram
```mermaid
classDiagram
    direction BT
    class TrainingJob {
        +KIND: T.Literal['TrainingJob']
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
```

## 2b. Execution Flow (Sequence Diagram)
```mermaid
sequenceDiagram
    autonumber
    participant User as Runner
    participant Job as TrainingJob
    
    User->>Job: run()
    activate Job
    Note over Job: Reads inputs and performs workflow steps
    Job-->>User: Locals (dict)
    deactivate Job
```

## 3. Class & Method Specifications

### `TrainingJob` ([`src/regression_model_template/jobs/training.py:L21-L145`](../../../src/regression_model_template/jobs/training.py#L21-L145))

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

#### Methods

* **`run(self: Any) -> base.Locals`** (L57-L145)
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`): Parameter description.
  - **Outputs**:
    - `base.Locals`: Return value description.
