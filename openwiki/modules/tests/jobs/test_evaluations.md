---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_evaluations"
source_path: "tests/jobs/test_evaluations.py"
description: "No description available."
tags: ["module", "test_evaluations"]
timestamp: "2026-09-06T06:26:19Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: test_evaluations

* **Source Reference:** [tests/jobs/test_evaluations.py](../../../../tests/jobs/test_evaluations.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `_pytest.capture`

* `pytest`

* `regression_model_template.jobs`

* `regression_model_template.core.metrics`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

* `regression_model_template.io.registries`

* `regression_model_template.io.services`

# Each File Documentation

## Imported modules

* `_pytest.capture`

* `pytest`

* `regression_model_template.jobs`

* `regression_model_template.core.metrics`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

* `regression_model_template.io.registries`

* `regression_model_template.io.services`

## Exported interfaces

_Dependent on implementation_

## Exported functions

* `test_evaluations_job`

## Public API

_Dependent on implementation_

## Internal architecture

_Dependent on implementation_

## Execution flow

_Dependent on implementation_

## Sequence explanation

_Dependent on implementation_

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    test_evaluations_job->>parametrize: invoke
    test_evaluations_job->>isinstance: invoke
    test_evaluations_job->>RunConfig: invoke
    test_evaluations_job->>EvaluationsJob: invoke
    test_evaluations_job->>get_experiment_by_name: invoke
    test_evaluations_job->>search_runs: invoke
    test_evaluations_job->>run: invoke
    test_evaluations_job->>set: invoke
    test_evaluations_job->>values: invoke
    test_evaluations_job->>items: invoke
    test_evaluations_job->>str: invoke
    test_evaluations_job->>len: invoke
    test_evaluations_job->>keys: invoke
    test_evaluations_job->>param: invoke
    test_evaluations_job->>client: invoke
    test_evaluations_job->>readouterr: invoke
    test_evaluations_job->>Threshold: invoke
    test_evaluations_job->>xfail: invoke
    test_evaluations_job->>float: invoke
```

### Component Diagram

```plantuml
component [test_evaluations] as Comp
Comp --> [capture]
Comp --> [pytest]
Comp --> [jobs]
Comp --> [metrics]
Comp --> [schemas]
Comp --> [datasets]
Comp --> [registries]
Comp --> [services]
```

## Examples

_Dependent on implementation_

## 3. Class & Method Specifications

## Standalone Functions

### `test_evaluations_job(alias_or_version: str | int, thresholds: dict[(str, metrics.Threshold)], mlflow_service: services.MlflowService, alerts_service: services.AlertsService, logger_service: services.LoggerService, inputs_reader: datasets.ParquetReader, targets_reader: datasets.ParquetReader, model_alias: registries.Version, metric: metrics.Metric, capsys: pc.CaptureFixture[str]) -> None`

### Description

No description available.

### Inputs

* `alias_or_version`

  - **type**: str | int

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `thresholds`

  - **type**: dict[(str, metrics.Threshold)]

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `mlflow_service`

  - **type**: services.MlflowService

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `alerts_service`

  - **type**: services.AlertsService

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `logger_service`

  - **type**: services.LoggerService

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `inputs_reader`

  - **type**: datasets.ParquetReader

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `targets_reader`

  - **type**: datasets.ParquetReader

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `model_alias`

  - **type**: registries.Version

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `metric`

  - **type**: metrics.Metric

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `capsys`

  - **type**: pc.CaptureFixture[str]

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: None

* **semantic meaning**: _Dependent on implementation_

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

## Used By

_Not used by any other module._
