---
iso_doc_type: "Report"
iso_viewpoint: "DeploymentView"
type: "operations"
title: "Experiment Tracking & Telemetry Logs"
description: "ISO 42010 DeploymentView / ISO 15289 Report documentation detailing the MLflow experiment taxonomy, metric schemas, and artifact layout."
tags: ["iso42010", "okf", "report", "experiment_logs", "mlflow"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# Experiment Tracking & Telemetry Logs

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
| `r2` | Coefficient of Determination | Maximization ($	o 1.0$) | `TrainingJob`, `EvaluationsJob` |
| `trial_score` | Validation score per trial | Optimization objective | `TuningJob` |

---

> *Related: [Production Operations](production_operations.md) · [Tactical Design](../architecture/tactical_design.md) · [Master Index](../index.md)*
