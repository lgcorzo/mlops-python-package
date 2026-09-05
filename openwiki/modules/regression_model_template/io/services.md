---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: services"
source_path: "src/regression_model_template/io/services.py"
description: "Manage global context during execution."
tags: ["module", "services"]
timestamp: "2026-09-05T05:14:18Z"
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

## 3. Class & Method Specifications

# Public Classes

### `PropagateHandler`

## Overview

No description available.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Public Methods

### `emit(self: Any, record: logging.LogRecord) -> None`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `record`

  - **type**: logging.LogRecord

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

# Example usage for emit

```

### `Service`

## Overview

Base class for a global service.

Use services to manage global contexts.
e.g., logger object, mlflow client, spark context, ...

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Public Methods

### `start(self: Any) -> None`

### Description

Start the service.

### Inputs

* `self`

  - **type**: Any

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

# Example usage for start

```

### `stop(self: Any) -> None`

### Description

Stop the service.

### Inputs

* `self`

  - **type**: Any

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

# Example usage for stop

```

### `LoggerService`

## Overview

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

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`sink`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`level`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`format`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`colorize`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`serialize`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`backtrace`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`diagnose`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`catch`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `start(self: Any) -> None`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

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

# Example usage for start

```

### `logger(self: Any) -> loguru.Logger`

### Description

Return the main logger.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: loguru.Logger

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for logger

```

### `AlertsService`

## Overview

Service for sending notifications.

Require libnotify-bin on Linux systems.

In production, use with Slack, Discord, or emails.

https://plyer.readthedocs.io/en/latest/api.html#plyer.facades.Notification

Parameters:
    enable (bool): use notifications or print.
    app_name (str): name of the application.
    timeout (int | None): timeout in secs.

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`enable`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`app_name`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`timeout`**

  - **Type**: int | None

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `start(self: Any) -> None`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

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

# Example usage for start

```

### `notify(self: Any, title: str, message: str) -> None`

### Description

Send a notification to the system.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `title`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `message`

  - **type**: str

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

# Example usage for notify

```

### `MlflowService`

## Overview

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

**Why it exists:** Provides specific business logic or state encapsulation.

**What business capability it provides:** Implementation of module responsibilities.

**How it collaborates:** Interacts with other components via standard API boundaries.

## Attributes

* **`env`**

  - **Type**: ClassVar[Env]

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`tracking_uri`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`registry_uri`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`experiment_name`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`registry_name`**

  - **Type**: str

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`autolog_disable`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`autolog_disable_for_unsupported_versions`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`autolog_exclusive`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`autolog_log_input_examples`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`autolog_log_model_signatures`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`autolog_log_models`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`autolog_log_datasets`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

* **`autolog_silent`**

  - **Type**: bool

  - **Purpose**: Attribute for class state.

  - **Constraints**: Standard type constraints.

## Public Methods

### `start(self: Any) -> None`

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

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

# Example usage for start

```

### `run_context(self: Any, run_config: RunConfig) -> T.Generator[(mlflow.ActiveRun, None, None)]`

### Description

Yield an active Mlflow run and exit it afterwards.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `run_config`

  - **type**: RunConfig

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: T.Generator[(mlflow.ActiveRun, None, None)]

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for run_context

```

### `client(self: Any) -> mt.MlflowClient`

### Description

Return a new Mlflow client.

### Inputs

* `self`

  - **type**: Any

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: mt.MlflowClient

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for client

```

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
