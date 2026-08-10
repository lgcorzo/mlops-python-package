---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: formats"
source_path: "tasks/formats.py"
description: "Format tasks for pyinvoke."
tags: ["module", "formats"]
timestamp: "2026-08-10T08:55:52Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "8412d40"
---
# Module Specification: formats

* **Source Reference:** [tasks/formats.py](../../../tasks/formats.py)

## 1. Architectural Role & Responsibilities
Format tasks for pyinvoke.

### Detected Architecture Patterns
Detected roles: General Subsystem

## 2. UML Diagrams
### Class Diagram
_No classes found._

### Sequence Diagram
```plantuml
sequenceDiagram
    imports->>run: invoke
    sources->>run: invoke
    all->>task: invoke
```

### Component Diagram
```plantuml
component [formats] as Comp
Comp --> [Context]
Comp --> [task]
```

## 3. Class & Method Specifications

## Standalone Functions

### `imports(ctx: Context) -> None`
Format python imports with ruff.

#### Inputs
* `ctx` (`Context`)

#### Outputs
* `None`

### `sources(ctx: Context) -> None`
Format python sources with ruff.

#### Inputs
* `ctx` (`Context`)

#### Outputs
* `None`

### `all(_: Context) -> None`
Run all format tasks.

#### Inputs
* `_` (`Context`)

#### Outputs
* `None`

## Dependencies

* `invoke.context.Context`
* `invoke.tasks.task`

## Used By

_Not used by any other module._
