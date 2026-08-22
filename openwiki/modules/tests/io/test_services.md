---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_services"
source_path: "tests/io/test_services.py"
description: "No description available."
tags: ["module", "test_services"]
timestamp: "2026-08-21T05:06:05Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "32cdac7"
---
# Module Specification: test_services

* **Source Reference:** [tests/io/test_services.py](../../../../tests/io/test_services.py)

## 1. Architectural Role & Responsibilities

No description available.

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

No description available.

#### Inputs

* `logger_service` (`services.LoggerService`)

* `logger_caplog` (`pl.LogCaptureFixture`)

#### Outputs
* `None`

### `test_alerts_service(enable: bool, mocker: pm.MockerFixture, capsys: pc.CaptureFixture[str]) -> None`

No description available.

#### Inputs

* `enable` (`bool`)

* `mocker` (`pm.MockerFixture`)

* `capsys` (`pc.CaptureFixture[str]`)

#### Outputs
* `None`

### `test_mlflow_service(mlflow_service: services.MlflowService) -> None`

No description available.

#### Inputs

* `mlflow_service` (`services.MlflowService`)

#### Outputs
* `None`

## Dependencies

* `_pytest.capture`

* `_pytest.logging`

* `mlflow`

* `plyer`

* `pytest`

* `pytest_mock`

* `regression_model_template.io.services`

## Used By

_Not used by any other module._
