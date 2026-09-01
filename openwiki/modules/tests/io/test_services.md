---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_services"
source_path: "tests/io/test_services.py"
description: "No description available."
tags: ["module", "test_services"]
timestamp: "2026-09-01T16:59:35Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "193029c"
---
# Module Specification: test_services

* **Source Reference:** [tests/io/test_services.py](../../../../tests/io/test_services.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `_pytest.capture`

* `_pytest.logging`

* `mlflow`

* `plyer`

* `pytest`

* `pytest_mock`

* `regression_model_template.io.services`

# Each File Documentation

## Imported modules

* `_pytest.capture`

* `_pytest.logging`

* `mlflow`

* `plyer`

* `pytest`

* `pytest_mock`

* `regression_model_template.io.services`

## Exported functions

* `test_logger_service`

* `test_alerts_service`

* `test_mlflow_service`

### Detected Architecture Patterns

Detected roles: Service

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    test_logger_service->>logger: invoke
    test_logger_service->>debug: invoke
    test_logger_service->>error: invoke
    test_alerts_service->>parametrize: invoke
    test_alerts_service->>AlertsService: invoke
    test_alerts_service->>patch: invoke
    test_alerts_service->>notify: invoke
    test_alerts_service->>assert_called_once: invoke
    test_alerts_service->>assert_not_called: invoke
    test_alerts_service->>readouterr: invoke
    test_mlflow_service->>RunConfig: invoke
    test_mlflow_service->>client: invoke
    test_mlflow_service->>get_run: invoke
    test_mlflow_service->>get_experiment_by_name: invoke
    test_mlflow_service->>run_context: invoke
    test_mlflow_service->>get_tracking_uri: invoke
    test_mlflow_service->>get_registry_uri: invoke
    test_mlflow_service->>values: invoke
    test_mlflow_service->>items: invoke
```

### Component Diagram

```plantuml
component [test_services] as Comp
Comp --> [capture]
Comp --> [logging]
Comp --> [mlflow]
Comp --> [plyer]
Comp --> [pytest]
Comp --> [pytest_mock]
Comp --> [services]
```

## 3. Class & Method Specifications

## Standalone Functions

### `test_logger_service(logger_service: services.LoggerService, logger_caplog: pl.LogCaptureFixture) -> None`

### Description

No description available.

### Inputs

* `logger_service`

  - **type**: services.LoggerService

  - **optional?**: No

* `logger_caplog`

  - **type**: pl.LogCaptureFixture

  - **optional?**: No

### Output

* **return type**: None

### `test_alerts_service(enable: bool, mocker: pm.MockerFixture, capsys: pc.CaptureFixture[str]) -> None`

### Description

No description available.

### Inputs

* `enable`

  - **type**: bool

  - **optional?**: No

* `mocker`

  - **type**: pm.MockerFixture

  - **optional?**: No

* `capsys`

  - **type**: pc.CaptureFixture[str]

  - **optional?**: No

### Output

* **return type**: None

### `test_mlflow_service(mlflow_service: services.MlflowService) -> None`

### Description

No description available.

### Inputs

* `mlflow_service`

  - **type**: services.MlflowService

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
