---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "index"
title: "Index of MLOps Python Package Wiki 🗂️"
source_path: ""
description: "Master index and landing page for MLOps Python Package OpenWiki."
tags: ["index", "navigation", "openwiki"]
timestamp: "2026-08-01T09:57:53Z"
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "8f9670a"
---

# Index of MLOps Python Package Wiki 🗂️

Welcome to the ISO-compliant Open Knowledge Format (OKF) v0.2 OpenWiki for the MLOps Python Package. This index provides progressive disclosure of all architectural, specification, and module documentation.

## 🧭 System-Level Architecture & Guides

- 🌐 [[architecture/iso_42010_overview]] — ISO/IEC/IEEE 42010 Architecture Description & Viewpoint Index.
- 📐 [[architecture/system_context]] — Context View & External System Boundaries (Kafka, MLflow).
- 📦 [[architecture/component_structure]] — Component View & UML 2.0 Structural Relationship.
- 🔄 [[architecture/runtime_sequences]] — Sequence View & Execution Flows (Job context, Predictions).
- ⚙️ [[architecture/deployment_view]] — Deployment View & Runtime Infrastructure.
- 🔐 [[architecture/security_view]] — Security View & Data Protection Rules.
- 📝 [[architecture/adr/adr_001_ast_engine]] — Architectural Decision Record for AST Engine selection.
- 📋 [[specifications/srs_requirements]] — ISO 15289 Specification: Software Requirements.
- 🔌 [[specifications/api_contracts]] — ISO 15289 Specification: HTTP & Kafka Contracts.
- 📊 [[quality/iso_25010_quality]] — ISO 25010 Quality Model Assessment & Metrics.
- 💻 [[user_guides/developer_guide]] — Developer Setup, CLI, and Testing Manual.
- 📜 [[logs]] — Documentation Synthesis History & Git Audit Trail.

## 🧱 1:1 Mirrored Module Specifications

The following list maps the codebase modules 1:1 with their detailed technical specifications.

- [[modules/regression_model_template/__init__]]
- [[modules/regression_model_template/__main__]]
- [[modules/regression_model_template/scripts]]
- [[modules/regression_model_template/settings]]

### 🎮 Controller Package
- [[modules/regression_model_template/controller/__init__]]
- [[modules/regression_model_template/controller/kafka_app]]

### 🧠 Core Package
- [[modules/regression_model_template/core/__init__]]
- [[modules/regression_model_template/core/metrics]]
- [[modules/regression_model_template/core/models]]
- [[modules/regression_model_template/core/schemas]]

### 📥 IO Package
- [[modules/regression_model_template/io/__init__]]
- [[modules/regression_model_template/io/configs]]
- [[modules/regression_model_template/io/datasets]]
- [[modules/regression_model_template/io/osvariables]]
- [[modules/regression_model_template/io/registries]]
- [[modules/regression_model_template/io/services]]

### ⚙️ Jobs Package
- [[modules/regression_model_template/jobs/__init__]]
- [[modules/regression_model_template/jobs/base]]
- [[modules/regression_model_template/jobs/evaluations]]
- [[modules/regression_model_template/jobs/explanations]]
- [[modules/regression_model_template/jobs/inference]]
- [[modules/regression_model_template/jobs/promotion]]
- [[modules/regression_model_template/jobs/training]]
- [[modules/regression_model_template/jobs/tuning]]

### 🛠️ Utilities Package
- [[modules/regression_model_template/utils/__init__]]
- [[modules/regression_model_template/utils/searchers]]
- [[modules/regression_model_template/utils/signers]]
- [[modules/regression_model_template/utils/splitters]]
