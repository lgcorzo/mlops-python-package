---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: Environment Variables Settings"
source_path: "[[src/regression_model_template/io/osvariables.py](../../../../src/regression_model_template/io/osvariables.py)](../../../../[src/regression_model_template/io/osvariables.py](../../../../src/regression_model_template/io/osvariables.py))"
description: "Singleton environment variable loader backed by Pydantic BaseSettings."
tags: ["io", "osvariables", "singleton", "env", "pydantic"]
last_verified_commit: "HEAD"
timestamp: "2026-07-31T16:17:00Z"
generated: "agent:okf-professional-documenter"
verified: "true"
---

# Module Specification: Environment Variables Settings

* **Source File Reference:** `[[src/regression_model_template/io/osvariables.py](../../../../src/regression_model_template/io/osvariables.py)](../../../../[src/regression_model_template/io/osvariables.py](../../../../src/regression_model_template/io/osvariables.py))` (Lines: L1-L26)
* **Upstream Dependencies:** `pydantic_settings`
* **Downstream Consumers:** [Modules/RegressionModelTemplate/Settings](../settings.md), [Modules/RegressionModelTemplate/IO/Services](services.md)

## 1. Architectural Role & Responsibilities
`osvariables.py` defines `Singleton` metaclass and `Env` settings provider. Enforces thread-safe environment variable parsing (`MLFLOW_TRACKING_URI`, `KAFKA_BOOTSTRAP_SERVERS`, `OTEL_EXPORTER_OTLP_ENDPOINT`).

## 2. Class Specifications

### `Singleton` (`[[src/regression_model_template/io/osvariables.py:L6-L13](../../../../src/regression_model_template/io/osvariables.py#L6-L13)](../../../../[src/regression_model_template/io/osvariables.py](../../../../src/regression_model_template/io/osvariables.py)#L6-L13)`)
* `__new__(cls)` (L10-L13): Guarantees single instance instantiation for environment settings.

### `Env` (`[[src/regression_model_template/io/osvariables.py:L16-L26](../../../../src/regression_model_template/io/osvariables.py#L16-L26)](../../../../[src/regression_model_template/io/osvariables.py](../../../../src/regression_model_template/io/osvariables.py)#L16-L26)`)
* Ingests `.env` files or system environment variables into typed fields.
