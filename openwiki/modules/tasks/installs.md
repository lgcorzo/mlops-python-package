---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: installs"
source_path: "tasks/installs.py"
description: "Install tasks for pyinvoke."
tags: ["module", "installs"]
timestamp: "2026-08-14T05:37:38Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: installs

* **Source Reference:** [tasks/installs.py](../../../tasks/installs.py)

## 1. Architectural Role & Responsibilities
Install tasks for pyinvoke.

### Detected Architecture Patterns
Detected roles: General Subsystem

## 2. UML Diagrams
### Class Diagram
_No classes found._

### Sequence Diagram
```plantuml
sequenceDiagram
    poetry->>run: invoke
    pre_commit->>run: invoke
    all->>task: invoke
```

### Component Diagram
```plantuml
component [installs] as Comp
Comp --> [Context]
Comp --> [task]
```

## 3. Class & Method Specifications

## Standalone Functions

### `poetry(ctx: Context) -> None`
Install poetry packages.

#### Inputs
* `ctx` (`Context`)

#### Outputs
* `None`

### `pre_commit(ctx: Context) -> None`
Install pre-commit hooks on git.

#### Inputs
* `ctx` (`Context`)

#### Outputs
* `None`

### `all(_: Context) -> None`
Run all install tasks.

#### Inputs
* `_` (`Context`)

#### Outputs
* `None`

## Dependencies

* `invoke.context.Context`
* `invoke.tasks.task`

## Used By

_Not used by any other module._
