---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_tuning"
source_path: "tests/jobs/test_tuning.py"
description: "No description available."
tags: ["module", "test_tuning"]
timestamp: "2026-08-20T05:56:47Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "32cdac7"
---
# Module Specification: test_tuning

* **Source Reference:** [tests/jobs/test_tuning.py](../../../../tests/jobs/test_tuning.py)

## 1. Architectural Role & Responsibilities

No description available.

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    test_tuning_job->>RunConfig: invoke
    test_tuning_job->>client: invoke
    test_tuning_job->>TuningJob: invoke
    test_tuning_job->>get_experiment_by_name: invoke
    test_tuning_job->>search_runs: invoke
    test_tuning_job->>run: invoke
    test_tuning_job->>set: invoke
    test_tuning_job->>values: invoke
    test_tuning_job->>items: invoke
    test_tuning_job->>float: invoke
    test_tuning_job->>keys: invoke
    test_tuning_job->>len: invoke
    test_tuning_job->>readouterr: invoke
```

### Component Diagram

```plantuml
component [test_tuning] as Comp
Comp --> [capture]
Comp --> [jobs]
Comp --> [metrics]
Comp --> [models]
Comp --> [schemas]
Comp --> [datasets]
Comp --> [services]
Comp --> [searchers]
Comp --> [splitters]
```

## 3. Class & Method Specifications

## Standalone Functions

### `test_tuning_job(mlflow_service: services.MlflowService, alerts_service: services.AlertsService, logger_service: services.LoggerService, inputs_reader: datasets.ParquetReader, targets_reader: datasets.ParquetReader, model: models.Model, metric: metrics.Metric, time_series_splitter: splitters.Splitter, searcher: searchers.Searcher, capsys: pc.CaptureFixture[str]) -> None`

No description available.

#### Inputs

* `mlflow_service` (`services.MlflowService`)

* `alerts_service` (`services.AlertsService`)

* `logger_service` (`services.LoggerService`)

* `inputs_reader` (`datasets.ParquetReader`)

* `targets_reader` (`datasets.ParquetReader`)

* `model` (`models.Model`)

* `metric` (`metrics.Metric`)

* `time_series_splitter` (`splitters.Splitter`)

* `searcher` (`searchers.Searcher`)

* `capsys` (`pc.CaptureFixture[str]`)

#### Outputs
* `None`

## Dependencies

* `_pytest.capture`

* `regression_model_template.jobs`

* `regression_model_template.core.metrics`

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

* `regression_model_template.io.services`

* `regression_model_template.utils.searchers`

* `regression_model_template.utils.splitters`

## Used By

_Not used by any other module._
