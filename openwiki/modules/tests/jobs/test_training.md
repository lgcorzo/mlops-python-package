---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_training"
source_path: "tests/jobs/test_training.py"
description: "No description available."
tags: ["module", "test_training"]
timestamp: "2026-09-06T06:26:19Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
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

## Exported interfaces

_Dependent on implementation_

## Exported functions

* `test_training_job`

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

## Examples

_Dependent on implementation_

## 3. Class & Method Specifications

## Standalone Functions

### `test_training_job(mlflow_service: services.MlflowService, alerts_service: services.AlertsService, logger_service: services.LoggerService, inputs_reader: datasets.ParquetReader, targets_reader: datasets.ParquetReader, model: models.Model, metric: metrics.Metric, train_test_splitter: splitters.Splitter, saver: registries.Saver, signer: signers.Signer, register: registries.Register, capsys: pc.CaptureFixture[str]) -> None`

### Description

No description available.

### Inputs

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

* `model`

  - **type**: models.Model

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `metric`

  - **type**: metrics.Metric

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `train_test_splitter`

  - **type**: splitters.Splitter

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `saver`

  - **type**: registries.Saver

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `signer`

  - **type**: signers.Signer

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `register`

  - **type**: registries.Register

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
