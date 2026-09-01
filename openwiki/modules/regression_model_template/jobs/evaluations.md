---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: evaluations"
source_path: "src/regression_model_template/jobs/evaluations.py"
description: "Define a job for evaluating registered models with data."
tags: ["module", "evaluations"]
timestamp: "2026-09-01T16:59:35Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "193029c"
---
# Module Specification: evaluations

* **Source Reference:** [src/regression_model_template/jobs/evaluations.py](../../../../src/regression_model_template/jobs/evaluations.py)

# Module Overview

## Purpose

Define a job for evaluating registered models with data.

## Responsibilities

Define a job for evaluating registered models with data.

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

# Each File Documentation

## Imported modules

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

## Exported classes

* `EvaluationsJob`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

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

### Sequence Diagram

```plantuml
sequenceDiagram
    EvaluationsJob.run->>logger: invoke
    EvaluationsJob.run->>info: invoke
    EvaluationsJob.run->>client: invoke
    EvaluationsJob.run->>locals: invoke
    EvaluationsJob.run->>run_context: invoke
    EvaluationsJob.run->>read: invoke
    EvaluationsJob.run->>check: invoke
    EvaluationsJob.run->>debug: invoke
    EvaluationsJob.run->>lineage: invoke
    EvaluationsJob.run->>log_input: invoke
    EvaluationsJob.run->>from_pandas: invoke
    EvaluationsJob.run->>uri_for_model_alias_or_version: invoke
    EvaluationsJob.run->>evaluate: invoke
    EvaluationsJob.run->>validate_evaluation_results: invoke
    EvaluationsJob.run->>notify: invoke
    EvaluationsJob.run->>to_dict: invoke
    EvaluationsJob.run->>to_mlflow: invoke
    EvaluationsJob.run->>concat: invoke
    EvaluationsJob.run->>items: invoke
```

### Component Diagram

```plantuml
component [evaluations] as Comp
Comp --> [typing]
Comp --> [mlflow]
Comp --> [pandas]
Comp --> [pydantic]
Comp --> [metrics]
Comp --> [schemas]
Comp --> [datasets]
Comp --> [registries]
Comp --> [services]
Comp --> [base]
```

## 3. Class & Method Specifications

# Public Classes

### `EvaluationsJob`

## Overview

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

## Attributes

* **`KIND`**

  - **Type**: T.Literal[EvaluationsJob]

* **`run_config`**

  - **Type**: services.MlflowService.RunConfig

* **`inputs`**

  - **Type**: datasets.ReaderKind

* **`targets`**

  - **Type**: datasets.ReaderKind

* **`model_type`**

  - **Type**: str

* **`alias_or_version`**

  - **Type**: str | int

* **`metrics`**

  - **Type**: metrics_.MetricsKind

* **`evaluators`**

  - **Type**: list[str]

* **`thresholds`**

  - **Type**: dict[(str, metrics_.Threshold)]

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
