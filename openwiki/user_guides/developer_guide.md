---
iso_doc_type: "Procedure"
iso_viewpoint: "DeploymentView"
type: "user_guide"
title: "ISO 26514 Developer & User Guide"
description: "Comprehensive developer onboarding guide for environment setup, executing pipeline jobs, running Kafka streaming controllers, and testing."
tags: ["iso26514", "user_guide", "developer", "onboarding"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
---

# ISO 26514 Developer & User Guide

## 1. Environment Setup & Dependency Installation

### Prerequisites
* Python 3.12+
* Poetry (`pip install poetry`)
* Docker & Docker Compose (optional for containerized setup)

### Step-by-Step Installation

1. **Clone & Navigate to Repository:**
   ```bash
   git clone https://github.com/lgcorzo/mlops-python-package.git
   cd mlops-python-package
   ```

2. **Install Dependencies via Poetry:**
   ```bash
   poetry install --with dev,docs,notebooks,checks
   ```

3. **Verify Environment Setup:**
   ```bash
   poetry run python check_env.py
   ```

---

## 2. Executing Pipeline Jobs

Pipeline jobs can be executed using `poetry run` or via standard CLI entry points:

### Model Training Pipeline
```bash
poetry run regression_model_template train --config-path confs --config-name config.yaml
```

### Hyperparameter Tuning
```bash
poetry run regression_model_template tune --config-path confs --config-name config.yaml
```

### Model Evaluation
```bash
poetry run regression_model_template evaluate --config-path confs --config-name config.yaml
```

### SHAP Feature Explanation
```bash
poetry run regression_model_template explain --config-path confs --config-name config.yaml
```

### Model Registry Promotion
```bash
poetry run regression_model_template promote --config-path confs --config-name config.yaml
```

---

## 3. Running Real-Time Kafka & FastAPI Service

### Start Background Services via Docker Compose:
```bash
docker-compose up -d
```

### Run Kafka FastAPI Controller Locally:
```bash
poetry run python -m regression_model_template.controller.kafka_app
```

### Check API Endpoint Status:
```bash
curl http://localhost:8000/health
```

---

## 4. Running Test Suite & Quality Checks

### Run Pytest Unit Tests:
```bash
poetry run pytest
```

### Run Code Formatters & Linters:
```bash
poetry run ruff check .
poetry run mypy src
```
