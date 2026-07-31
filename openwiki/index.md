---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "hub"
title: "OpenWiki Master Knowledge Hub — MLOps Python Package"
description: "Master index and navigation hub for the mlops-python-package repository, complying with ISO/IEC/IEEE 42010, 15289, 25010, and 26514 standards."
tags: ["index", "navigation", "iso42010", "iso15289", "mlops", "okf"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
---

# OpenWiki Master Knowledge Hub: `mlops-python-package`

Welcome to the **ISO/IEC/IEEE Standard OpenWiki Documentation Hub** for `mlops-python-package` (`regression_model_template` v2.0.1).

This software engineering wiki is deterministically synthesized using local AST analysis (`graphify`, Python `ast` introspection) and strictly adheres to international standards for software architecture description, lifecycle documentation, quality evaluation, and user guides.

---

## 🏛️ 1. ISO/IEC/IEEE 42010 Architecture Views

The architectural design of the system is described across distinct stakeholder viewpoints:

* 🌐 **[[Architecture/SystemContext]]** — *Context View*: System boundaries, external MLflow, DVC, Kafka, and OpenTelemetry integration interfaces.
* 📦 **[[Architecture/ComponentStructure]]** — *Component View*: Subsystem breakdown, class hierarchies, and UML 2.0 class diagrams.
* 🔄 **[[Architecture/RuntimeSequences]]** — *Sequence View*: Message dispatches, job execution pipelines, and Kafka real-time streaming interaction flows.
* 🖥️ **[[Architecture/DeploymentView]]** — *Deployment View*: Docker containerization, `docker-compose` setups, and MLServer deployment targets.
* 🔐 **[[Architecture/SecurityView]]** — *Security View*: Authentication, environment key protection, model signature verification, and data sanitization boundaries.
* 📝 **[[Architecture/ADR/ADR_001_AST_Engine]]** — *Architecture Decision Record*: Rationale for local AST extraction over external embedding databases.

---

## 📋 2. ISO/IEC/IEEE 15289 Specifications & Reports

* 📜 **[[Specifications/SRSRequirements]]** — Software Requirements Specification (SRS) detailing functional and non-functional requirements.
* 🔌 **[[Specifications/APIContracts]]** — Complete API Specification, CLI scripts, parameters, and method signatures.
* 📝 **[[Logs]]** — Incremental audit log and AST verification history.

---

## 🏆 3. ISO/IEC 25010 Software Quality Assessment

* 📊 **[[Quality/ISO25010Quality]]** — Comprehensive quality evaluation matrix covering Functional Suitability, Performance Efficiency, Maintainability, Security, and Portability.

---

## 📘 4. ISO/IEC/IEEE 26514 User & Developer Guides

* 🛠️ **[[UserGuides/DeveloperGuide]]** — Developer onboarding, environment setup (Poetry/Pyproject), CLI execution, Kafka streaming, and testing procedures.

---

## 🧱 5. Granular Open Knowledge Format (OKF) Module Wiki Pages

The codebase is mirrored 1:1 into granular OKF wiki specifications under `openwiki/modules/`:

### Root Package (`src/regression_model_template/`)
* [[Modules/RegressionModelTemplate/Init]] — Package initialization & version metadata (`src/regression_model_template/__init__.py:L1-L3`)
* [[Modules/RegressionModelTemplate/Main]] — Package CLI entry point (`src/regression_model_template/__main__.py:L1-L7`)
* [[Modules/RegressionModelTemplate/Scripts]] — CLI commands dispatcher (`src/regression_model_template/scripts.py:L1-L55`)
* [[Modules/RegressionModelTemplate/Settings]] — Configuration settings provider (`src/regression_model_template/settings.py:L1-L25`)

### Controller Layer (`src/regression_model_template/controller/`)
* [[Modules/RegressionModelTemplate/Controller/KafkaApp]] — Real-time Kafka event streaming & FastAPI server (`src/regression_model_template/controller/kafka_app.py:L1-L462`)

### Core Subsystem (`src/regression_model_template/core/`)
* [[Modules/RegressionModelTemplate/Core/Metrics]] — Regression evaluation metrics & MLflow scorers (`src/regression_model_template/core/metrics.py:L1-L148`)
* [[Modules/RegressionModelTemplate/Core/Models]] — Abstract model wrapper & Scikit-Learn baseline (`src/regression_model_template/core/models.py:L1-L220`)
* [[Modules/RegressionModelTemplate/Core/Schemas]] — Pandera & Pydantic input/output schemas (`src/regression_model_template/core/schemas.py:L1-L117`)

### I/O & Infrastructure Layer (`src/regression_model_template/io/`)
* [[Modules/RegressionModelTemplate/IO/Configs]] — Hydra/Omegaconf YAML configuration loaders (`src/regression_model_template/io/configs.py:L1-L45`)
* [[Modules/RegressionModelTemplate/IO/Datasets]] — Parquet data readers, writers & lineage loggers (`src/regression_model_template/io/datasets.py:L1-L125`)
* [[Modules/RegressionModelTemplate/IO/OSVariables]] — Pydantic environment variable settings (`src/regression_model_template/io/osvariables.py:L1-L26`)
* [[Modules/RegressionModelTemplate/IO/Registries]] — MLflow Model Registry savers, loaders & adapters (`src/regression_model_template/io/registries.py:L1-L317`)
* [[Modules/RegressionModelTemplate/IO/Services]] — Telemetry, Loguru, Plyer alerts & MLflow service wrappers (`src/regression_model_template/io/services.py:L1-L252`)

### Pipeline Jobs Subsystem (`src/regression_model_template/jobs/`)
* [[Modules/RegressionModelTemplate/Jobs/Base]] — Context-managed base pipeline job (`src/regression_model_template/jobs/base.py:L1-L85`)
* [[Modules/RegressionModelTemplate/Jobs/Training]] — Model training pipeline job (`src/regression_model_template/jobs/training.py:L1-L145`)
* [[Modules/RegressionModelTemplate/Jobs/Tuning]] — Hyperparameter tuning pipeline job (`src/regression_model_template/jobs/tuning.py:L1-L104`)
* [[Modules/RegressionModelTemplate/Jobs/Evaluations]] — Model evaluation & validation job (`src/regression_model_template/jobs/evaluations.py:L1-L125`)
* [[Modules/RegressionModelTemplate/Jobs/Explanations]] — SHAP model explanation job (`src/regression_model_template/jobs/explanations.py:L1-L78`)
* [[Modules/RegressionModelTemplate/Jobs/Promotion]] — MLflow Model Registry promotion job (`src/regression_model_template/jobs/promotion.py:L1-L57`)
* [[Modules/RegressionModelTemplate/Jobs/Inference]] — Batch & online prediction job (`src/regression_model_template/jobs/inference.py:L1-L66`)

### Utilities (`src/regression_model_template/utils/`)
* [[Modules/RegressionModelTemplate/Utils/Searchers]] — Hyperparameter search helpers (`src/regression_model_template/utils/searchers.py:L1-L113`)
* [[Modules/RegressionModelTemplate/Utils/Signers]] — MLflow model signature inferrers (`src/regression_model_template/utils/signers.py:L1-L51`)
* [[Modules/RegressionModelTemplate/Utils/Splitters]] — Dataset train/test & time-series splitters (`src/regression_model_template/utils/splitters.py:L1-L108`)
