---
type: "module-architecture"
title: "kafka_app"
description: "Technical architecture and class hierarchy for kafka_app"
tags: ["architecture", "uml", "pyreverse", "openwiki"]
timestamp: "2026-07-30T19:10:46Z"
---

# Module Name: kafka_app

Source File: `src/regression_model_template/controller/kafka_app.py`
* **Source Directory Reference:** `src/regression_model_template/controller/`
* **Package Dependency:** Upstream: `typing`, `json`, `regression_model_template.io.registries`, `threading`, `confluent_kafka.admin`, `pandas`, `confluent_kafka`, `pydantic`, `logging`, `regression_model_template.io`, `uvicorn`, `time`, `fastapi.concurrency`, `fastapi`, `regression_model_template.core.schemas`, `uvicorn.middleware.proxy_headers`, `fastapi.middleware.cors`, `fastapi.middleware.trustedhost`, `collections`, `os` | Downstream: None

## 1. Executive Summary & Purpose
Deterministic architectural model extracted via AST parsing for module `kafka_app`.

## 2. UML 2.0 Class & Inheritance Architecture (Deterministic)
The following class diagram models the object-oriented structure, explicit inheritance hierarchies, and polymorphic interface implementations derived from local AST analysis:

```mermaid
classDiagram
    class RateLimiter {
        -__init__(max_requests, window_seconds, max_tracked_ips)
        +is_allowed(ip) : bool
    }
    class PredictionRequest {
        +input_data
        +validate_schema() : Any
        +check_input_size(cls, v) : Dict
    }
    BaseModel <|-- PredictionRequest
    class PredictionResponse {
        +result
    }
    BaseModel <|-- PredictionResponse
    class FastAPIKafkaService {
        -__init__(prediction_callback, kafka_config, input_topic, output_topic)
        +delivery_report(err, msg) : None
        +start() : None
        #_initialize_kafka_producer() : None
        #_initialize_kafka_consumer() : None
        #_ensure_topics_exist() : None
        #_run_server() : None
        #_consume_messages() : None
        #_poll_message() : Any
        #_handle_message_error(msg) : bool
        #_process_message(msg) : None
        #_close_consumer() : None
        +stop() : None
    }
    class PredictionService {
        -__init__(model)
        +predict(input_data) : PredictionResponse
    }
```

## 3. Package & Class Relations

The following diagram defines the package boundaries and directional inter-package dependencies:

```mermaid
classDiagram
    class RateLimiter {
        -__init__(max_requests, window_seconds, max_tracked_ips)
        +is_allowed(ip) : bool
    }
    class PredictionRequest {
        +input_data
        +validate_schema() : Any
        +check_input_size(cls, v) : Dict
    }
    BaseModel <|-- PredictionRequest
    class PredictionResponse {
        +result
    }
    BaseModel <|-- PredictionResponse
    class FastAPIKafkaService {
        -__init__(prediction_callback, kafka_config, input_topic, output_topic)
        +delivery_report(err, msg) : None
        +start() : None
        #_initialize_kafka_producer() : None
        #_initialize_kafka_consumer() : None
        #_ensure_topics_exist() : None
        #_run_server() : None
        #_consume_messages() : None
        #_poll_message() : Any
        #_handle_message_error(msg) : bool
        #_process_message(msg) : None
        #_close_consumer() : None
        +stop() : None
    }
    class PredictionService {
        -__init__(model)
        +predict(input_data) : PredictionResponse
    }
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

```mermaid
flowchart TD
    kafka_app --> collections
    kafka_app --> confluent_kafka
    kafka_app --> confluent_kafka_admin
    kafka_app --> fastapi
    kafka_app --> fastapi_concurrency
    kafka_app --> fastapi_middleware_cors
    kafka_app --> fastapi_middleware_trustedhost
    kafka_app --> json
    kafka_app --> logging
    kafka_app --> os
    kafka_app --> pandas
    kafka_app --> pydantic
    kafka_app --> regression_model_template_core_schemas
    kafka_app --> regression_model_template_io
    kafka_app --> regression_model_template_io_registries
    kafka_app --> threading
    kafka_app --> time
    kafka_app --> typing
    kafka_app --> uvicorn
    kafka_app --> uvicorn_middleware_proxy_headers
```
