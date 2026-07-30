---
type: "module-architecture"
title: "kafka_app"
description: "Technical architecture and class hierarchy for kafka_app"
tags: ["architecture", "uml", "pyreverse", "openwiki"]
timestamp: "2026-07-30T19:10:46Z"
---

# Module Name: kafka_app

* **Source Directory Reference:** `src/regression_model_template/controller/`
* **Package Dependency:** Upstream: `typing`, `json`, `regression_model_template.io.registries`, `threading`, `confluent_kafka.admin`, `pandas`, `confluent_kafka`, `pydantic`, `logging`, `regression_model_template.io`, `uvicorn`, `time`, `fastapi.concurrency`, `fastapi`, `regression_model_template.core.schemas`, `uvicorn.middleware.proxy_headers`, `fastapi.middleware.cors`, `fastapi.middleware.trustedhost`, `collections`, `os` | Downstream: None

## 1. Executive Summary & Purpose
Deterministic architectural model extracted via AST parsing for module `kafka_app`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)
The following class diagram models the object-oriented structure, explicit inheritance hierarchies, and polymorphic interface implementations derived from local AST analysis:

```mermaid
classDiagram
    direction BT
    class RateLimiter {
        +__init__()
        +is_allowed()
    }
    class PredictionRequest {
        +validate_schema()
        +check_input_size()
    }
    BaseModel <|-- PredictionRequest : Inheritance / Specialization
    class PredictionResponse {
    }
    BaseModel <|-- PredictionResponse : Inheritance / Specialization
    class FastAPIKafkaService {
        +__init__()
        +delivery_report()
        +start()
        +_initialize_kafka_producer()
        +_initialize_kafka_consumer()
        +_ensure_topics_exist()
        +_run_server()
        +_consume_messages()
        +_poll_message()
        +_handle_message_error()
        +_process_message()
        +_close_consumer()
        +stop()
    }
    class PredictionService {
        +__init__()
        +predict()
    }
```

## 3. Package & Class Relations

The following diagram defines the package boundaries and directional inter-package dependencies:

```mermaid
classDiagram
    direction LR
    namespace kafka_app {
        class kafka_app_module
    }
    class typing_module
    kafka_app_module --> typing_module : imports
    class json_module
    kafka_app_module --> json_module : imports
    class regression_model_template_io_registries_module
    kafka_app_module --> regression_model_template_io_registries_module : imports
    class threading_module
    kafka_app_module --> threading_module : imports
    class confluent_kafka_admin_module
    kafka_app_module --> confluent_kafka_admin_module : imports
    class pandas_module
    kafka_app_module --> pandas_module : imports
    class confluent_kafka_module
    kafka_app_module --> confluent_kafka_module : imports
    class pydantic_module
    kafka_app_module --> pydantic_module : imports
    class logging_module
    kafka_app_module --> logging_module : imports
    class regression_model_template_io_module
    kafka_app_module --> regression_model_template_io_module : imports
    class uvicorn_module
    kafka_app_module --> uvicorn_module : imports
    class time_module
    kafka_app_module --> time_module : imports
    class fastapi_concurrency_module
    kafka_app_module --> fastapi_concurrency_module : imports
    class fastapi_module
    kafka_app_module --> fastapi_module : imports
    class regression_model_template_core_schemas_module
    kafka_app_module --> regression_model_template_core_schemas_module : imports
    class uvicorn_middleware_proxy_headers_module
    kafka_app_module --> uvicorn_middleware_proxy_headers_module : imports
    class fastapi_middleware_cors_module
    kafka_app_module --> fastapi_middleware_cors_module : imports
    class fastapi_middleware_trustedhost_module
    kafka_app_module --> fastapi_middleware_trustedhost_module : imports
    class collections_module
    kafka_app_module --> collections_module : imports
    class os_module
    kafka_app_module --> os_module : imports
```

* **Inheritance & Polymorphism:** Detailed breakdown of abstract base classes, interfaces, and concrete overrides.
* **Dependencies:** How classes within this package collaborate externally.

## 4. Execution Flow & Runtime Behavior

The following sequence diagram outlines the execution lifecycle and message passing during core operations:

```mermaid
sequenceDiagram
    autonumber
    participant Caller as Client Interface
    participant RateLimiter as RateLimiter
    Caller->>RateLimiter: __init__()
    Note over RateLimiter: Execution of __init__
    RateLimiter->>RateLimiter: internal OrderedDict()
    RateLimiter-->>Caller: Returns status
    participant PredictionRequest as PredictionRequest
    Caller->>PredictionRequest: validate_schema()
    Note over PredictionRequest: Execution of validate_schema
    PredictionRequest->>PredictionRequest: internal DataFrame()
    PredictionRequest->>PredictionRequest: internal validate()
    PredictionRequest-->>Caller: Returns status
    participant PredictionResponse as PredictionResponse
    participant FastAPIKafkaService as FastAPIKafkaService
    Caller->>FastAPIKafkaService: __init__()
    Note over FastAPIKafkaService: Execution of __init__
    FastAPIKafkaService->>FastAPIKafkaService: internal Event()
    FastAPIKafkaService-->>Caller: Returns status
    participant PredictionService as PredictionService
    Caller->>PredictionService: __init__()
    Note over PredictionService: Execution of __init__
    PredictionService-->>Caller: Returns status
```

---

* **Source Citations:**
  - Class `RateLimiter`: `src/regression_model_template/controller/kafka_app.py:82`
  - Method `__init__`: `src/regression_model_template/controller/kafka_app.py:85`
  - Method `is_allowed`: `src/regression_model_template/controller/kafka_app.py:91`
  - Class `PredictionRequest`: `src/regression_model_template/controller/kafka_app.py:138`
  - Method `validate_schema`: `src/regression_model_template/controller/kafka_app.py:143`
  - Method `check_input_size`: `src/regression_model_template/controller/kafka_app.py:149`
  - Class `PredictionResponse`: `src/regression_model_template/controller/kafka_app.py:177`
  - Class `FastAPIKafkaService`: `src/regression_model_template/controller/kafka_app.py:184`
  - Method `__init__`: `src/regression_model_template/controller/kafka_app.py:187`
  - Method `delivery_report`: `src/regression_model_template/controller/kafka_app.py:203`
  - Method `start`: `src/regression_model_template/controller/kafka_app.py:210`
  - Method `_initialize_kafka_producer`: `src/regression_model_template/controller/kafka_app.py:220`
  - Method `_initialize_kafka_consumer`: `src/regression_model_template/controller/kafka_app.py:232`
  - Method `_ensure_topics_exist`: `src/regression_model_template/controller/kafka_app.py:244`
  - Method `_run_server`: `src/regression_model_template/controller/kafka_app.py:264`
  - Method `_consume_messages`: `src/regression_model_template/controller/kafka_app.py:271`
  - Method `_poll_message`: `src/regression_model_template/controller/kafka_app.py:287`
  - Method `_handle_message_error`: `src/regression_model_template/controller/kafka_app.py:295`
  - Method `_process_message`: `src/regression_model_template/controller/kafka_app.py:320`
  - Method `_close_consumer`: `src/regression_model_template/controller/kafka_app.py:374`
  - Method `stop`: `src/regression_model_template/controller/kafka_app.py:380`
  - Class `PredictionService`: `src/regression_model_template/controller/kafka_app.py:442`
  - Method `__init__`: `src/regression_model_template/controller/kafka_app.py:445`
  - Method `predict`: `src/regression_model_template/controller/kafka_app.py:448`
