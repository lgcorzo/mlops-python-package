---
iso_doc_type: "Description"
iso_viewpoint: "SequenceView"
type: "architecture"
title: "ISO 42010 Sequence View — Runtime Workflows & Execution Sequences"
description: "Sequence view illustrating training pipelines, model evaluation, registry promotion, and Kafka streaming real-time inference."
tags: ["iso42010", "sequence", "workflow", "training", "kafka"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# ISO 42010 Sequence View: Runtime Workflows & Execution Sequences

## 1. Model Training & Registration Pipeline (`TrainingJob`)

```mermaid
sequenceDiagram
    autonumber
    actor CLI as CLI / User (`scripts.py`)
    participant Job as `TrainingJob` (`jobs/training.py`)
    participant DS as `ParquetReader` (`io/datasets.py`)
    participant MDL as `BaselineSklearnModel` (`core/models.py`)
    participant MLF as `MlflowService` (`io/services.py`)
    participant REG as `CustomSaver` (`io/registries.py`)

    CLI->>Job: execute `run()`
    activate Job
    Job->>MLF: start `run_context(RunConfig)`
    activate MLF
    Job->>DS: `read()` dataset splits
    Job->>MDL: `fit(X_train, y_train)`
    MDL-->>Job: fitted model instance
    Job->>MDL: `predict(X_val)`
    Job->>MLF: log evaluation metrics (`rmse`, `mae`, `r2`)
    Job->>REG: `save(model, signature, example)`
    REG->>MLF: log_model to MLflow Artifact Store
    MLF-->>Job: run finished
    deactivate MLF
    Job-->>CLI: pipeline success
    deactivate Job
```

---

## 2. Kafka Real-Time Streaming & FastAPI Inference (`FastAPIKafkaService`)

```mermaid
sequenceDiagram
    autonumber
    actor Client as Client / Microservice
    participant API as `FastAPIKafkaService` (`controller/kafka_app.py`)
    participant Schema as `PredictionRequest` (`controller/kafka_app.py`)
    participant Model as `PredictionService` (`controller/kafka_app.py`)
    participant Kafka as Apache Kafka Cluster

    Kafka->>API: `_poll_message()` (Input Topic)
    activate API
    API->>Schema: validate JSON payload
    alt Valid Payload
        API->>Model: `predict(input_data)`
        Model-->>API: numpy prediction array
        API->>Kafka: `delivery_report()` Publish to Output Topic
    else Rate Limit / Invalid Schema
        API->>API: `_handle_message_error()`
        API->>Kafka: Publish error envelope
    end
    deactivate API

    Client->>API: GET `/health` or `/metrics`
    API-->>Client: 200 OK (System Health / Prometheus Metrics)
```
