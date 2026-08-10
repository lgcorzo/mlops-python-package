---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: packages"
source_path: "tasks/packages.py"
description: "Package tasks for pyinvoke."
tags: ["module", "packages"]
timestamp: "2026-08-10T08:55:52Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "8412d40"
---
# Module Specification: packages

* **Source Reference:** [tasks/packages.py](../../../tasks/packages.py)

## 1. Architectural Role & Responsibilities
Package tasks for pyinvoke.

### Detected Architecture Patterns
Detected roles: General Subsystem

## 2. UML Diagrams
### Class Diagram
_No classes found._

### Sequence Diagram
```plantuml
sequenceDiagram
    build->>task: invoke
    build->>run: invoke
    all->>task: invoke
```

### Component Diagram
```plantuml
component [packages] as Comp
Comp --> [Context]
Comp --> [task]
Comp --> [cleans]
```

## 3. Class & Method Specifications

## Standalone Functions

### `build(ctx: Context, format: str) -> None`
Build the python package.

#### Inputs
* `ctx` (`Context`)
* `format` (`str`)

#### Outputs
* `None`

### `all(_: Context) -> None`
Run all package tasks.

#### Inputs
* `_` (`Context`)

#### Outputs
* `None`

## Dependencies

* `invoke.context.Context`
* `invoke.tasks.task`
* `.cleans`

## Used By

_Not used by any other module._
