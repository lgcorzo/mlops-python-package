---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_training"
source_path: "tests/jobs/test_training.py"
description: "No description available."
tags: ["module", "test_training"]
timestamp: "2026-08-28T06:13:58Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "3029bb6"
---
# Module Specification: test_training

* **Source Reference:** [tests/jobs/test_training.py](../../../../tests/jobs/test_training.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `_pytest.capture`

* `regression_model_template.jobs`

* `regression_model_template.core.metrics`

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

* `regression_model_template.io.registries`

* `regression_model_template.io.services`

* `regression_model_template.utils.signers`

* `regression_model_template.utils.splitters`

# Each File Documentation

## Imported modules

* `_pytest.capture`

* `regression_model_template.jobs`

* `regression_model_template.core.metrics`

* `regression_model_template.core.models`

* `regression_model_template.core.schemas`

* `regression_model_template.io.datasets`

* `regression_model_template.io.registries`

* `regression_model_template.io.services`

* `regression_model_template.utils.signers`

* `regression_model_template.utils.splitters`

## Exported functions

* `test_training_job`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    test_training_job->>RunConfig: invoke
    test_training_job->>client: invoke
    test_training_job->>TrainingJob: invoke
    test_training_job->>get_experiment_by_name: invoke
    test_training_job->>search_runs: invoke
    test_training_job->>get_model_version: invoke
    test_training_job->>run: invoke
    test_training_job->>set: invoke
    test_training_job->>values: invoke
    test_training_job->>items: invoke
    test_training_job->>len: invoke
    test_training_job->>float: invoke
    test_training_job->>readouterr: invoke
```

### Component Diagram

```plantuml
component [test_training] as Comp
Comp --> [capture]
Comp --> [jobs]
Comp --> [metrics]
Comp --> [models]
Comp --> [schemas]
Comp --> [datasets]
Comp --> [registries]
Comp --> [services]
Comp --> [signers]
Comp --> [splitters]
```

## 3. Class & Method Specifications

## Standalone Functions

### `test_training_job(mlflow_service: services.MlflowService, alerts_service: services.AlertsService, logger_service: services.LoggerService, inputs_reader: datasets.ParquetReader, targets_reader: datasets.ParquetReader, model: models.Model, metric: metrics.Metric, train_test_splitter: splitters.Splitter, saver: registries.Saver, signer: signers.Signer, register: registries.Register, capsys: pc.CaptureFixture[str]) -> None`

### Description

No description available.

### Inputs

* `mlflow_service`

  - **type**: services.MlflowService

  - **optional?**: No

* `alerts_service`

  - **type**: services.AlertsService

  - **optional?**: No

* `logger_service`

  - **type**: services.LoggerService

  - **optional?**: No

* `inputs_reader`

  - **type**: datasets.ParquetReader

  - **optional?**: No

* `targets_reader`

  - **type**: datasets.ParquetReader

  - **optional?**: No

* `model`

  - **type**: models.Model

  - **optional?**: No

* `metric`

  - **type**: metrics.Metric

  - **optional?**: No

* `train_test_splitter`

  - **type**: splitters.Splitter

  - **optional?**: No

* `saver`

  - **type**: registries.Saver

  - **optional?**: No

* `signer`

  - **type**: signers.Signer

  - **optional?**: No

* `register`

  - **type**: registries.Register

  - **optional?**: No

* `capsys`

  - **type**: pc.CaptureFixture[str]

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
