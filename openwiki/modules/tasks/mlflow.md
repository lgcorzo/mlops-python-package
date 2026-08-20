---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: mlflow"
source_path: "tasks/mlflow.py"
description: "Mlflow tasks for pyinvoke."
tags: ["module", "mlflow"]
timestamp: "2026-08-20T05:56:47Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "32cdac7"
---
# Module Specification: mlflow

* **Source Reference:** [tasks/mlflow.py](../../../tasks/mlflow.py)

## 1. Architectural Role & Responsibilities

Mlflow tasks for pyinvoke.

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    doctor->>run: invoke
    serve->>run: invoke
    all->>task: invoke
```

### Component Diagram

```plantuml
component [mlflow] as Comp
Comp --> [Context]
Comp --> [task]
```

## 3. Class & Method Specifications

## Standalone Functions

### `doctor(ctx: Context) -> None`

Run mlflow doctor.

#### Inputs

* `ctx` (`Context`)

#### Outputs
* `None`

### `serve(ctx: Context, host: str, port: str, backend_uri: str) -> None`

Start the mlflow server.

#### Inputs

* `ctx` (`Context`)

* `host` (`str`)

* `port` (`str`)

* `backend_uri` (`str`)

#### Outputs
* `None`

### `all(_: Context) -> None`

Run all mlflow tasks.

#### Inputs

* `_` (`Context`)

#### Outputs
* `None`

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`

## Used By

* [metrics.py](../regression_model_template/core/metrics.md)

* [datasets.py](../regression_model_template/io/datasets.md)

* [registries.py](../regression_model_template/io/registries.md)

* [services.py](../regression_model_template/io/services.md)

* [evaluations.py](../regression_model_template/jobs/evaluations.md)

* [training.py](../regression_model_template/jobs/training.md)

* [tuning.py](../regression_model_template/jobs/tuning.md)

* [signers.py](../regression_model_template/utils/signers.md)

* [test_metrics.py](../tests/core/test_metrics.md)

* [test_services.py](../tests/io/test_services.md)

* [test_promotion.py](../tests/jobs/test_promotion.md)
