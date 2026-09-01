---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_inference"
source_path: "tests/jobs/test_inference.py"
description: "No description available."
tags: ["module", "test_inference"]
timestamp: "2026-09-01T16:59:35Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "193029c"
---
# Module Specification: test_inference

* **Source Reference:** [tests/jobs/test_inference.py](../../../../tests/jobs/test_inference.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `_pytest.capture`

* `pytest`

* `regression_model_template.jobs`

* `regression_model_template.io.datasets`

* `regression_model_template.io.registries`

* `regression_model_template.io.services`

# Each File Documentation

## Imported modules

* `_pytest.capture`

* `pytest`

* `regression_model_template.jobs`

* `regression_model_template.io.datasets`

* `regression_model_template.io.registries`

* `regression_model_template.io.services`

## Exported functions

* `test_inference_job`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    test_inference_job->>parametrize: invoke
    test_inference_job->>isinstance: invoke
    test_inference_job->>InferenceJob: invoke
    test_inference_job->>get: invoke
    test_inference_job->>run: invoke
    test_inference_job->>set: invoke
    test_inference_job->>str: invoke
    test_inference_job->>readouterr: invoke
```

### Component Diagram

```plantuml
component [test_inference] as Comp
Comp --> [capture]
Comp --> [pytest]
Comp --> [jobs]
Comp --> [datasets]
Comp --> [registries]
Comp --> [services]
```

## 3. Class & Method Specifications

## Standalone Functions

### `test_inference_job(alias_or_version: str | int, mlflow_service: services.MlflowService, alerts_service: services.AlertsService, logger_service: services.LoggerService, inputs_reader: datasets.Reader, tmp_outputs_writer: datasets.Writer, model_alias: registries.Version, loader: registries.Loader, capsys: pc.CaptureFixture[str]) -> None`

### Description

No description available.

### Inputs

* `alias_or_version`

  - **type**: str | int

  - **optional?**: No

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

  - **type**: datasets.Reader

  - **optional?**: No

* `tmp_outputs_writer`

  - **type**: datasets.Writer

  - **optional?**: No

* `model_alias`

  - **type**: registries.Version

  - **optional?**: No

* `loader`

  - **type**: registries.Loader

  - **optional?**: No

* `capsys`

  - **type**: pc.CaptureFixture[str]

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
