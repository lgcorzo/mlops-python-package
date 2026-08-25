---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: projects"
source_path: "tasks/projects.py"
description: "Project tasks for pyinvoke."
tags: ["module", "projects"]
timestamp: "2026-08-25T05:40:20Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "74a428a"
---
# Module Specification: projects

* **Source Reference:** [tasks/projects.py](../../../tasks/projects.py)

## 1. Architectural Role & Responsibilities

Project tasks for pyinvoke.

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    requirements->>run: invoke
    environment->>task: invoke
    environment->>open: invoke
    environment->>strip: invoke
    environment->>dump: invoke
    environment->>write: invoke
    environment->>read: invoke
    environment->>split: invoke
    environment->>append: invoke
    run->>run: invoke
    run->>capitalize: invoke
    all->>task: invoke
    all->>call: invoke
```

### Component Diagram

```plantuml
component [projects] as Comp
Comp --> [json]
Comp --> [Context]
Comp --> [call]
Comp --> [task]
```

## 3. Class & Method Specifications

## Standalone Functions

### `requirements(ctx: Context) -> None`

Export the project requirements file.

#### Inputs

* `ctx` (`Context`)

#### Outputs
* `None`

### `environment(ctx: Context) -> None`

Export the project environment file.

#### Inputs

* `ctx` (`Context`)

#### Outputs
* `None`

### `run(ctx: Context, job: str) -> None`

Run an mlflow project from the MLproject file.

#### Inputs

* `ctx` (`Context`)

* `job` (`str`)

#### Outputs
* `None`

### `all(_: Context) -> None`

Run all project tasks.

#### Inputs

* `_` (`Context`)

#### Outputs
* `None`

## Dependencies

* `json`

* `invoke.context.Context`

* `invoke.tasks.call`

* `invoke.tasks.task`

## Used By

_Not used by any other module._
