---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Logging, Telemetry & MLflow Services"
source_path: "src/regression_model_template/io/services.py"
description: "Telemetry context services including Loguru logging, Plyer system desktop alerts, and MLflow run context manager."
tags: ["io", "services", "loguru", "plyer", "mlflow", "opentelemetry"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
---

# Module Specification: Logging, Telemetry & MLflow Services

* **Source File Reference:** `src/regression_model_template/io/services.py` (Lines: L1-L252)
* **Upstream Dependencies:** `loguru`, `plyer`, `mlflow`, `opentelemetry`
* **Downstream Consumers:** [[Modules/RegressionModelTemplate/Jobs/Base]], [[Modules/RegressionModelTemplate/Jobs/Training]]

## 1. Architectural Role & Responsibilities
`services.py` provides infrastructure services (`Service` base class). Implements `LoggerService` (Loguru structured logging), `AlertsService` (desktop notifications via Plyer), and `MlflowService` (MLflow tracking client and experiment run context manager).

## 2. UML 2.0 Class Diagram

```mermaid
classDiagram
    direction BT
    class Service {
        <<abstract>>
        +start()*
        +stop()*
    }
    class LoggerService {
        +start()
        +logger() Logger
    }
    class AlertsService {
        +start()
        +notify(title, message)
    }
    class MlflowService {
        +start()
        +run_context(run_config) ContextManager
        +client() MlflowClient
    }

    Service <|-- LoggerService : Inheritance
    Service <|-- AlertsService : Inheritance
    Service <|-- MlflowService : Inheritance
```

## 3. Class & Method Specifications

### `Service` (`src/regression_model_template/io/services.py:L38-L50`)
* `start(self)` (L46-L47): Abstract service initialization.
* `stop(self)` (L49-L50): Abstract service termination.

### `LoggerService` (`src/regression_model_template/io/services.py:L54-L124`)
* `start(self)` (L84-L116): Configures Loguru sinks, formatting, log retention, and OpenTelemetry OTLP log record propagation.

### `MlflowService` (`src/regression_model_template/io/services.py:L162-L252`)
* `run_context(self, run_config: RunConfig)` (L229-L244): Returns python context manager (`with mlflow_service.run_context(...)`) managing active MLflow run lifecycle.
