from .config import make_frontmatter

def get_home_md():
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ArchitectureDescription",
        concept_type="guide",
        title="MLOps Python Package — Enterprise Regression Lifecycle",
        description="Master wiki entrypoint and architectural navigation hub for the MLOps Python Package under ISO/IEC/IEEE 42010:2022 standards.",
        tags=["iso42010", "okf", "mlops", "architecture_description", "home"]
    )
    return fm + "\n\n" + """# MLOps Python Package — Enterprise Regression Lifecycle

> **Standards Compliance**: [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74428.html) (Architecture Descriptions) & [ISO/IEC/IEEE 15289:2019](https://www.iso.org/standard/72242.html) (Life Cycle Information Items).  
> **Repository**: `mlops-python-package`  
> **Core Domain**: Production-grade Machine Learning Operations (MLOps) architecture implementing an end-to-end regression model lifecycle from ingestion to streaming serving.

---

## 📌 Master Navigation & Entry Points

- [Master Viewpoint Index](index.md) · [Glossary & Ubiquitous Language](GLOSSARY.md) · [Repository Guide](README.md)

---

## 🏛️ Architecture Viewpoints (ISO 42010)

```mermaid
graph TD
    subgraph Context["Context Layer (ISO 42010 ContextView)"]
        BC["Business Context & Lifecycle"]:::ctx
        SD["Strategic Design & Onion Architecture"]:::ctx
    end

    subgraph Core["Core Domain & Jobs (ComponentView)"]
        TD["Tactical Design & Patterns"]:::comp
        MDM["Data Schemas & Feature Contracts"]:::comp
        JOBS["Lifecycle Jobs (Train/Tune/Eval/Promote)"]:::comp
    end

    subgraph Infrastructure["Infrastructure & Serving (DeploymentView)"]
        INFRA["Adapters (MLflow, Kafka, S3, DVC)"]:::infra
        KAFKA["Kafka Streaming & FastAPI Controller"]:::infra
    end

    BC --> SD
    SD --> TD
    TD --> JOBS
    JOBS --> MDM
    JOBS --> INFRA
    INFRA --> KAFKA

    classDef ctx fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef comp fill:#0f172a,stroke:#818cf8,stroke-width:2px,color:#f8fafc;
    classDef infra fill:#111827,stroke:#34d399,stroke-width:2px,color:#f8fafc;
```

| Section | Focus Area | Key Architectural Deliverables |
| :--- | :--- | :--- |
| [**Business Context**](architecture/business_context.md) | Problem & Value | Business justification, ROI model, KPIs, and MLOps lifecycle stages. |
| [**Strategic Design**](architecture/strategic_design.md) | Macro Architecture | C4 Level 1 & 2 diagrams, Onion Architecture layers, Bounded Contexts. |
| [**Tactical Design**](architecture/tactical_design.md) | Micro Architecture | C4 Level 3 Component diagram, Strategy / Factory / Context Manager patterns. |
| [**Lifecycle Jobs**](architecture/agent_specifications.md) | Autonomous Workflows | Detailed behavioral contracts for Training, Tuning, Evaluations, Explanations, Inference, and Promotion. |
| [**Runtime Sequences**](architecture/runtime_sequences.md) | Execution Traces | End-to-end Mermaid sequence diagrams for batch lifecycle and Kafka streaming. |
| [**Data Model & Contracts**](architecture/mission_data_model.md) | Data Contracts | Pandera DataFrameModels (`Inputs`, `Targets`, `Outputs`, `SHAPValues`), Parquet schema contracts. |
| [**Infrastructure Adapters**](architecture/infrastructure_adapters.md) | External Integrations | MLflow Tracking Server, MinIO/S3, Confluent Kafka, DVC data versioning, Loguru/Alerts. |

---

## 🔒 Security & Governance

| Policy / Report | Description | Key Controls |
| :--- | :--- | :--- |
| [**Security Architecture**](security/security_architecture.md) | Threat Model & Defense | STRIDE analysis, cryptographic model signing (`InferSigner`), rate limiting, DoS defense. |
| [**HITL Governance**](security/hitl_governance.md) | Human-in-the-Loop Gates | Model registry promotion gates, champion-challenger threshold verification, manual sign-off. |
| [**Verification Triad**](security/verification_triad.md) | Quality Gates | 3-Vertex verification: Logical (Pytest), Architectural (Ruff/Mypy), Security (Sanitization). |
| [**Compliance & Audit**](security/compliance_audit.md) | Regulatory Alignment | EU AI Act conformity assessment, reproducibility standards, experiment tracking auditability. |

---

## ⚙️ Operations, Quality & Source Modules

- **Operations**: [User Manual](operations/user_manual.md) · [Production Operations & Deployment](operations/production_operations.md) · [Experiment Tracking Logs](operations/experiment_logs.md)
- **Quality**: [ISO 25010 Test Plan & Quality Report](quality/test_plan_report.md)
- **Codebase Mirror (1:1)**: Inspect all 29 underlying Python modules via the [Master Index Module Catalog](index.md#5-11-structural-codebase-mirror-modules).
"""

def get_readme_md():
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ComponentView",
        concept_type="module",
        title="MLOps Python Package — Documentation Guide",
        description="Repository documentation guide and technical overview for the MLOps Python Package.",
        tags=["iso42010", "okf", "guide", "readme"]
    )
    return fm + "\n\n" + """# MLOps Python Package — Documentation Guide

> **Source Reference**: Anchor at repository root `.`  
> **Layer**: Systems Documentation  
> **Role**: Comprehensive guide to repository layout, developer setup, code metrics, and ISO compliance standards.

---

## 1. Executive Overview

The **MLOps Python Package** (`regression_model_template`) is an enterprise-grade reference architecture for reproducible, scalable, and secure machine learning operations. It decouples domain logic, data contracts, and ML algorithms from I/O mechanisms, external tracking services, and streaming infrastructure.

### Core Technology Stack

| Component | Technology | Rationale |
|:---|:---|:---|
| **Programming Language** | Python 3.10+ | Strict type hinting, standard typing syntax. |
| **Package & Env Manager** | Poetry | Deterministic dependency resolution, virtualenv management. |
| **Data Contract Validation** | Pandera + Pydantic v2 | Strict tabular schema contracts, typing validation. |
| **ML Algorithms & Evaluation**| Scikit-Learn | Extensible model interfaces (`BaselineSklearnModel`, `SklearnMetric`). |
| **Hyperparameter Search** | Optuna | Bayesian hyperparameter optimization and pruning. |
| **Explainability (XAI)** | SHAP (TreeExplainer) | Global and local feature attribution extraction. |
| **Experiment Tracking** | MLflow | Metric, parameter, and model registry lifecycle management. |
| **Streaming & API** | FastAPI + Confluent Kafka | High-throughput streaming inference with sliding-window rate limiting. |
| **Data Versioning** | DVC + Parquet | Immutable dataset versioning and efficient columnar storage. |
| **Task Automation** | Invoke (`tasks/`) | Standardized execution targets for linting, testing, and Docker builds. |

---

## 2. Repository Layout

```text
mlops-python-package/
├── confs/                      # Hierarchical OmegaConf YAML configurations
├── data/                       # DVC-tracked datasets (raw, interim, processed)
├── notebooks/                  # Exploratory data analysis notebooks
├── src/
│   └── regression_model_template/  # Primary Python package
│       ├── controller/         # Streaming API & Kafka endpoints
│       ├── core/               # Mathematical domain: Models, Metrics, Schemas
│       ├── io/                 # Input/Output: Configs, Datasets, Registries, Services
│       ├── jobs/               # Workflow execution: Train, Tune, Eval, Explain, Infer, Promote
│       ├── utils/              # Auxiliary utilities: Searchers, Signers, Splitters
│       ├── init_data.py        # Synthetic data generation utility
│       ├── scripts.py          # Script execution entrypoint
│       └── settings.py         # Application settings
├── tasks/                      # Invoke task runners
├── tests/                      # 29 Pytest unit and integration test suites
└── wiki/                       # ISO-compliant GitHub wiki documentation
```

---

## 3. Codebase Metrics Summary

- **Total Python Modules**: 29
- **Total Unit & Integration Test Suites**: 29
- **Line Coverage Target**: ≥ 95%
- **AST Verified Symbols**: 25+ classes, 60+ methods, 100% typed contracts
- **Broken Relative Links**: 0 (Automated link resolution gate)
"""

def get_sidebar_md():
    return """## 🏠 Navigation

- [Home](Home.md)
- [Master Index](index.md)
- [Glossary](GLOSSARY.md)
- [Documentation Guide](README.md)

## 📊 Architecture (ISO 42010)

- [Business Context](architecture/business_context.md)
- [Strategic Design](architecture/strategic_design.md)
- [Tactical Design](architecture/tactical_design.md)
- [Lifecycle Job Specs](architecture/agent_specifications.md)
- [Runtime Sequences](architecture/runtime_sequences.md)
- [Data Model & Contracts](architecture/mission_data_model.md)
- [Infrastructure Adapters](architecture/infrastructure_adapters.md)

## 🔒 Security & Governance

- [Security Architecture](security/security_architecture.md)
- [HITL Governance](security/hitl_governance.md)
- [Verification Triad](security/verification_triad.md)
- [Compliance & Audit](security/compliance_audit.md)

## 📖 Operations & Quality

- [User Manual](operations/user_manual.md)
- [Production Operations](operations/production_operations.md)
- [Experiment Logs](operations/experiment_logs.md)
- [Test Plan & Report](quality/test_plan_report.md)

## 📦 Source Modules (1:1 Mirror)

### Package Root
- [__init__.md](modules/regression_model_template/__init__.md)
- [__main__.md](modules/regression_model_template/__main__.md)
- [init_data.md](modules/regression_model_template/init_data.md)
- [scripts.md](modules/regression_model_template/scripts.md)
- [settings.md](modules/regression_model_template/settings.md)

### controller
- [controller/__init__.md](modules/regression_model_template/controller/__init__.md)
- [kafka_app.md](modules/regression_model_template/controller/kafka_app.md)

### core (Domain)
- [core/__init__.md](modules/regression_model_template/core/__init__.md)
- [metrics.md](modules/regression_model_template/core/metrics.md)
- [models.md](modules/regression_model_template/core/models.md)
- [schemas.md](modules/regression_model_template/core/schemas.md)

### io (Infrastructure & I/O)
- [io/__init__.md](modules/regression_model_template/io/__init__.md)
- [configs.md](modules/regression_model_template/io/configs.md)
- [datasets.md](modules/regression_model_template/io/datasets.md)
- [osvariables.md](modules/regression_model_template/io/osvariables.md)
- [registries.md](modules/regression_model_template/io/registries.md)
- [services.md](modules/regression_model_template/io/services.md)

### jobs (Lifecycle Stages)
- [jobs/__init__.md](modules/regression_model_template/jobs/__init__.md)
- [base.md](modules/regression_model_template/jobs/base.md)
- [evaluations.md](modules/regression_model_template/jobs/evaluations.md)
- [explanations.md](modules/regression_model_template/jobs/explanations.md)
- [inference.md](modules/regression_model_template/jobs/inference.md)
- [promotion.md](modules/regression_model_template/jobs/promotion.md)
- [training.md](modules/regression_model_template/jobs/training.md)
- [tuning.md](modules/regression_model_template/jobs/tuning.md)

### utils (Utilities)
- [utils/__init__.md](modules/regression_model_template/utils/__init__.md)
- [searchers.md](modules/regression_model_template/utils/searchers.md)
- [signers.md](modules/regression_model_template/utils/signers.md)
- [splitters.md](modules/regression_model_template/utils/splitters.md)
"""

def get_index_md():
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ArchitectureDescription",
        concept_type="architecture",
        title="Master Wiki Index — ISO Architecture Description",
        description="Master index of the MLOps Python Package documentation under ISO/IEC/IEEE 42010:2022 and 15289:2019 standards.",
        tags=["iso42010", "iso15289", "index", "architecture_description"]
    )
    return fm + "\n\n" + """# Master Documentation Index — MLOps Python Package

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
"""

def get_glossary_md():
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ContextView",
        concept_type="architecture",
        title="Ubiquitous Language & Domain Glossary",
        description="Comprehensive domain definitions and ubiquitous acronyms for the MLOps Python Package.",
        tags=["iso42010", "glossary", "ddd", "mlops"]
    )
    return fm + "\n\n" + """# Ubiquitous Language & Domain Glossary

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
"""
