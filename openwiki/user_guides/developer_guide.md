---
iso_doc_type: "Procedure"
iso_viewpoint: "ContextView"
type: "procedure"
title: "Developer Onboarding & Guide"
description: "Developer onboarding guide detailing local environment setup, testing procedures, CLI executions, and serving configurations."
tags: ["iso26514", "procedure", "onboarding", "setup", "testing"]
timestamp: "2026-08-01T09:57:53Z"
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "8f9670a"
---

# Developer Onboarding & Guide: mlops-python-package

This guide describes how to set up the local development environment, run test suites, execute CLI workflows, and run the real-time prediction service.

## 1. Local Environment Setup

The project uses **Poetry** for dependency management.

### Prerequisites
- Python 3.12+
- Poetry installed globally (`pipx install poetry` or similar)
- Docker (optional, for running local Kafka / MLflow brokers)

### Installation Steps
1. Clone the repository and navigate to its root:
   ```bash
   git clone <repo_url>
   cd mlops-python-package
   ```
2. Install dependencies and create the virtual environment:
   ```bash
   poetry install
   ```
3. Activate the poetry shell environment:
   ```bash
   poetry shell
   ```

---

## 2. Running the Test Suite

We use `pytest` with coverage report generation.

### Run all tests
```bash
poetry run pytest
```

### Run specific test files
```bash
poetry run pytest tests/jobs/test_inference.py -v
```

### Run coverage analysis
```bash
poetry run pytest --cov=src --cov-report=term-missing
```

---

## 3. CLI Workflow Execution

Jobs (Training, Tuning, Inference, etc.) are executed using YAML/JSON configuration files.

### CLI Syntax
```bash
poetry run python -m regression_model_template <config_file_path> [--extras <config_string>]
```

### Examples

#### 1. Print the Config JSON Schema
You can inspect the expected structure of the configuration file by running:
```bash
poetry run python -m regression_model_template --schema
```

#### 2. Trigger a Training Job
Create a `config.yaml` specifying the job type and its paths:
```yaml
job:
  KIND: "TrainingJob"
  inputs:
    KIND: "ParquetReader"
    path: "data/inputs.parquet"
  targets:
    KIND: "ParquetReader"
    path: "data/targets.parquet"
  model:
    KIND: "BaselineSklearnModel"
```
Then execute:
```bash
poetry run python -m regression_model_template config.yaml
```

---

## 4. Launching the Serving Service

To launch the FastAPI HTTP server and Confluent Kafka consumers concurrently:

```bash
poetry run python -m regression_model_template.controller.kafka_app
```

The server binds to `127.0.0.1:8100` by default. You can test the endpoints using curl:
```bash
curl -X POST http://127.0.0.1:8100/predict \
     -H "Content-Type: application/json" \
     -d '{"input_data": {"season": [1], "yr": [0], "mnth": [1], "hr": [12], "holiday": [false], "weekday": [6], "workingday": [true], "weathersit": [1], "temp": [0.5], "atemp": [0.5], "hum": [0.5], "windspeed": [0.2], "casual": [10], "registered": [100]}}'
```
