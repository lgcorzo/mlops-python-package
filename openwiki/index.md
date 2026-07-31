---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "hub"
title: "OpenWiki Master Knowledge Hub — MLOps Python Package"
description: "Master index and navigation hub for the mlops-python-package repository, complying with ISO/IEC/IEEE 42010, 15289, 25010, and 26514 standards."
tags: ["index", "navigation", "iso42010", "iso15289", "mlops", "okf"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# OpenWiki Master Knowledge Hub: `mlops-python-package`

Welcome to the **ISO/IEC/IEEE Standard OpenWiki Documentation Hub** for `mlops-python-package` (`regression_model_template` v2.0.1).

This software engineering wiki is deterministically synthesized using local AST analysis (`graphify`, Python `ast` introspection) and strictly adheres to international standards for software architecture description, lifecycle documentation, quality evaluation, and user guides.

---

## 🏛️ 1. ISO/IEC/IEEE 42010 Architecture Views

The architectural design of the system is described across distinct stakeholder viewpoints:

* 🌐 **[Architecture/SystemContext](architecture/system_context.md)** — *Context View*: System boundaries, external MLflow, DVC, Kafka, and OpenTelemetry integration interfaces.
* 📦 **[Architecture/ComponentStructure](architecture/component_structure.md)** — *Component View*: Subsystem breakdown, class hierarchies, and UML 2.0 class diagrams.
* 🔄 **[Architecture/RuntimeSequences](architecture/runtime_sequences.md)** — *Sequence View*: Message dispatches, job execution pipelines, and Kafka real-time streaming interaction flows.
* 🖥️ **[Architecture/DeploymentView](architecture/deployment_view.md)** — *Deployment View*: Docker containerization, `docker-compose` setups, and MLServer deployment targets.
* 🔐 **[Architecture/SecurityView](architecture/security_view.md)** — *Security View*: Authentication, environment key protection, model signature verification, and data sanitization boundaries.
* 📝 **[[Architecture/ADR/ADR_001_AST_Engine]]** — *Architecture Decision Record*: Rationale for local AST extraction over external embedding databases.

---

## 📋 2. ISO/IEC/IEEE 15289 Specifications & Reports

* 📜 **[Specifications/SRSRequirements](specifications/srs_requirements.md)** — Software Requirements Specification (SRS) detailing functional and non-functional requirements.
* 🔌 **[Specifications/APIContracts](specifications/api_contracts.md)** — Complete API Specification, CLI scripts, parameters, and method signatures.
* 📝 **[Logs](logs.md)** — Incremental audit log and AST verification history.

---

## 🏆 3. ISO/IEC 25010 Software Quality Assessment

* 📊 **[[Quality/ISO25010Quality]]** — Comprehensive quality evaluation matrix covering Functional Suitability, Performance Efficiency, Maintainability, Security, and Portability.

---

## 📘 4. ISO/IEC/IEEE 26514 User & Developer Guides

* 🛠️ **[UserGuides/DeveloperGuide](user_guides/developer_guide.md)** — Developer onboarding, environment setup (Poetry/Pyproject), CLI execution, Kafka streaming, and testing procedures.

---

## 🧱 5. Granular Open Knowledge Format (OKF) Module Wiki Pages

The codebase is mirrored 1:1 into granular OKF wiki specifications under `openwiki/modules/`:

### Root Package (`[[src/regression_model_template](../src/regression_model_template)](../[src/regression_model_template](../src/regression_model_template))/`)
* [Modules/RegressionModelTemplate/Init](modules/regression_model_template/__init__.md) — Package initialization & version metadata (`[[src/regression_model_template/__init__.py:L1-L3](../src/regression_model_template/__init__.py#L1-L3)](../[src/regression_model_template/__init__.py](../src/regression_model_template/__init__.py)#L1-L3)`)
* [Modules/RegressionModelTemplate/Main](modules/regression_model_template/__main__.md) — Package CLI entry point (`[[src/regression_model_template/__main__.py:L1-L7](../src/regression_model_template/__main__.py#L1-L7)](../[src/regression_model_template/__main__.py](../src/regression_model_template/__main__.py)#L1-L7)`)
* [Modules/RegressionModelTemplate/Scripts](modules/regression_model_template/scripts.md) — CLI commands dispatcher (`[[src/regression_model_template/scripts.py:L1-L55](../src/regression_model_template/scripts.py#L1-L55)](../[src/regression_model_template/scripts.py](../src/regression_model_template/scripts.py)#L1-L55)`)
* [Modules/RegressionModelTemplate/Settings](modules/regression_model_template/settings.md) — Configuration settings provider (`[[src/regression_model_template/settings.py:L1-L25](../src/regression_model_template/settings.py#L1-L25)](../[src/regression_model_template/settings.py](../src/regression_model_template/settings.py)#L1-L25)`)

### Controller Layer (`[[src/regression_model_template/controller](../src/regression_model_template/controller)](../[src/regression_model_template/controller](../src/regression_model_template/controller))/`)
* [Modules/RegressionModelTemplate/Controller/KafkaApp](modules/regression_model_template/controller/kafka_app.md) — Real-time Kafka event streaming & FastAPI server (`[[src/regression_model_template/controller/kafka_app.py:L1-L462](../src/regression_model_template/controller/kafka_app.py#L1-L462)](../[src/regression_model_template/controller/kafka_app.py](../src/regression_model_template/controller/kafka_app.py)#L1-L462)`)

### Core Subsystem (`[[src/regression_model_template/core](../src/regression_model_template/core)](../[src/regression_model_template/core](../src/regression_model_template/core))/`)
* [Modules/RegressionModelTemplate/Core/Metrics](modules/regression_model_template/core/metrics.md) — Regression evaluation metrics & MLflow scorers (`[[src/regression_model_template/core/metrics.py:L1-L148](../src/regression_model_template/core/metrics.py#L1-L148)](../[src/regression_model_template/core/metrics.py](../src/regression_model_template/core/metrics.py)#L1-L148)`)
* [Modules/RegressionModelTemplate/Core/Models](modules/regression_model_template/core/models.md) — Abstract model wrapper & Scikit-Learn baseline (`[[src/regression_model_template/core/models.py:L1-L220](../src/regression_model_template/core/models.py#L1-L220)](../[src/regression_model_template/core/models.py](../src/regression_model_template/core/models.py)#L1-L220)`)
* [Modules/RegressionModelTemplate/Core/Schemas](modules/regression_model_template/core/schemas.md) — Pandera & Pydantic input/output schemas (`[[src/regression_model_template/core/schemas.py:L1-L117](../src/regression_model_template/core/schemas.py#L1-L117)](../[src/regression_model_template/core/schemas.py](../src/regression_model_template/core/schemas.py)#L1-L117)`)

### I/O & Infrastructure Layer (`[[src/regression_model_template/io](../src/regression_model_template/io)](../[src/regression_model_template/io](../src/regression_model_template/io))/`)
* [Modules/RegressionModelTemplate/IO/Configs](modules/regression_model_template/io/configs.md) — Hydra/Omegaconf YAML configuration loaders (`[[src/regression_model_template/io/configs.py:L1-L45](../src/regression_model_template/io/configs.py#L1-L45)](../[src/regression_model_template/io/configs.py](../src/regression_model_template/io/configs.py)#L1-L45)`)
* [Modules/RegressionModelTemplate/IO/Datasets](modules/regression_model_template/io/datasets.md) — Parquet data readers, writers & lineage loggers (`[[src/regression_model_template/io/datasets.py:L1-L125](../src/regression_model_template/io/datasets.py#L1-L125)](../[src/regression_model_template/io/datasets.py](../src/regression_model_template/io/datasets.py)#L1-L125)`)
* [[Modules/RegressionModelTemplate/IO/OSVariables]] — Pydantic environment variable settings (`[[src/regression_model_template/io/osvariables.py:L1-L26](../src/regression_model_template/io/osvariables.py#L1-L26)](../[src/regression_model_template/io/osvariables.py](../src/regression_model_template/io/osvariables.py)#L1-L26)`)
* [Modules/RegressionModelTemplate/IO/Registries](modules/regression_model_template/io/registries.md) — MLflow Model Registry savers, loaders & adapters (`[[src/regression_model_template/io/registries.py:L1-L317](../src/regression_model_template/io/registries.py#L1-L317)](../[src/regression_model_template/io/registries.py](../src/regression_model_template/io/registries.py)#L1-L317)`)
* [Modules/RegressionModelTemplate/IO/Services](modules/regression_model_template/io/services.md) — Telemetry, Loguru, Plyer alerts & MLflow service wrappers (`[[src/regression_model_template/io/services.py:L1-L252](../src/regression_model_template/io/services.py#L1-L252)](../[src/regression_model_template/io/services.py](../src/regression_model_template/io/services.py)#L1-L252)`)

### Pipeline Jobs Subsystem (`[[src/regression_model_template/jobs](../src/regression_model_template/jobs)](../[src/regression_model_template/jobs](../src/regression_model_template/jobs))/`)
* [Modules/RegressionModelTemplate/Jobs/Base](modules/regression_model_template/jobs/base.md) — Context-managed base pipeline job (`[[src/regression_model_template/jobs/base.py:L1-L85](../src/regression_model_template/jobs/base.py#L1-L85)](../[src/regression_model_template/jobs/base.py](../src/regression_model_template/jobs/base.py)#L1-L85)`)
* [Modules/RegressionModelTemplate/Jobs/Training](modules/regression_model_template/jobs/training.md) — Model training pipeline job (`[[src/regression_model_template/jobs/training.py:L1-L145](../src/regression_model_template/jobs/training.py#L1-L145)](../[src/regression_model_template/jobs/training.py](../src/regression_model_template/jobs/training.py)#L1-L145)`)
* [Modules/RegressionModelTemplate/Jobs/Tuning](modules/regression_model_template/jobs/tuning.md) — Hyperparameter tuning pipeline job (`[[src/regression_model_template/jobs/tuning.py:L1-L104](../src/regression_model_template/jobs/tuning.py#L1-L104)](../[src/regression_model_template/jobs/tuning.py](../src/regression_model_template/jobs/tuning.py)#L1-L104)`)
* [Modules/RegressionModelTemplate/Jobs/Evaluations](modules/regression_model_template/jobs/evaluations.md) — Model evaluation & validation job (`[[src/regression_model_template/jobs/evaluations.py:L1-L125](../src/regression_model_template/jobs/evaluations.py#L1-L125)](../[src/regression_model_template/jobs/evaluations.py](../src/regression_model_template/jobs/evaluations.py)#L1-L125)`)
* [Modules/RegressionModelTemplate/Jobs/Explanations](modules/regression_model_template/jobs/explanations.md) — SHAP model explanation job (`[[src/regression_model_template/jobs/explanations.py:L1-L78](../src/regression_model_template/jobs/explanations.py#L1-L78)](../[src/regression_model_template/jobs/explanations.py](../src/regression_model_template/jobs/explanations.py)#L1-L78)`)
* [Modules/RegressionModelTemplate/Jobs/Promotion](modules/regression_model_template/jobs/promotion.md) — MLflow Model Registry promotion job (`[[src/regression_model_template/jobs/promotion.py:L1-L57](../src/regression_model_template/jobs/promotion.py#L1-L57)](../[src/regression_model_template/jobs/promotion.py](../src/regression_model_template/jobs/promotion.py)#L1-L57)`)
* [Modules/RegressionModelTemplate/Jobs/Inference](modules/regression_model_template/jobs/inference.md) — Batch & online prediction job (`[[src/regression_model_template/jobs/inference.py:L1-L66](../src/regression_model_template/jobs/inference.py#L1-L66)](../[src/regression_model_template/jobs/inference.py](../src/regression_model_template/jobs/inference.py)#L1-L66)`)

### Utilities (`[[src/regression_model_template/utils](../src/regression_model_template/utils)](../[src/regression_model_template/utils](../src/regression_model_template/utils))/`)
* [Modules/RegressionModelTemplate/Utils/Searchers](modules/regression_model_template/utils/searchers.md) — Hyperparameter search helpers (`[[src/regression_model_template/utils/searchers.py:L1-L113](../src/regression_model_template/utils/searchers.py#L1-L113)](../[src/regression_model_template/utils/searchers.py](../src/regression_model_template/utils/searchers.py)#L1-L113)`)
* [Modules/RegressionModelTemplate/Utils/Signers](modules/regression_model_template/utils/signers.md) — MLflow model signature inferrers (`[[src/regression_model_template/utils/signers.py:L1-L51](../src/regression_model_template/utils/signers.py#L1-L51)](../[src/regression_model_template/utils/signers.py](../src/regression_model_template/utils/signers.py)#L1-L51)`)
* [Modules/RegressionModelTemplate/Utils/Splitters](modules/regression_model_template/utils/splitters.md) — Dataset train/test & time-series splitters (`[[src/regression_model_template/utils/splitters.py:L1-L108](../src/regression_model_template/utils/splitters.py#L1-L108)](../[src/regression_model_template/utils/splitters.py](../src/regression_model_template/utils/splitters.py)#L1-L108)`)
