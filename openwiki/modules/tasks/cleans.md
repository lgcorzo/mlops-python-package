---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: cleans"
source_path: "tasks/cleans.py"
description: "Clean tasks for pyinvoke."
tags: ["module", "cleans"]
timestamp: "2026-08-17T05:34:56Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "73b4d7b"
---
# Module Specification: cleans

* **Source Reference:** [tasks/cleans.py](../../../tasks/cleans.py)

## 1. Architectural Role & Responsibilities

Clean tasks for pyinvoke.

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

Clean the mypy tool.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `ruff(ctx: Context) -> None`

Clean the ruff tool.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `pytest(ctx: Context) -> None`

Clean the pytest tool.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `coverage(ctx: Context) -> None`

Clean the coverage tool.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `dist(ctx: Context) -> None`

Clean the dist folder.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `docs(ctx: Context) -> None`

Clean the docs folder.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `cache(ctx: Context) -> None`

Clean the cache folder.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `mlruns(ctx: Context) -> None`

Clean the mlruns folder.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `outputs(ctx: Context) -> None`

Clean the outputs folder.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `venv(ctx: Context) -> None`

Clean the venv folder.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `poetry(ctx: Context) -> None`

Clean poetry lock file.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `python(ctx: Context) -> None`

Clean python caches and bytecodes.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `requirements(ctx: Context) -> None`

Clean the project requirements file.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `environment(ctx: Context) -> None`

Clean the project environment file.

#### Inputs

* `ctx` (`Context`)


#### Outputs
* `None`

### `tools(_: Context) -> None`

Run all tools tasks.

#### Inputs

* `_` (`Context`)


#### Outputs
* `None`

### `folders(_: Context) -> None`

Run all folders tasks.

#### Inputs

* `_` (`Context`)


#### Outputs
* `None`

### `sources(_: Context) -> None`

Run all sources tasks.

#### Inputs

* `_` (`Context`)


#### Outputs
* `None`

### `projects(_: Context) -> None`

Run all projects tasks.

#### Inputs

* `_` (`Context`)


#### Outputs
* `None`

### `all(_: Context) -> None`

Run all tools and folders tasks.

#### Inputs

* `_` (`Context`)


#### Outputs
* `None`

### `reset(_: Context) -> None`

Run all tools, folders, sources, and projects tasks.

#### Inputs

* `_` (`Context`)


#### Outputs
* `None`

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`


## Used By

_Not used by any other module._
