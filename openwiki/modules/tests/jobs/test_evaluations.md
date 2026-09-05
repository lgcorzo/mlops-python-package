---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_evaluations"
source_path: "tests/jobs/test_evaluations.py"
description: "No description available."
tags: ["module", "test_evaluations"]
timestamp: "2026-09-05T05:14:18Z"
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

## Exported functions

* `test_evaluations_job`

## Exported interfaces

_No interfaces found._

## Public API

_See exported classes and functions._

## Internal architecture

_See architectural detected patterns and UML._

## Execution flow

_Execution flow depends on public API usage._

## Sequence explanation

_See sequence diagram._

## UML

_See diagrams below._

## Examples

_No module level examples available._

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

## 3. Class & Method Specifications

## Standalone Functions

### `test_evaluations_job(alias_or_version: str | int, thresholds: dict[(str, metrics.Threshold)], mlflow_service: services.MlflowService, alerts_service: services.AlertsService, logger_service: services.LoggerService, inputs_reader: datasets.ParquetReader, targets_reader: datasets.ParquetReader, model_alias: registries.Version, metric: metrics.Metric, capsys: pc.CaptureFixture[str]) -> None`

### Description

No description available.

### Inputs

* `alias_or_version`

  - **type**: str | int

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `thresholds`

  - **type**: dict[(str, metrics.Threshold)]

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `mlflow_service`

  - **type**: services.MlflowService

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `alerts_service`

  - **type**: services.AlertsService

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `logger_service`

  - **type**: services.LoggerService

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `inputs_reader`

  - **type**: datasets.ParquetReader

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `targets_reader`

  - **type**: datasets.ParquetReader

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `model_alias`

  - **type**: registries.Version

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `metric`

  - **type**: metrics.Metric

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `capsys`

  - **type**: pc.CaptureFixture[str]

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: None

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for test_evaluations_job

```

## Used By

_Not used by any other module._
