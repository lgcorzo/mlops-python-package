---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: evaluations"
source_path: "src/regression_model_template/jobs/evaluations.py"
description: "Define a job for evaluating registered models with data."
tags: ["module", "evaluations"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: evaluations

* **Source Reference:** [src/regression_model_template/jobs/evaluations.py](../../../src/regression_model_template/jobs/evaluations.py)

## 1. Architectural Role & Responsibilities
Define a job for evaluating registered models with data.

## 2. UML 2.0 Class Diagram
```plantuml
classDiagram
    direction BT
    class EvaluationsJob {
        +KIND: T.Literal~EvaluationsJob~
        +run_config: services.MlflowService.RunConfig
        +inputs: datasets.ReaderKind
        +targets: datasets.ReaderKind
        +model_type: str
        +alias_or_version: str | int
        +metrics: metrics_.MetricsKind
        +evaluators: list~str~
        +thresholds: dict~(str, metrics_.Threshold)~
        +run(self: Any) base.Locals
    }
    Job <|-- EvaluationsJob : Generalization
```

## 3. Class & Method Specifications

### `EvaluationsJob`

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

#### Attributes
* **`KIND`** (`T.Literal[EvaluationsJob]`)
* **`run_config`** (`services.MlflowService.RunConfig`)
* **`inputs`** (`datasets.ReaderKind`)
* **`targets`** (`datasets.ReaderKind`)
* **`model_type`** (`str`)
* **`alias_or_version`** (`str | int`)
* **`metrics`** (`metrics_.MetricsKind`)
* **`evaluators`** (`list[str]`)
* **`thresholds`** (`dict[(str, metrics_.Threshold)]`)

#### Public Methods
* **`run(self: Any) -> base.Locals`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `base.Locals`

## Dependencies

* `typing`
* `mlflow`
* `pandas`
* `pydantic`
* `regression_model_template.core.metrics`
* `regression_model_template.core.schemas`
* `regression_model_template.io.datasets`
* `regression_model_template.io.registries`
* `regression_model_template.io.services`
* `regression_model_template.jobs.base`

## Used By

* [__init__.py](../../regression_model_template/jobs/__init__.md)
