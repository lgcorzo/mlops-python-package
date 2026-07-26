---
type: script
title: "kafka_app"
source_path: "src/regression_model_template/controller/kafka_app.py"
description: "FastAPI and Kafka Service for Predictions with Logging."
tags: [script, regression_model_template]
last_verified_commit: "abe2ee0"
---

# kafka_app

Source File: `src/regression_model_template/controller/kafka_app.py`

FastAPI and Kafka Service for Predictions with Logging.

```mermaid
classDiagram
    class FastAPIKafkaService {
        +prediction_callback : Callable
        +kafka_config : dict
        +input_topic : str
        +output_topic : str
        +stop_event : threading.Event
        +producer : confluent_kafka.Producer
        +consumer : confluent_kafka.Consumer
        +start() : None
        +delivery_report(err, msg) : None
        +_initialize_kafka_producer() : None
        +_initialize_kafka_consumer() : None
        +_run_server() : None
        +_consume_messages() : None
        +_poll_message() : Message | None
        +_handle_message_error(msg) : bool
        +_process_message(msg) : None
        +_close_consumer() : None
        +stop() : None
    }

    class PredictionService {
        +model : Any
        +predict(input_data: PredictionRequest) : PredictionResponse
    }

    FastAPIKafkaService --> PredictionService : prediction_callback
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
