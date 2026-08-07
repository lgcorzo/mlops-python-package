---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: services"
source_path: "src/regression_model_template/io/services.py"
description: "Manage global context during execution."
tags: ["module", "services"]
timestamp: "2026-08-07T08:29:41Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "12aa8d5"
---
# Module Specification: services

* **Source Reference:** [src/regression_model_template/io/services.py](../../../src/regression_model_template/io/services.py)

## 1. Architectural Role & Responsibilities
Manage global context during execution.

## 2. UML 2.0 Class Diagram
```plantuml
classDiagram
    direction BT
    class PropagateHandler {
        +emit(self: Any, record: logging.LogRecord) None
    }
    Handler <|-- PropagateHandler : Generalization
    class Service {
        +start(self: Any) None
        +stop(self: Any) None
    }
    ABC <|-- Service : Generalization
    BaseModel <|-- Service : Generalization
    class LoggerService {
        +sink: str
        +level: str
        +format: str
        +colorize: bool
        +serialize: bool
        +backtrace: bool
        +diagnose: bool
        +catch: bool
        +start(self: Any) None
        +logger(self: Any) loguru.Logger
    }
    Service <|-- LoggerService : Generalization
    class AlertsService {
        +enable: bool
        +app_name: str
        +timeout: int | None
        +start(self: Any) None
        +notify(self: Any, title: str, message: str) None
    }
    Service <|-- AlertsService : Generalization
    class MlflowService {
        +env: ClassVar~Env~
        +tracking_uri: str
        +registry_uri: str
        +experiment_name: str
        +registry_name: str
        +autolog_disable: bool
        +autolog_disable_for_unsupported_versions: bool
        +autolog_exclusive: bool
        +autolog_log_input_examples: bool
        +autolog_log_model_signatures: bool
        +autolog_log_models: bool
        +autolog_log_datasets: bool
        +autolog_silent: bool
        +start(self: Any) None
        +run_context(self: Any, run_config: RunConfig) T.Generator~(mlflow.ActiveRun, None, None)~
        +client(self: Any) mt.MlflowClient
    }
    Service <|-- MlflowService : Generalization
```

## 3. Class & Method Specifications

### `PropagateHandler`

No description available.

#### Public Methods
* **`emit(self: Any, record: logging.LogRecord) -> None`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
    - `record` (`logging.LogRecord`)
  - **Outputs**: `None`

### `Service`

Base class for a global service.

Use services to manage global contexts.
e.g., logger object, mlflow client, spark context, ...

#### Public Methods
* **`start(self: Any) -> None`**
  - **Purpose**: Start the service.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `None`
* **`stop(self: Any) -> None`**
  - **Purpose**: Stop the service.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `None`

### `LoggerService`

Service for logging messages.

https://loguru.readthedocs.io/en/stable/api/logger.html

Parameters:
    sink (str): logging output.
    level (str): logging level.
    format (str): logging format.
    colorize (bool): colorize output.
    serialize (bool): convert to JSON.
    backtrace (bool): enable exception trace.
    diagnose (bool): enable variable display.
    catch (bool): catch errors during log handling.

#### Attributes
* **`sink`** (`str`)
* **`level`** (`str`)
* **`format`** (`str`)
* **`colorize`** (`bool`)
* **`serialize`** (`bool`)
* **`backtrace`** (`bool`)
* **`diagnose`** (`bool`)
* **`catch`** (`bool`)

#### Public Methods
* **`start(self: Any) -> None`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `None`
* **`logger(self: Any) -> loguru.Logger`**
  - **Purpose**: Return the main logger.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `loguru.Logger`

### `AlertsService`

Service for sending notifications.

Require libnotify-bin on Linux systems.

In production, use with Slack, Discord, or emails.

https://plyer.readthedocs.io/en/latest/api.html#plyer.facades.Notification

Parameters:
    enable (bool): use notifications or print.
    app_name (str): name of the application.
    timeout (int | None): timeout in secs.

#### Attributes
* **`enable`** (`bool`)
* **`app_name`** (`str`)
* **`timeout`** (`int | None`)

#### Public Methods
* **`start(self: Any) -> None`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `None`
* **`notify(self: Any, title: str, message: str) -> None`**
  - **Purpose**: Send a notification to the system.
  - **Inputs**:
    - `self` (`Any`)
    - `title` (`str`)
    - `message` (`str`)
  - **Outputs**: `None`

### `MlflowService`

Service for Mlflow tracking and registry.

Parameters:
    tracking_uri (str): the URI for the Mlflow tracking server.
    registry_uri (str): the URI for the Mlflow model registry.
    experiment_name (str): the name of tracking experiment.
    registry_name (str): the name of model registry.
    autolog_disable (bool): disable autologging.
    autolog_disable_for_unsupported_versions (bool): disable autologging for unsupported versions.
    autolog_exclusive (bool): If True, enables exclusive autologging.
    autolog_log_input_examples (bool): If True, logs input examples during autologging.
    autolog_log_model_signatures (bool): If True, logs model signatures during autologging.
    autolog_log_models (bool): If True, enables logging of models during autologging.
    autolog_log_datasets (bool): If True, logs datasets used during autologging.
    autolog_silent (bool): If True, suppresses all Mlflow warnings during autologging.

#### Attributes
* **`env`** (`ClassVar[Env]`)
* **`tracking_uri`** (`str`)
* **`registry_uri`** (`str`)
* **`experiment_name`** (`str`)
* **`registry_name`** (`str`)
* **`autolog_disable`** (`bool`)
* **`autolog_disable_for_unsupported_versions`** (`bool`)
* **`autolog_exclusive`** (`bool`)
* **`autolog_log_input_examples`** (`bool`)
* **`autolog_log_model_signatures`** (`bool`)
* **`autolog_log_models`** (`bool`)
* **`autolog_log_datasets`** (`bool`)
* **`autolog_silent`** (`bool`)

#### Public Methods
* **`start(self: Any) -> None`**
  - **Purpose**: No description available.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `None`
* **`run_context(self: Any, run_config: RunConfig) -> T.Generator[(mlflow.ActiveRun, None, None)]`**
  - **Purpose**: Yield an active Mlflow run and exit it afterwards.
  - **Inputs**:
    - `self` (`Any`)
    - `run_config` (`RunConfig`)
  - **Outputs**: `T.Generator[(mlflow.ActiveRun, None, None)]`
* **`client(self: Any) -> mt.MlflowClient`**
  - **Purpose**: Return a new Mlflow client.
  - **Inputs**:
    - `self` (`Any`)
  - **Outputs**: `mt.MlflowClient`

## Dependencies

* `__future__.annotations`
* `abc`
* `contextlib`
* `logging`
* `sys`
* `typing`
* `typing.ClassVar`
* `loguru`
* `mlflow`
* `mlflow.tracking`
* `pydantic`
* `opentelemetry.trace`
* `opentelemetry._logs.set_logger_provider`
* `opentelemetry.exporter.otlp.proto.http._log_exporter.OTLPLogExporter`
* `opentelemetry.exporter.otlp.proto.http.trace_exporter.OTLPSpanExporter`
* `opentelemetry.sdk._logs.LoggerProvider`
* `opentelemetry.sdk._logs.LoggingHandler`
* `opentelemetry.sdk._logs.export.BatchLogRecordProcessor`
* `opentelemetry.sdk.resources.Resource`
* `opentelemetry.sdk.trace.TracerProvider`
* `opentelemetry.sdk.trace.export.BatchSpanProcessor`
* `plyer.notification`
* `regression_model_template.io.osvariables.Env`

## Used By

* [kafka_app.py](../../regression_model_template/controller/kafka_app.md)
* [base.py](../../regression_model_template/jobs/base.md)
* [evaluations.py](../../regression_model_template/jobs/evaluations.md)
* [training.py](../../regression_model_template/jobs/training.md)
* [tuning.py](../../regression_model_template/jobs/tuning.md)
