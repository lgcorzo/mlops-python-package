---
iso_doc_type: "Description"
iso_viewpoint: "ComponentView"
type: "architecture"
title: "Infrastructure Adapters & Platform Integrations"
description: "ISO 42010 ComponentView / ISO 15289 Description documentation detailing external platform adapters in io/ and controller/."
tags: ["iso42010", "okf", "component_view", "infrastructure", "adapters"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# Infrastructure Adapters & Platform Integrations

> **Purpose**: Document external connectivity adapters, storage systems, message brokers, and telemetry backends.

---

## 1. External Infrastructure Topology

```mermaid
graph LR
    subgraph CoreApp["MLOps Python Package"]
        IO_SRV["io/services.py"]
        IO_REG["io/registries.py"]
        IO_DATA["io/datasets.py"]
        CTRL["controller/kafka_app.py"]
    end

    subgraph ExternalServices["External Infrastructure Platforms"]
        MLFLOW[("MLflow Tracking & Registry")]
        KAFKA{"Confluent Kafka Broker"}
        S3[("MinIO / S3 Object Store")]
        DVC["Data Version Control (DVC)"]
        NOTIF["Notification Gateway (Alerts)"]
    end

    IO_SRV -->|Tracking URI & REST API| MLFLOW
    IO_REG -->|Model Registry API| MLFLOW
    IO_DATA -->|Parquet Read/Write| S3
    IO_DATA -->|Pointers & Metadata| DVC
    CTRL -->|TCP 9092 & Consumer Groups| KAFKA
    IO_SRV -->|Desktop / Webhook Alerts| NOTIF

    classDef core fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef ext fill:#111827,stroke:#34d399,stroke-width:2px,color:#f8fafc;
    class IO_SRV,IO_REG,IO_DATA,CTRL core;
    class MLFLOW,KAFKA,S3,DVC,NOTIF ext;
```

---

## 2. Infrastructure Adapters Breakdown

### 1. MLflow Tracking & Registry (`io/services.py`, `io/registries.py`)
- **Protocol**: HTTP/REST and Python MLflow Client (`mlflow.tracking.MlflowClient`).
- **Configuration**: Injected via `osvariables.py` (`MLFLOW_TRACKING_URI`, `MLFLOW_REGISTRY_URI`).
- **Features**: Experiment isolation, metric logging (`MSE`, `RMSE`, `R2`), artifact versioning, and champion-challenger alias assignment.

### 2. Parquet Storage & DVC Integration (`io/datasets.py`)
- **Format**: Apache Parquet columnar binary with snappy compression.
- **Implementations**:
  - `ParquetReader`: Enforces optional row limits and extracts dataset lineage metadata.
  - `ParquetWriter`: Atomically writes DataFrames to persistent storage.
- **DVC Sync**: Datasets in `data/` are tracked using `.dvc` sidecar files committed to Git.

### 3. Kafka Streaming Broker (`controller/kafka_app.py`)
- **Client**: `confluent-kafka` (C-optimized `librdkafka` bindings).
- **Topology**: Input topic for incoming JSON requests; output topic for prediction responses.
- **Resilience**: Consumer poll loop with automatic partition assignment, graceful shutdown handlers, and error recovery.

### 4. Logging & Alerting Services (`io/services.py`)
- **`LoggerService`**: Configures Loguru sinks with structured serialization and level filtering.
- **`AlertsService`**: Dispatches system notifications upon pipeline failures.

---

> *Related: [Tactical Design](tactical_design.md) · [Production Operations](../operations/production_operations.md) · [Master Index](../index.md)*
