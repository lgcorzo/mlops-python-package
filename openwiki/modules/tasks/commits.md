---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: commits"
source_path: "tasks/commits.py"
description: "Commits tasks for pyinvoke."
tags: ["module", "commits"]
timestamp: "2026-08-28T06:13:58Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "3029bb6"
---
# Module Specification: commits

* **Source Reference:** [tasks/commits.py](../../../tasks/commits.py)

# Module Overview

## Purpose

Commits tasks for pyinvoke.

## Responsibilities

Commits tasks for pyinvoke.

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`

# Each File Documentation

## Imported modules

* `invoke.context.Context`

* `invoke.tasks.task`

## Exported functions

* `info`

* `bump`

* `commit`

* `all`

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

### Description

Print a guide for messages.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `bump(ctx: Context) -> None`

### Description

Bump the version of the package.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `commit(ctx: Context) -> None`

### Description

Commit all changes with a message.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `all(_: Context) -> None`

### Description

Run all commit tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
