---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::controller::kafka_app — Streaming & REST Prediction Service"
source_path: "src/regression_model_template/controller/kafka_app.py"
description: "FastAPI application and Confluent Kafka consumer service implementing rate limiting, schema validation, and low-latency inference."
tags: ["iso42010", "okf", "component_view", "kafka", "fastapi", "rate_limiting"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::controller::kafka_app — Streaming & REST Prediction Service

> **Source**: `src/regression_model_template/controller/kafka_app.py` (Lines: L1-L501)  
> **Layer**: Interface / Streaming  
> **Role**: Dual-protocol inference server hosting synchronous FastAPI endpoints and asynchronous Confluent Kafka event consumption.

---

## 1. Class Diagram

```mermaid
classDiagram
    class RateLimiter {
        -int max_requests
        -int window_seconds
        -int max_tracked_ips
        -dict ip_requests
        +is_allowed(ip: str) bool
    }

    class PredictionRequest {
        +Dict~str, Any~ input_data
        +validate_schema() DataFrame
        +check_input_size(v: Dict) Dict$
    }

    class PredictionResponse {
        +Dict~str, Any~ result
    }

    class FastAPIKafkaService {
        -Callable prediction_callback
        -Dict kafka_config
        -str input_topic
        -str output_topic
        +start() None
        +stop() None
        -_consume_messages() None
        -_process_message(msg: Message) None
    }

    class PredictionService {
        -Any model
        +predict(input_data: PredictionRequest) PredictionResponse
    }

    FastAPIKafkaService --> RateLimiter : validates client limits
    FastAPIKafkaService --> PredictionService : invokes model
    PredictionService --> PredictionRequest : validates payload
```

---

## 2. Comprehensive Method Contracts

### `RateLimiter.is_allowed(self, ip: str) -> bool`
- **Source Citation**: `src/regression_model_template/controller/kafka_app.py:L91-L112`
- **Visibility**: Public (`+`)
- **Behavior**: Evaluates request count within sliding window for incoming IP address; raises or evicts old entries when bounds exceed `MAX_TRACKED_IPS`.

### `FastAPIKafkaService._process_message(self, msg: Message) -> None`
- **Source Citation**: `src/regression_model_template/controller/kafka_app.py:L320-L372`
- **Visibility**: Private (`-`)
- **Behavior**: Parses JSON event from Kafka input topic, validates against `PredictionRequest`, calculates predictions, and produces response to output topic.

---

> *Related: [Security Architecture](../../../security/security_architecture.md) · [Production Operations](../../../operations/production_operations.md)*
