---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: commits"
source_path: "tasks/commits.py"
description: "Commits tasks for pyinvoke."
tags: ["module", "commits"]
timestamp: "2026-08-18T05:58:44Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "5aba7e1"
---
# Module Specification: commits

* **Source Reference:** [tasks/commits.py](../../../tasks/commits.py)

## 1. Architectural Role & Responsibilities

Commits tasks for pyinvoke.

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    info->>run: invoke
    bump->>run: invoke
    commit->>run: invoke
    all->>task: invoke
```

### Component Diagram

```plantuml
component [commits] as Comp
Comp --> [Context]
Comp --> [task]
```

## 3. Class & Method Specifications

## Standalone Functions

### `info(ctx: Context) -> None`

Print a guide for messages.

#### Inputs

* `ctx` (`Context`)

#### Outputs
* `None`

### `bump(ctx: Context) -> None`

Bump the version of the package.

#### Inputs

* `ctx` (`Context`)

#### Outputs
* `None`

### `commit(ctx: Context) -> None`

Commit all changes with a message.

#### Inputs

* `ctx` (`Context`)

#### Outputs
* `None`

### `all(_: Context) -> None`

Run all commit tasks.

#### Inputs

* `_` (`Context`)

#### Outputs
* `None`

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`

## Used By

_Not used by any other module._
