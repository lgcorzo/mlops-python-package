---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: cleans"
source_path: "tasks/cleans.py"
description: "Clean tasks for pyinvoke."
tags: ["module", "cleans"]
timestamp: "2026-09-01T16:59:35Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "193029c"
---
# Module Specification: cleans

* **Source Reference:** [tasks/cleans.py](../../../tasks/cleans.py)

# Module Overview

## Purpose

Clean tasks for pyinvoke.

## Responsibilities

Clean tasks for pyinvoke.

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`

# Each File Documentation

## Imported modules

* `invoke.context.Context`

* `invoke.tasks.task`

## Exported functions

* `mypy`

* `ruff`

* `pytest`

* `coverage`

* `dist`

* `docs`

* `cache`

* `mlruns`

* `outputs`

* `venv`

* `poetry`

* `python`

* `requirements`

* `environment`

* `tools`

* `folders`

* `sources`

* `projects`

* `all`

* `reset`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    mypy->>run: invoke
    ruff->>run: invoke
    pytest->>run: invoke
    coverage->>run: invoke
    dist->>run: invoke
    docs->>run: invoke
    cache->>run: invoke
    mlruns->>run: invoke
    outputs->>run: invoke
    venv->>run: invoke
    poetry->>run: invoke
    python->>run: invoke
    requirements->>run: invoke
    environment->>run: invoke
    tools->>task: invoke
    folders->>task: invoke
    sources->>task: invoke
    projects->>task: invoke
    all->>task: invoke
    reset->>task: invoke
```

### Component Diagram

```plantuml
component [cleans] as Comp
Comp --> [Context]
Comp --> [task]
```

## 3. Class & Method Specifications

## Standalone Functions

### `mypy(ctx: Context) -> None`

### Description

Clean the mypy tool.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `ruff(ctx: Context) -> None`

### Description

Clean the ruff tool.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `pytest(ctx: Context) -> None`

### Description

Clean the pytest tool.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `coverage(ctx: Context) -> None`

### Description

Clean the coverage tool.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `dist(ctx: Context) -> None`

### Description

Clean the dist folder.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `docs(ctx: Context) -> None`

### Description

Clean the docs folder.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `cache(ctx: Context) -> None`

### Description

Clean the cache folder.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `mlruns(ctx: Context) -> None`

### Description

Clean the mlruns folder.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `outputs(ctx: Context) -> None`

### Description

Clean the outputs folder.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `venv(ctx: Context) -> None`

### Description

Clean the venv folder.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `poetry(ctx: Context) -> None`

### Description

Clean poetry lock file.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `python(ctx: Context) -> None`

### Description

Clean python caches and bytecodes.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `requirements(ctx: Context) -> None`

### Description

Clean the project requirements file.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `environment(ctx: Context) -> None`

### Description

Clean the project environment file.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `tools(_: Context) -> None`

### Description

Run all tools tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `folders(_: Context) -> None`

### Description

Run all folders tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `sources(_: Context) -> None`

### Description

Run all sources tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `projects(_: Context) -> None`

### Description

Run all projects tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `all(_: Context) -> None`

### Description

Run all tools and folders tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `reset(_: Context) -> None`

### Description

Run all tools, folders, sources, and projects tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
