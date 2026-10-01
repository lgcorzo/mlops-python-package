from .config import make_frontmatter

def get_user_manual_md():
    fm = make_frontmatter(
        doc_type="Procedure",
        viewpoint="DeploymentView",
        concept_type="operations",
        title="User & Developer Operational Manual",
        description="ISO 42010 DeploymentView / ISO 15289 Procedure documentation providing step-by-step developer setup and pipeline execution procedures.",
        tags=["iso42010", "okf", "procedure", "user_manual", "cli"]
    )
    return fm + "\n\n" + """# User & Developer Operational Manual

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
curl -X POST http://localhost:8000/predict \\
  -H "Content-Type: application/json" \\
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
"""

def get_production_operations_md():
    fm = make_frontmatter(
        doc_type="Procedure",
        viewpoint="DeploymentView",
        concept_type="operations",
        title="Production Operations & Deployment Runbook",
        description="ISO 42010 DeploymentView / ISO 15289 Procedure documentation covering container deployment, Docker Compose topology, and troubleshooting.",
        tags=["iso42010", "okf", "deployment_view", "docker", "runbook"]
    )
    return fm + "\n\n" + """# Production Operations & Deployment Runbook

> **Purpose**: Production runbook covering container architecture, Docker Compose orchestration, health monitoring, and incident mitigation procedures.

---

## 1. Production Topology & Multi-Service Compose

```mermaid
graph TD
    subgraph Host["Production Node / Kubernetes Pod"]
        APP["mlops-api-container\n(FastAPI + Kafka Consumer)\nPort: 8000"]
        MLF["mlflow-tracking-server\nPort: 5000"]
        KAFKA["confluent-kafka\nPort: 9092"]
        ZK["zookeeper\nPort: 2181"]
    end

    ZK --> KAFKA
    KAFKA --> APP
    MLF --> APP

    CLIENT["External Clients / Consumers"] -->|HTTP / TCP| APP

    classDef srv fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    class APP,MLF,KAFKA,ZK srv;
```

### Launching Multi-Service Stack
```bash
# Launch Kafka, Zookeeper, and MLflow
docker-compose up -d

# Verify container health
docker-compose ps
```

---

## 2. Standard Operating Procedures (Runbook)

### Procedure 1: Restarting Streaming Consumer
If Kafka partition rebalancing hangs or consumer lag accumulates:
```bash
docker-compose restart app
```

### Procedure 2: Inspecting Consumer Lag
```bash
docker exec -it kafka kafka-consumer-groups \\
  --bootstrap-server localhost:9092 \\
  --describe --group mlops-prediction-group
```

### Procedure 3: Diagnostic Health Verification
```bash
# Check service status
curl -i http://localhost:8000/health

# Inspect real-time container logs
docker logs --tail 100 -f mlops-api
```

---

## 3. Incident Mitigation Matrix

| Symptom | Root Cause | Remediation Procedure |
|:---|:---|:---|
| **HTTP 429 Too Many Requests** | Client exceeding 100 req/60s quota | Inspect client source IP; adjust rate limit window in `confs/app.yaml`. |
| **Kafka Commit Failed Error** | Message processing exceeded timeout | Increase `max.poll.interval.ms` or scale batch prediction workers. |
| **Schema Validation Error** | Input payload missing columns | Review incoming JSON against `InputsSchema`; inspect DLQ topic. |
| **MLflow Connection Refused** | Tracking server down or unreachable | Verify MLflow container status; test network route to `MLFLOW_TRACKING_URI`. |

---

> *Related: [User Manual](user_manual.md) · [Security Architecture](../security/security_architecture.md) · [Master Index](../index.md)*
"""

def get_experiment_logs_md():
    fm = make_frontmatter(
        doc_type="Report",
        viewpoint="DeploymentView",
        concept_type="operations",
        title="Experiment Tracking & Telemetry Logs",
        description="ISO 42010 DeploymentView / ISO 15289 Report documentation detailing the MLflow experiment taxonomy, metric schemas, and artifact layout.",
        tags=["iso42010", "okf", "report", "experiment_logs", "mlflow"]
    )
    return fm + "\n\n" + """# Experiment Tracking & Telemetry Logs

> **Purpose**: Detail the telemetry schema, parameter tracking conventions, and artifact storage hierarchies maintained inside MLflow.

---

## 1. Experiment Schema & Naming Conventions

All runs are organized hierarchically under defined MLflow experiments:

```text
mlruns/
└── <experiment_id>/
    └── <run_id>/
        ├── params/               # Model hyperparameters & split settings
        │   ├── max_depth
        │   ├── n_estimators
        │   └── test_size
        ├── metrics/              # Time-series & scalar evaluation results
        │   ├── train_mse
        │   ├── test_mse
        │   ├── test_rmse
        │   └── test_r2
        ├── artifacts/            # Serialized models and attestation files
        │   ├── model/            # MLmodel binary bundle
        │   ├── explanations/     # SHAP summary plots & feature rankings
        │   └── signatures/       # SHA-256 InferSigner receipts
        └── meta.yaml             # Git commit SHA, author, and timestamp
```

---

## 2. Standard Metric Logging Schema

| Metric Key | Mathematical Definition | Evaluation Target | Logged In Job |
|:---|:---|:---|:---|
| `mse` | Mean Squared Error | Minimization | `TrainingJob`, `EvaluationsJob` |
| `rmse` | Root Mean Squared Error | Minimization | `TrainingJob`, `EvaluationsJob` |
| `mae` | Mean Absolute Error | Minimization | `TrainingJob`, `EvaluationsJob` |
| `r2` | Coefficient of Determination | Maximization ($\to 1.0$) | `TrainingJob`, `EvaluationsJob` |
| `trial_score` | Validation score per trial | Optimization objective | `TuningJob` |

---

> *Related: [Production Operations](production_operations.md) · [Tactical Design](../architecture/tactical_design.md) · [Master Index](../index.md)*
"""
