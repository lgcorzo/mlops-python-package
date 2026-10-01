---
iso_doc_type: "Description"
iso_viewpoint: "ContextView"
type: "architecture"
title: "Strategic Design & Onion Architecture"
description: "ISO 42010 ContextView / ISO 15289 Description documentation for the system context, C4 levels 1-2, and Onion Architecture layers."
tags: ["iso42010", "okf", "context_view", "c4", "onion_architecture"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# Strategic Design & Onion Architecture

> **Purpose**: Detail the system boundary, high-level context, container interactions, and Onion Architecture layering of the MLOps Python Package.

---

## 1. C4 Level 1: System Context Diagram

```mermaid
C4Context
    title System Context Diagram — MLOps Python Package

    Person(data_scientist, "Data Scientist", "Trains, tunes, and evaluates regression models.")
    Person(operator, "MLOps / Platform Engineer", "Deploys, monitors, and operates streaming services.")
    System(mlops_pkg, "MLOps Python Package", "Executes end-to-end regression workflows, schema verification, and streaming inference.")

    System_Ext(mlflow_srv, "MLflow Tracking Server", "Centralized metric tracking and model artifact registry.")
    System_Ext(kafka_cluster, "Confluent Kafka Cluster", "Distributed event bus for incoming prediction events and results.")
    System_Ext(s3_store, "Object Storage (MinIO / S3)", "Stores raw Parquet data, processed datasets, and model binaries.")

    Rel(data_scientist, mlops_pkg, "Executes CLI jobs via", "Invoke / Python -m")
    Rel(operator, mlops_pkg, "Monitors health & streams via", "HTTP / Prometheus")
    Rel(mlops_pkg, mlflow_srv, "Logs runs & registers models", "REST API")
    Rel(mlops_pkg, kafka_cluster, "Consumes & Publishes events", "Kafka TCP")
    Rel(mlops_pkg, s3_store, "Reads/Writes Parquet files", "S3 / DVC")
```

---

## 2. C4 Level 2: Container Diagram

```mermaid
C4Container
    title Container Diagram — Internal Subsystems

    Container(core, "Core Domain", "Python / Pandera / Scikit-Learn", "Encapsulates mathematical abstractions: Model, Metric, Schemas.")
    Container(jobs, "Lifecycle Jobs", "Python / Pydantic", "Executes BaseJob, TrainingJob, TuningJob, EvaluationsJob, InferenceJob, PromotionJob.")
    Container(io, "IO Adapters", "Python / OmegaConf / Parquet", "Handles Datasets, Configs, Registries, OSVariables, Services.")
    Container(controller, "Streaming Controller", "FastAPI / Confluent Kafka", "Handles REST prediction endpoints and Kafka event consumers.")
    Container(utils, "Utilities", "Python / Optuna / SHA-256", "Provides Searchers, Signers, and Splitters.")

    Rel(jobs, core, "Uses mathematical abstractions", "Python Import")
    Rel(jobs, io, "Reads datasets & logs runs", "Service Context")
    Rel(jobs, utils, "Applies hyperparameter search & splitting", "Helper Call")
    Rel(controller, core, "Validates payloads against schemas", "Pandera Check")
    Rel(controller, io, "Loads models from registry", "Loader Adapter")
```

---

## 3. Onion Architecture Layers

The repository strictly enforces dependency inversion. Inner domain layers remain pure and completely oblivious to outer framework and infrastructure layers:

```mermaid
graph TD
    subgraph L4["Layer 4: Interface & Controllers"]
        CTRL["controller/kafka_app.py
scripts.py
__main__.py"]
    end
    subgraph L3["Layer 3: Infrastructure & Adapters"]
        IO["io/services.py (MLflow, Alerts)
io/registries.py
io/datasets.py
io/configs.py"]
    end
    subgraph L2["Layer 2: Application Lifecycle Jobs"]
        JOBS["jobs/base.py
jobs/training.py
jobs/tuning.py
jobs/evaluations.py
jobs/inference.py
jobs/promotion.py"]
    end
    subgraph L1["Layer 1: Core Domain (Pure Mathematics)"]
        CORE["core/models.py (Model, BaselineSklearnModel)
core/metrics.py (Metric, SklearnMetric)
core/schemas.py (Pandera DataFrameModels)"]
    end

    CTRL --> IO
    CTRL --> JOBS
    IO --> CORE
    JOBS --> CORE
    JOBS --> IO

    classDef l1 fill:#312e81,stroke:#818cf8,stroke-width:2px,color:#f8fafc;
    classDef l2 fill:#1e3a5f,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef l3 fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#f8fafc;
    classDef l4 fill:#701a75,stroke:#f472b6,stroke-width:2px,color:#f8fafc;

    class CORE l1;
    class JOBS l2;
    class IO l3;
    class CTRL l4;
```

1. **Domain Layer (`core/`)**: Completely independent of database, framework, or network details. Defines abstract mathematical contracts for predictive estimators (`Model`), loss/scoring functions (`Metric`), and tabular structures (`Schema`).
2. **Application Layer (`jobs/`)**: Implements operational use cases. Each job subclasses `Job` (`jobs/base.py`), managing the setup, execution, and teardown lifecycle of distinct workflows.
3. **Infrastructure Layer (`io/`)**: Implements technology-specific adapters for external platforms, including MLflow tracking, OmegaConf YAML parsing, and Parquet file I/O.
4. **Interface Layer (`controller/`)**: Exposes streaming endpoints via Kafka and synchronous REST endpoints via FastAPI.

---

> *Related: [Tactical Design](tactical_design.md) · [Runtime Sequences](runtime_sequences.md) · [Master Index](../index.md)*
