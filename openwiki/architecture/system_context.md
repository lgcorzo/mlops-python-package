---
iso_doc_type: "Description"
iso_viewpoint: "ContextView"
type: "architecture"
title: "System Context View"
description: "System Context View showing external boundaries, actors, data sources, and integrations (Kafka, MLflow)."
tags: ["iso42010", "context", "boundaries", "kafka", "mlflow"]
timestamp: "2026-08-01T09:57:53Z"
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "8f9670a"
---

# System Context View: mlops-python-package

This viewpoint describes the boundaries of the MLOps Regression Service, outlining actors, external system dependencies, and incoming/outgoing data streams.

## 1. System Context Diagram

```mermaid
graph TD
    subgraph "External Systems"
        MLflow["MLflow Tracking & Registry"]
        Kafka["Kafka Broker (bootstrap.servers)"]
        FS["Local / Cloud Storage (Parquet)"]
    end

    subgraph "mlops-python-package"
        Jobs["Job Execution Engine (Training, Tuning, etc.)"]
        Serving["Serving Service (FastAPI & Kafka App)"]
    end

    Developer["Data Scientist / Developer"] -- "Triggers Jobs via CLI" --> Jobs
    HTTPClient["HTTP Prediction Client"] -- "POST /predict" --> Serving
    KafkaProducer["External Data Streamer"] -- "Publishes to input_topic" --> Kafka

    Jobs -- "Logs experiments & models" --> MLflow
    Jobs -- "Reads / Writes datasets" --> FS
    Serving -- "Loads registered models" --> MLflow
    Serving -- "Consumes input_topic" --> Kafka
    Serving -- "Publishes prediction to output_topic" --> Kafka
    Kafka -- "Delivers predictions" --> HTTPClient
```

## 2. Interface Definitions & Boundaries

### MLflow Integration
- **Role:** Central repository for model tracking and model registration.
- **Protocol:** REST HTTP / gRPC via `mlflow` client.
- **Boundaries:** Configured using the `MLflowService` wrapper (`src/regression_model_template/io/services.py:L130-L195`).

### Kafka Broker
- **Role:** Real-time data streaming message queue.
- **Protocol:** Kafka Protocol via `confluent_kafka` C-extension client.
- **Topics:**
  - `input_topic` (Default): Receives features payload dictionaries.
  - `output_topic` (Default): Emits inference results with predicted output values.

### Storage Interface
- **Role:** Handles batch inputs and outputs.
- **Protocol:** Filesystem I/O via Pandas/PyArrow.
- **Formats:** Parquet dataset readers and writers (`src/regression_model_template/io/datasets.py:L10-L100`).

## 3. Actor Roles & Interactions

- **Data Scientist:** Triggers pipeline jobs (`training`, `tuning`, `evaluations`, `promotion`, `explanations`, `inference`) via CLI entry points.
- **Prediction Client:** Queries predictions in real-time using either HTTP endpoints or asynchronous Kafka message streams.
