---
type: script
title: "services"
source_path: "src/regression_model_template/io/services.py"
description: "Manage global context during execution."
tags: [script, regression_model_template]
last_verified_commit: "c0c5dbc"
---

# services

Source File: `src/regression_model_template/io/services.py`

Manage global context during execution.

```mermaid
classDiagram
    class PropagateHandler {
        +emit(record) : None
    }
    class Service {
        +start() : None
        +stop() : None
    }
    class LoggerService {
        +sink
        +level
        +format
        +colorize
        +serialize
        +backtrace
        +diagnose
        +catch
        +start() : None
        +logger() : Any
    }
    Service <|-- LoggerService
    class AlertsService {
        +enable
        +app_name
        +timeout
        +start() : None
        +notify(title, message) : None
    }
    Service <|-- AlertsService
    class MlflowService {
        +env
        +tracking_uri
        +registry_uri
        +experiment_name
        +registry_name
        +autolog_disable
        +autolog_disable_for_unsupported_versions
        +autolog_exclusive
        +autolog_log_input_examples
        +autolog_log_model_signatures
        +autolog_log_models
        +autolog_log_datasets
        +autolog_silent
        +start() : None
        +run_context(run_config) : Any
        +client() : Any
    }
    Service <|-- MlflowService
    class MlflowService.RunConfig {
        +name
        +description
        +tags
        +log_system_metrics
    }
```

```mermaid
flowchart TD

    services --> __future__
    services --> abc
    services --> contextlib
    services --> logging
    services --> loguru
    services --> mlflow
    services --> opentelemetry
    services --> opentelemetry__logs
    services --> opentelemetry_exporter_otlp_proto_http__log_exporter
    services --> opentelemetry_exporter_otlp_proto_http_trace_exporter
    services --> opentelemetry_sdk__logs
    services --> opentelemetry_sdk__logs_export
    services --> opentelemetry_sdk_resources
    services --> opentelemetry_sdk_trace
    services --> opentelemetry_sdk_trace_export
    services --> plyer
    services --> pydantic
    services --> regression_model_template_io_osvariables
    services --> sys
    services --> typing
```
