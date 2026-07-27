---
type: script
title: "kafka_app"
source_path: "src/regression_model_template/controller/kafka_app.py"
description: "FastAPI and Kafka Service for Predictions with Logging."
tags: [script, regression_model_template]
last_verified_commit: "c0c5dbc"
---

# kafka_app

Source File: `src/regression_model_template/controller/kafka_app.py`

FastAPI and Kafka Service for Predictions with Logging.

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

```mermaid
sequenceDiagram
    participant Client
    participant FastAPI as /predict Endpoint
    participant RateLimiter
    participant ThreadPool
    participant PredictionService
    participant Model

    Client->>FastAPI: POST /predict (PredictionRequest)
    FastAPI->>RateLimiter: is_allowed(client_ip)
    RateLimiter-->>FastAPI: true
    FastAPI->>ThreadPool: run_in_threadpool(prediction_callback, request_data)
    ThreadPool->>PredictionService: predict(input_data)
    PredictionService->>Model: predict(inputs)
    Model-->>PredictionService: Outputs (DataFrame)
    PredictionService-->>ThreadPool: PredictionResponse
    ThreadPool-->>FastAPI: PredictionResponse
    FastAPI-->>Client: PredictionResponse (JSON)
```

```mermaid
flowchart TD
    subgraph Kafka Streaming Flow
        A[Kafka Topic: Input] -->|Poll Message| B(FastAPIKafkaService._consume_messages)
        B --> C{msg.error()?}
        C -- Yes --> D(_handle_message_error)
        C -- No --> E(_process_message)
        E --> F[Parse JSON & Validate PredictionRequest]
        F --> G[prediction_callback: PredictionService.predict]
        G --> H[Kafka Producer: produce]
        H --> I[Kafka Topic: Output]
        H --> J[Commit Offset asynchronously]
    end
```

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