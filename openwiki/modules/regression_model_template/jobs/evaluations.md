---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: evaluations"
source_path: "src/regression_model_template/jobs/evaluations.py"
description: "Define a job for evaluating registered models with data."
tags: ["module", "evaluations", "regression_model_template"]
timestamp: "2026-08-01T09:57:53Z"
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "8f9670a"
---

# Module Specification: evaluations

* **Source Reference:** [src/regression_model_template/jobs/evaluations.py](../../../src/regression_model_template/jobs/evaluations.py) (Lines: L1-L125)

## 1. Architectural Role & Responsibilities
Define a job for evaluating registered models with data.

## 2. UML 2.0 Class Diagram
```mermaid
classDiagram
    direction BT
    class EvaluationsJob {
        +KIND: T.Literal['EvaluationsJob']
        +run_config: services.MlflowService.RunConfig
        +inputs: datasets.ReaderKind
        +targets: datasets.ReaderKind
        +model_type: str
        +alias_or_version: str | int
        +metrics: metrics_.MetricsKind
        +evaluators: list[str]
        +thresholds: dict[str, metrics_.Threshold]
        +run(self: Any) base.Locals
    }
```

## 2b. Execution Flow (Sequence Diagram)
```mermaid
sequenceDiagram
    autonumber
    participant User as Runner
    participant Job as EvaluationsJob
    
    User->>Job: run()
    activate Job
    Note over Job: Reads inputs and performs workflow steps
    Job-->>User: Locals (dict)
    deactivate Job
```

## 3. Class & Method Specifications

### `EvaluationsJob` ([`src/regression_model_template/jobs/evaluations.py:L19-L125`](../../../src/regression_model_template/jobs/evaluations.py#L19-L125))

Generate evaluations from a registered model and a dataset.

Parameters:
    run_config (services.MlflowService.RunConfig): mlflow run config.
    inputs (datasets.ReaderKind): reader for the inputs data.
    targets (datasets.ReaderKind): reader for the targets data.
    model_type (str): model type (e.g. "regressor", "classifier").
    alias_or_version (str | int): alias or version for the  model.
    metrics (metrics_.MetricKind): metrics for the reporting.
    evaluators (list[str]): list of evaluators to use.
    thresholds (dict[str, metrics_.Threshold] | None): metric thresholds.

#### Methods

* **`run(self: Any) -> base.Locals`** (L50-L125)
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`): Parameter description.
  - **Outputs**:
    - `base.Locals`: Return value description.
