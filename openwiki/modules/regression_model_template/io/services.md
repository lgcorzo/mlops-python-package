---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: services"
source_path: "src/regression_model_template/io/services.py"
description: "Manage global context during execution."
tags: ["module", "services"]
timestamp: "2026-09-06T06:26:18Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: services

* **Source Reference:** [src/regression_model_template/io/services.py](../../../../src/regression_model_template/io/services.py)

# Module Overview

## Purpose

Manage global context during execution.

## Responsibilities

Manage global context during execution.

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

# Each File Documentation

## Imported modules

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

## Exported classes

* `PropagateHandler`

* `Service`

* `LoggerService`

* `AlertsService`

* `MlflowService`

## Exported interfaces

_Dependent on implementation_

## Public API

_Dependent on implementation_

## Internal architecture

_Dependent on implementation_

## Execution flow

_Dependent on implementation_

## Sequence explanation

_Dependent on implementation_

### Detected Architecture Patterns

Detected roles: Service

## 2. UML Diagrams

### Class Diagram

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

### Sequence Diagram

```plantuml
sequenceDiagram
    PropagateHandler.emit->>handle: invoke
    PropagateHandler.emit->>getLogger: invoke
    LoggerService.start->>create: invoke
    LoggerService.start->>TracerProvider: invoke
    LoggerService.start->>set_tracer_provider: invoke
    LoggerService.start->>OTLPSpanExporter: invoke
    LoggerService.start->>add_span_processor: invoke
    LoggerService.start->>LoggerProvider: invoke
    LoggerService.start->>set_logger_provider: invoke
    LoggerService.start->>OTLPLogExporter: invoke
    LoggerService.start->>add_log_record_processor: invoke
    LoggerService.start->>LoggingHandler: invoke
    LoggerService.start->>addHandler: invoke
    LoggerService.start->>basicConfig: invoke
    LoggerService.start->>getLogger: invoke
    LoggerService.start->>info: invoke
    LoggerService.start->>remove: invoke
    LoggerService.start->>model_dump: invoke
    LoggerService.start->>get: invoke
    LoggerService.start->>add: invoke
    LoggerService.start->>BatchSpanProcessor: invoke
    LoggerService.start->>BatchLogRecordProcessor: invoke
    LoggerService.start->>PropagateHandler: invoke
    AlertsService.notify->>notify: invoke
    AlertsService.notify->>print: invoke
    MlflowService.start->>set_tracking_uri: invoke
    MlflowService.start->>set_registry_uri: invoke
    MlflowService.start->>set_experiment: invoke
    MlflowService.start->>autolog: invoke
    MlflowService.run_context->>start_run: invoke
    MlflowService.client->>MlflowClient: invoke
```

### Component Diagram

```plantuml
component [services] as Comp
Comp --> [annotations]
Comp --> [abc]
Comp --> [contextlib]
Comp --> [logging]
Comp --> [sys]
Comp --> [typing]
Comp --> [ClassVar]
Comp --> [loguru]
Comp --> [mlflow]
Comp --> [tracking]
Comp --> [pydantic]
Comp --> [trace]
Comp --> [set_logger_provider]
Comp --> [OTLPLogExporter]
Comp --> [OTLPSpanExporter]
Comp --> [LoggerProvider]
Comp --> [LoggingHandler]
Comp --> [BatchLogRecordProcessor]
Comp --> [Resource]
Comp --> [TracerProvider]
Comp --> [BatchSpanProcessor]
Comp --> [notification]
Comp --> [Env]
```

## Examples

_Dependent on implementation_

## 3. Class & Method Specifications

# Public Classes

### `PropagateHandler`

## Overview

No description available.

## Public Methods

* **`emit(self: Any, record: logging.LogRecord) -> None`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `record`

  - **type**: logging.LogRecord

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

### `Service`

## Overview

Base class for a global service.

Use services to manage global contexts.
e.g., logger object, mlflow client, spark context, ...

## Public Methods

* **`start(self: Any) -> None`**

### Description

Start the service.

### Inputs

* `self`

  - **type**: Any

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

* **`stop(self: Any) -> None`**

### Description

Stop the service.

### Inputs

* `self`

  - **type**: Any

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

### `LoggerService`

## Overview

Service for logging messages.

https://loguru.readthedocs.io/en/stable/api/logger.html

## Attributes

* **`sink`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`level`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`format`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`colorize`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`serialize`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`backtrace`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`diagnose`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`catch`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`start(self: Any) -> None`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

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

* **`logger(self: Any) -> loguru.Logger`**

### Description

Return the main logger.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: loguru.Logger

* **semantic meaning**: loguru.Logger: the main logger.

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

### `AlertsService`

## Overview

Service for sending notifications.

Require libnotify-bin on Linux systems.

In production, use with Slack, Discord, or emails.

https://plyer.readthedocs.io/en/latest/api.html#plyer.facades.Notification

## Attributes

* **`enable`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`app_name`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`timeout`**

  - **Type**: int | None

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`start(self: Any) -> None`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

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

* **`notify(self: Any, title: str, message: str) -> None`**

### Description

Send a notification to the system.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `title`

  - **type**: str

  - **meaning**: title of the notification.

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `message`

  - **type**: str

  - **meaning**: message of the notification.

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

### `MlflowService`

## Overview

Service for Mlflow tracking and registry.

## Attributes

* **`env`**

  - **Type**: ClassVar[Env]

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`tracking_uri`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`registry_uri`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`experiment_name`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`registry_name`**

  - **Type**: str

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`autolog_disable`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`autolog_disable_for_unsupported_versions`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`autolog_exclusive`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`autolog_log_input_examples`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`autolog_log_model_signatures`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`autolog_log_models`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`autolog_log_datasets`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

* **`autolog_silent`**

  - **Type**: bool

  - **Purpose**: _Dependent on implementation_

  - **Constraints**: _Dependent on implementation_

## Public Methods

* **`start(self: Any) -> None`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

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

* **`run_context(self: Any, run_config: RunConfig) -> T.Generator[(mlflow.ActiveRun, None, None)]`**

### Description

Yield an active Mlflow run and exit it afterwards.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `run_config`

  - **type**: RunConfig

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: T.Generator[(mlflow.ActiveRun, None, None)]

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

* **`client(self: Any) -> mt.MlflowClient`**

### Description

Return a new Mlflow client.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: mt.MlflowClient

* **semantic meaning**: MlflowClient: the mlflow client.

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

* [kafka_app.py](../../regression_model_template/controller/kafka_app.md)

* [base.py](../../regression_model_template/jobs/base.md)

* [evaluations.py](../../regression_model_template/jobs/evaluations.md)

* [training.py](../../regression_model_template/jobs/training.md)

* [tuning.py](../../regression_model_template/jobs/tuning.md)

* [conftest.py](../../tests/conftest.md)

* [test_registries.py](../../tests/io/test_registries.md)

* [test_services.py](../../tests/io/test_services.md)

* [test_base.py](../../tests/jobs/test_base.md)

* [test_evaluations.py](../../tests/jobs/test_evaluations.md)

* [test_explanations.py](../../tests/jobs/test_explanations.md)

* [test_inference.py](../../tests/jobs/test_inference.md)

* [test_promotion.py](../../tests/jobs/test_promotion.md)

* [test_training.py](../../tests/jobs/test_training.md)

* [test_tuning.py](../../tests/jobs/test_tuning.md)
