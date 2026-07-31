---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Configuration Loaders"
source_path: "src/regression_model_template/io/configs.py"
description: "Hydra and Omegaconf YAML configuration loaders and resolvers."
tags: ["io", "configs", "hydra", "omegaconf", "yaml"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
---

# Module Specification: Configuration Loaders

* **Source File Reference:** `src/regression_model_template/io/configs.py` (Lines: L1-L45)
* **Upstream Dependencies:** `omegaconf`, `hydra`
* **Downstream Consumers:** [[Modules/RegressionModelTemplate/Scripts]], [[Modules/RegressionModelTemplate/Jobs/Base]]

## 1. Architectural Role & Responsibilities
`configs.py` handles parsing, merging, and resolving YAML configuration files via Hydra/OmegaConf. Configures experiment parameters, model hyperparameters, dataset paths, and MLflow logging settings.
