---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: docs"
source_path: "tasks/docs.py"
description: "Docs tasks for pyinvoke."
tags: ["module", "docs"]
timestamp: "2026-08-12T05:53:45Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: docs

* **Source Reference:** [tasks/docs.py](../../../tasks/docs.py)

## 1. Architectural Role & Responsibilities
Docs tasks for pyinvoke.

### Detected Architecture Patterns
Detected roles: General Subsystem

## 2. UML Diagrams
### Class Diagram
_No classes found._

### Sequence Diagram
```plantuml
sequenceDiagram
    serve->>run: invoke
    api->>run: invoke
    all->>task: invoke
```

### Component Diagram
```plantuml
component [docs] as Comp
Comp --> [Context]
Comp --> [task]
Comp --> [cleans]
```

## 3. Class & Method Specifications

## Standalone Functions

### `serve(ctx: Context, format: str, port: int) -> None`
Serve the API docs with pdoc.

#### Inputs
* `ctx` (`Context`)
* `format` (`str`)
* `port` (`int`)

#### Outputs
* `None`

### `api(ctx: Context, format: str, output_dir: str) -> None`
Generate the API docs with pdoc.

#### Inputs
* `ctx` (`Context`)
* `format` (`str`)
* `output_dir` (`str`)

#### Outputs
* `None`

### `all(_: Context) -> None`
Run all docs tasks.

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
