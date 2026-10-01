---
iso_doc_type: "Description"
iso_viewpoint: "ContextView"
type: "architecture"
title: "Ubiquitous Language & Domain Glossary"
description: "Comprehensive domain definitions and ubiquitous acronyms for the MLOps Python Package."
tags: ["iso42010", "glossary", "ddd", "mlops"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# Ubiquitous Language & Domain Glossary

> **Purpose**: Establish an unambiguous vocabulary across data science, MLOps engineering, platform operations, and compliance auditors.

---

## 📖 Domain Terms & Definitions

### Baseline Model
A reference machine learning model (`BaselineSklearnModel`) providing an empirical baseline for regression tasks. It implements the unified `Model` interface using Scikit-Learn pipelines and Random Forest estimators.

### Champion-Challenger Pattern
A model governance pattern executed by `PromotionJob`. A newly trained and evaluated model (Challenger) is benchmarked against the currently active production model (Champion). Only if performance exceeds predefined thresholds is the Challenger promoted to the production alias.

### DVC (Data Version Control)
An open-source version control system for machine learning projects, managing data pipelines and large dataset pointers in Git without tracking large binary blobs.

### Explanations (XAI)
Feature importance and local sample attributions computed by `ExplanationsJob` using the SHAP (SHapley Additive exPlanations) `TreeExplainer` algorithm, enforcing strict schema compliance on feature rankings.

### Human-in-the-Loop (HITL)
A strict governance constraint requiring human sign-off for critical operational transitions, particularly for merging pull requests into default branches and deploying models to live customer-facing endpoints.

### InferSigner
A cryptographic attestation utility (`utils/signers.py`) calculating a SHA-256 hash across serialized prediction inputs and outputs to ensure data provenance and tamper-evident auditing.

### Job Lifecycle (`base.Job`)
A standardized Python context manager interface (`__enter__`, `__exit__`, `run`) that coordinates service start/stop, alert notifications, and error logging across all operational pipelines.

### Lineage
Metadata linking generated datasets and models back to the originating input data sources, feature engineering steps, commit SHAs, and runtime environment parameters.

### Pandera Schema
A data validation framework enforcing static and runtime tabular constraints on Pandas DataFrames (`InputsSchema`, `TargetsSchema`, `OutputsSchema`), guaranteeing schema safety at service boundaries.

### RateLimiter
A security mechanism embedded in `controller/kafka_app.py` utilizing a sliding window algorithm to throttle excess incoming prediction requests and prevent algorithmic Denial of Service (DoS).

### Splitter
A mathematical strategy abstraction (`utils/splitters.py`) partitioning datasets into train and test subsets while respecting temporal sequence constraints (`TimeSeriesSplitter`) or random stratification (`TrainTestSplitter`).

---

> *Related: [Master Index](index.md) · [Strategic Design](architecture/strategic_design.md)*
