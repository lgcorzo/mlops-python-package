---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: mlflow"
source_path: "tasks/mlflow.py"
description: "Mlflow tasks for pyinvoke."
tags: ["module", "mlflow"]
timestamp: "2026-09-01T16:59:35Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "193029c"
---
# Module Specification: mlflow

* **Source Reference:** [tasks/mlflow.py](../../../tasks/mlflow.py)

# Module Overview

## Purpose

Mlflow tasks for pyinvoke.

## Responsibilities

Mlflow tasks for pyinvoke.

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`

# Each File Documentation

## Imported modules

* `invoke.context.Context`

* `invoke.tasks.task`

## Exported functions

* `doctor`

* `serve`

* `all`

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

### Description

Run mlflow doctor.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `serve(ctx: Context, host: str, port: str, backend_uri: str) -> None`

### Description

Start the mlflow server.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

* `host`

  - **type**: str

  - **optional?**: Yes

  - **default value**: '127.0.0.1'

* `port`

  - **type**: str

  - **optional?**: Yes

  - **default value**: '5000'

* `backend_uri`

  - **type**: str

  - **optional?**: Yes

  - **default value**: './mlruns'

### Output

* **return type**: None

### `all(_: Context) -> None`

### Description

Run all mlflow tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

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
