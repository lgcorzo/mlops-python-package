---
iso_doc_type: "Procedure"
iso_viewpoint: "DeploymentView"
type: "operations"
title: "User & Developer Operational Manual"
description: "ISO 42010 DeploymentView / ISO 15289 Procedure documentation providing step-by-step developer setup and pipeline execution procedures."
tags: ["iso42010", "okf", "procedure", "user_manual", "cli"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# User & Developer Operational Manual

> **Purpose**: Practical operational runbook and step-by-step developer manual for local development, data initialization, job execution, and API invocation.

---

## 1. Local Environment Setup

### Prerequisites
- Python 3.10+
- Poetry (recommended) or pip
- Docker & Docker Compose (for streaming and MLflow services)

```bash
# Clone the repository
git clone https://github.com/lgcorzo/mlops-python-package.git
cd mlops-python-package

# Install dependencies via Poetry
poetry install

# Activate virtual environment
poetry shell
```

---

## 2. Generating Synthetic Training Data

To initialize the raw data environment:

```bash
# Executes data generation script
python -m regression_model_template.init_data
```

This generates synthetic bike sharing regression samples conforming to `InputsSchema` and `TargetsSchema` under `data/`.

---

## 3. Running Operational Lifecycle Jobs

Lifecycle jobs can be executed via the package entrypoint or `invoke` task automation:

```bash
# Execute Model Training
python -m regression_model_template --config-name training

# Execute Hyperparameter Tuning (Optuna)
python -m regression_model_template --config-name tuning

# Execute Model Evaluation
python -m regression_model_template --config-name evaluation

# Execute SHAP Feature Explainability
python -m regression_model_template --config-name explanation

# Execute Batch Inference
python -m regression_model_template --config-name inference

# Execute Model Promotion to Champion Alias
python -m regression_model_template --config-name promotion
```

Alternatively, Invoke tasks provide consolidated commands:

```bash
invoke checks.lint      # Runs Ruff linting and formatting checks
invoke checks.types     # Runs Mypy static type verification
invoke checks.tests     # Runs all 29 Pytest suites with coverage
```

---

## 4. Starting the Streaming & API Service

Start the FastAPI and Kafka prediction service:

```bash
# Start Kafka consumer and FastAPI HTTP server
python -m regression_model_template.controller.kafka_app
```

### Health Check Endpoint
```bash
curl http://localhost:8000/health
# Response: {"status": "healthy"}
```

### Synchronous Prediction Request
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "input_data": {
      "instant": [1],
      "dteday": ["2011-01-01 00:00:00"],
      "season": [1],
      "yr": [0],
      "mnth": [1],
      "hr": [0],
      "holiday": [0],
      "weekday": [6],
      "workingday": [0],
      "weathersit": [1],
      "temp": [0.24],
      "atemp": [0.2879],
      "hum": [0.81],
      "windspeed": [0.0]
    }
  }'
```

---

> *Related: [Production Operations](production_operations.md) · [Experiment Logs](experiment_logs.md) · [Master Index](../index.md)*
