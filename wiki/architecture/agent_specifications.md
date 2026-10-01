---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "architecture"
title: "Lifecycle Job Specifications & Contracts"
description: "ISO 42010 ComponentView / ISO 15289 Specification documentation detailing the functional contracts of all 6 MLOps lifecycle jobs."
tags: ["iso42010", "okf", "component_view", "specification", "jobs"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# Lifecycle Job Specifications & Contracts

> **Purpose**: Formal specification of the inputs, outputs, execution logic, and error behaviors for all 6 operational jobs in `jobs/`.

---

## 1. Unified Job Matrix

| Job Name | Module Source | Primary Responsibility | Key Inputs | Primary Outputs |
| :--- | :--- | :--- | :--- | :--- |
| **`TrainingJob`** | `jobs/training.py` | Model training & artifact logging | Raw Parquet datasets, model config | Trained model, MLflow run, metrics |
| **`TuningJob`** | `jobs/tuning.py` | Hyperparameter optimization | Search space grid, metric objective | Best parameters, trial metrics |
| **`EvaluationsJob`** | `jobs/evaluations.py` | Validation against threshold gates | Test inputs, targets, model alias | Evaluation report, threshold pass/fail |
| **`ExplanationsJob`** | `jobs/explanations.py` | SHAP interpretability extraction | Sample inputs, registered model | Global importance & sample SHAP values |
| **`InferenceJob`** | `jobs/inference.py` | Batch prediction & cryptographic signing | Unlabeled inputs, model version | Output predictions, SHA-256 signature |
| **`PromotionJob`** | `jobs/promotion.py` | Champion-challenger alias promotion | Candidate model version, target alias | Updated MLflow model alias tag |

---

## 2. Detailed Job Contracts

### `TrainingJob` (`jobs/training.py`)
- **Inputs**: `inputs` (`ParquetReader`), `targets` (`ParquetReader`), `model` (`ModelKind`), `run_config` (`RunConfig`).
- **Execution Flow**:
  1. Reads `inputs` and `targets` DataFrames and validates against Pandera schemas.
  2. Partitions data using the configured `Splitter`.
  3. Fits the underlying `Model` on train splits.
  4. Computes train and test evaluation metrics.
  5. Logs parameters, metrics, and serialized model artifact to active MLflow run.
- **Exceptions**: `pandera.errors.SchemaError`, `FileNotFoundError`.

### `TuningJob` (`jobs/tuning.py`)
- **Inputs**: `inputs`, `targets`, `model`, `searcher` (`OptunaSearcher` / `GridCVSearcher`), `metric`.
- **Execution Flow**:
  1. Orchestrates cross-validated hyperparameter trials over parameter grids.
  2. Evaluates scoring metrics on validation folds.
  3. Records trial histories and identifies optimal hyperparameter set.
  4. Logs best parameters and trials dataframe to MLflow.

### `EvaluationsJob` (`jobs/evaluations.py`)
- **Inputs**: `inputs`, `targets`, `model_type`, `run_config`.
- **Execution Flow**:
  1. Ingests evaluation test splits.
  2. Generates predictions using designated model artifact.
  3. Evaluates all configured metrics (`RegressionMetricsEnum`).
  4. Compares results against predefined `Threshold` constraints.

### `ExplanationsJob` (`jobs/explanations.py`)
- **Inputs**: `inputs_samples`, `models_explanations`, `samples_explanations`, `alias_or_version`.
- **Execution Flow**:
  1. Instantiates `shap.TreeExplainer` over model tree estimators.
  2. Calculates global mean absolute SHAP feature importances.
  3. Computes local SHAP attribution values per input sample.
  4. Writes outputs to Parquet datasets matching `SHAPValuesSchema` and `FeatureImportancesSchema`.

### `InferenceJob` (`jobs/inference.py`)
- **Inputs**: `inputs` (`ReaderKind`), `outputs` (`WriterKind`), `loader` (`LoaderKind`), `alias_or_version`.
- **Execution Flow**:
  1. Loads model artifact via `Loader` adapter.
  2. Validates incoming tabular input against `InputsSchema`.
  3. Generates prediction outputs matching `OutputsSchema`.
  4. Signs input-output bundle using `InferSigner` and writes result to destination storage.

### `PromotionJob` (`jobs/promotion.py`)
- **Inputs**: `alias` (`str`), `version` (`int | None`).
- **Execution Flow**:
  1. Queries MLflow Model Registry for the specified registered model.
  2. Validates that candidate model passed all evaluation criteria.
  3. Re-assigns designated model alias (e.g. `champion`) to target version.

---

> *Related: [Runtime Sequences](runtime_sequences.md) · [Tactical Design](tactical_design.md) · [Master Index](../index.md)*
