---
iso_doc_type: "Description"
iso_viewpoint: "DeploymentView"
type: "architecture"
title: "ISO 42010 Deployment View — Runtime Infrastructure & Containerization"
description: "Deployment view detailing Docker image layers, docker-compose, MLServer, and environment configuration."
tags: ["iso42010", "deployment", "docker", "mlserver", "kafka"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
---

# ISO 42010 Deployment View: Runtime Infrastructure & Containerization

## 1. Deployment Overview & Container Strategy

`mlops-python-package` supports containerized deployment for both batch pipeline training and real-time Kafka/FastAPI streaming endpoints.

```mermaid
graph LR
    subgraph Container Ecosystem
        docker["Dockerfile (Python 3.12-slim)"]
        compose["docker-compose.yml"]
        mlserver["MLServer / MLflow Model Server"]
    end
    
    subgraph Runtime Deployment Targets
        k8s["Kubernetes Pod / Cluster"]
        docker_host["Docker Engine / Local Host"]
        mlflow_serv["MLflow Tracking Host"]
    end

    docker --> compose
    compose --> docker_host
    docker --> k8s
    mlserver --> k8s
```

---

## 2. Docker Configuration (`Dockerfile` & `docker-compose.yml`)

### A. Base Image & Build Layers
* **Base Image:** `python:3.12-slim`
* **Dependency Manager:** `poetry`
* **Build Stages:** Multi-stage build isolating build tools (`gcc`, `curl`) from final minimal runtime image.
* **Environment Variables:** `PYTHONPATH=/app/src`, `POETRY_VIRTUALENVS_CREATE=false`.

### B. Service Topology (`docker-compose.yml`)
* **Kafka Service:** Listens on port `9092` for real-time inference streaming.
* **FastAPI Service:** Exposes `/health`, `/metrics`, and `/predict` on port `8000`.
* **MLflow Tracking Server:** Connected via `MLFLOW_TRACKING_URI`.

---

## 3. Environment Configuration (`src/regression_model_template/io/osvariables.py:L16-L26`)

The service automatically ingests runtime settings from `.env` files or system environment variables:

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `ENV` | `dev` | Environment scope (`dev`, `staging`, `prod`). |
| `MLFLOW_TRACKING_URI` | `http://localhost:5000` | Target MLflow tracking server URI. |
| `KAFKA_BOOTSTRAP_SERVERS` | `localhost:9092` | Kafka broker endpoints. |
| `KAFKA_INPUT_TOPIC` | `regression-inputs` | Kafka topic for raw inference payloads. |
| `KAFKA_OUTPUT_TOPIC` | `regression-outputs` | Kafka topic for prediction results. |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:4317` | OpenTelemetry OTLP gRPC endpoint. |
