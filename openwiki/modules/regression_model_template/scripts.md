---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: CLI Command Dispatcher"
source_path: "src/regression_model_template/scripts.py"
description: "Command-line argument parser and pipeline job launcher for training, tuning, evaluation, SHAP explanations, and promotion."
tags: ["scripts", "cli", "argparse", "jobs"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
---

# Module Specification: CLI Command Dispatcher

* **Source File Reference:** `src/regression_model_template/scripts.py` (Lines: L1-L55)
* **Upstream Dependencies:** [[Modules/RegressionModelTemplate/Jobs/Training]], [[Modules/RegressionModelTemplate/Jobs/Tuning]], [[Modules/RegressionModelTemplate/Jobs/Evaluations]], [[Modules/RegressionModelTemplate/Jobs/Explanations]], [[Modules/RegressionModelTemplate/Jobs/Promotion]], [[Modules/RegressionModelTemplate/Jobs/Inference]]
* **Downstream Consumers:** Package binary script `regression_model_template`

## 1. Architectural Role & Responsibilities
`scripts.py` parses terminal arguments (`argparse`), initializes Hydra configuration specs, instantiates requested `Job` implementations (`TrainingJob`, `TuningJob`, etc.), and executes pipeline workflows within context managers.

## 2. Public Function Contracts

### `main() -> None`
* **Line Citation:** `src/regression_model_template/scripts.py:L15-L55`
* **Visibility:** Public (`+`)
* **Behavior:** Parses CLI command arguments (`train`, `tune`, `evaluate`, `explain`, `promote`, `infer`), resolves `--config-path` and `--config-name`, and invokes target job.
