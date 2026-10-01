---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "architecture"
title: "Master Wiki Index — ISO Architecture Description"
description: "Master index of the MLOps Python Package documentation under ISO/IEC/IEEE 42010:2022 and 15289:2019 standards."
tags: ["iso42010", "iso15289", "index", "architecture_description"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# Master Documentation Index — MLOps Python Package

> **Standards Compliance**: [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74428.html) (Architecture Descriptions) & [ISO/IEC/IEEE 15289:2019](https://www.iso.org/standard/72242.html) (Life Cycle Information Items).

---

## 📌 Navigation & Entry Points

- [Home](Home.md) · [Glossary](GLOSSARY.md) · [Documentation Guide](README.md) · [Sidebar](_Sidebar.md)

---

## 1. Stakeholder Perspectives & Concerns Matrix (ISO 42010)

| Stakeholder Persona | Primary Concerns | Framing ISO Viewpoint | Governed Wiki Document |
| :--- | :--- | :--- | :--- |
| **Lead Data Scientist** | Model accuracy, baseline comparison, SHAP feature attributions | ContextView & ComponentView | [Business Context](architecture/business_context.md), [Lifecycle Jobs](architecture/agent_specifications.md) |
| **MLOps Engineer** | CI/CD pipelines, experiment tracking, model registry promotion | ComponentView & SequenceView | [Tactical Design](architecture/tactical_design.md), [Runtime Sequences](architecture/runtime_sequences.md) |
| **Security & Compliance Auditor** | Model integrity, input sanitization, EU AI Act conformity | SecurityView & QualityView | [Security Architecture](security/security_architecture.md), [Compliance Audit](security/compliance_audit.md) |
| **Platform / DevOps Engineer**| Kafka streaming latency, Docker deployment, resource quotas | DeploymentView & Operations | [Infrastructure Adapters](architecture/infrastructure_adapters.md), [Production Operations](operations/production_operations.md) |

---

## 2. Architecture Viewpoints (ISO 42010)

| Viewpoint | Document | Description |
|:---|:---|:---|
| **ContextView** | [Business Context](architecture/business_context.md) | Business justification, ROI model, KPIs, and ML lifecycle stages. |
| **ContextView** | [Strategic Design](architecture/strategic_design.md) | C4 Level 1-2, Onion Architecture, Bounded Contexts. |
| **ComponentView** | [Tactical Design](architecture/tactical_design.md) | C4 Level 3 Component diagram, design patterns (Strategy, Factory, Singleton). |
| **ComponentView** | [Lifecycle Job Specs](architecture/agent_specifications.md) | Specification of all 6 jobs (`base.Job`, Training, Tuning, Eval, Explain, Infer, Promote). |
| **SequenceView** | [Runtime Sequences](architecture/runtime_sequences.md) | 4 comprehensive Mermaid execution sequences for batch and streaming pipelines. |
| **ComponentView** | [Data Model & Contracts](architecture/mission_data_model.md) | Pandera schemas, Parquet lineage, Kafka JSON payload contracts. |
| **ComponentView** | [Infrastructure Adapters](architecture/infrastructure_adapters.md) | MLflow Tracking Server, MinIO/S3, Confluent Kafka, DVC, Logging/Alerts. |

---

## 3. Security & Governance (ISO 42010 SecurityView & Policies)

| Topic | Document | Description |
|:---|:---|:---|
| **SecurityView** | [Security Architecture](security/security_architecture.md) | STRIDE threat model, cryptographic model signing, rate limiting, DoS protection. |
| **Policy** | [HITL Governance](security/hitl_governance.md) | 4-Vertex Human-in-the-Loop governance mesh & promotion threshold verification. |
| **Policy** | [Verification Triad](security/verification_triad.md) | Logical, Architectural, and Security quality gates. |
| **Report** | [Compliance & Audit](security/compliance_audit.md) | EU AI Act conformity assessment, reproducibility standards, experiment auditability. |

---

## 4. Operations, Deployment & Quality (ISO 15289 & 25010)

| Topic | Document | Description |
|:---|:---|:---|
| **Procedure** | [User Manual](operations/user_manual.md) | Step-by-step guides for environment setup, data generation, CLI, and REST endpoints. |
| **DeploymentView** | [Production Operations](operations/production_operations.md) | Docker containerization, Docker Compose multi-service setup, runbook & troubleshooting. |
| **Report** | [Experiment Logs](operations/experiment_logs.md) | MLflow tracking schema, parameters, metrics, and artifact layout. |
| **QualityView** | [Test Plan & Report](quality/test_plan_report.md) | ISO 25010 software quality evaluation, 29 Pytest suites, performance benchmarks. |

---

## 5. 1:1 Structural Codebase Mirror (Modules)

| Subsystem | Source Path | Wiki Specification Page | Key Symbols |
| :--- | :--- | :--- | :--- |
| **Root** | `src/regression_model_template/__init__.py` | [__init__.md](modules/regression_model_template/__init__.md) | Package metadata |
| **Root** | `src/regression_model_template/__main__.py` | [__main__.md](modules/regression_model_template/__main__.md) | CLI dispatcher |
| **Root** | `src/regression_model_template/init_data.py` | [init_data.md](modules/regression_model_template/init_data.md) | `generate_data` |
| **Root** | `src/regression_model_template/scripts.py` | [scripts.md](modules/regression_model_template/scripts.md) | `main` |
| **Root** | `src/regression_model_template/settings.py` | [settings.md](modules/regression_model_template/settings.md) | `Settings`, `MainSettings` |
| **controller** | `src/regression_model_template/controller/__init__.py` | [controller/__init__.md](modules/regression_model_template/controller/__init__.md) | Controller exports |
| **controller** | `src/regression_model_template/controller/kafka_app.py` | [kafka_app.md](modules/regression_model_template/controller/kafka_app.md) | `RateLimiter`, `PredictionRequest`, `FastAPIKafkaService` |
| **core** | `src/regression_model_template/core/__init__.py` | [core/__init__.md](modules/regression_model_template/core/__init__.md) | Core domain exports |
| **core** | `src/regression_model_template/core/metrics.py` | [metrics.md](modules/regression_model_template/core/metrics.md) | `Metric`, `SklearnMetric`, `Threshold` |
| **core** | `src/regression_model_template/core/models.py` | [models.md](modules/regression_model_template/core/models.md) | `Model`, `BaselineSklearnModel` |
| **core** | `src/regression_model_template/core/schemas.py` | [schemas.md](modules/regression_model_template/core/schemas.md) | `InputsSchema`, `TargetsSchema`, `OutputsSchema` |
| **io** | `src/regression_model_template/io/__init__.py` | [io/__init__.md](modules/regression_model_template/io/__init__.md) | I/O layer exports |
| **io** | `src/regression_model_template/io/configs.py` | [configs.md](modules/regression_model_template/io/configs.md) | `parse_file`, `merge_configs` |
| **io** | `src/regression_model_template/io/datasets.py` | [datasets.md](modules/regression_model_template/io/datasets.md) | `Reader`, `ParquetReader`, `Writer`, `ParquetWriter` |
| **io** | `src/regression_model_template/io/osvariables.py` | [osvariables.md](modules/regression_model_template/io/osvariables.md) | `Singleton`, `Env` |
| **io** | `src/regression_model_template/io/registries.py` | [registries.md](modules/regression_model_template/io/registries.md) | `Loader`, `Register`, `MlflowRegister` |
| **io** | `src/regression_model_template/io/services.py` | [services.md](modules/regression_model_template/io/services.md) | `Service`, `LoggerService`, `MlflowService` |
| **jobs** | `src/regression_model_template/jobs/__init__.py` | [jobs/__init__.md](modules/regression_model_template/jobs/__init__.md) | Jobs layer exports |
| **jobs** | `src/regression_model_template/jobs/base.py` | [base.md](modules/regression_model_template/jobs/base.md) | `Job` (Context manager base) |
| **jobs** | `src/regression_model_template/jobs/evaluations.py` | [evaluations.md](modules/regression_model_template/jobs/evaluations.md) | `EvaluationsJob` |
| **jobs** | `src/regression_model_template/jobs/explanations.py` | [explanations.md](modules/regression_model_template/jobs/explanations.md) | `ExplanationsJob` (SHAP) |
| **jobs** | `src/regression_model_template/jobs/inference.py` | [inference.md](modules/regression_model_template/jobs/inference.md) | `InferenceJob` |
| **jobs** | `src/regression_model_template/jobs/promotion.py` | [promotion.md](modules/regression_model_template/jobs/promotion.md) | `PromotionJob` |
| **jobs** | `src/regression_model_template/jobs/training.py` | [training.md](modules/regression_model_template/jobs/training.md) | `TrainingJob` |
| **jobs** | `src/regression_model_template/jobs/tuning.py` | [tuning.md](modules/regression_model_template/jobs/tuning.md) | `TuningJob` |
| **utils** | `src/regression_model_template/utils/__init__.py` | [utils/__init__.md](modules/regression_model_template/utils/__init__.md) | Utilities exports |
| **utils** | `src/regression_model_template/utils/searchers.py` | [searchers.md](modules/regression_model_template/utils/searchers.md) | `Searcher`, `GridCVSearcher` |
| **utils** | `src/regression_model_template/utils/signers.py` | [signers.md](modules/regression_model_template/utils/signers.md) | `Signer`, `InferSigner` |
| **utils** | `src/regression_model_template/utils/splitters.py` | [splitters.md](modules/regression_model_template/utils/splitters.md) | `Splitter`, `TrainTestSplitter`, `TimeSeriesSplitter` |
