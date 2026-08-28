---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: installs"
source_path: "tasks/installs.py"
description: "Install tasks for pyinvoke."
tags: ["module", "installs"]
timestamp: "2026-08-28T06:13:58Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "3029bb6"
---
# Module Specification: installs

* **Source Reference:** [tasks/installs.py](../../../tasks/installs.py)

# Module Overview

## Purpose

Install tasks for pyinvoke.

## Responsibilities

Install tasks for pyinvoke.

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`

# Each File Documentation

## Imported modules

* `invoke.context.Context`

* `invoke.tasks.task`

## Exported functions

* `poetry`

* `pre_commit`

* `all`

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

### Description

Install poetry packages.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `pre_commit(ctx: Context) -> None`

### Description

Install pre-commit hooks on git.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `all(_: Context) -> None`

### Description

Run all install tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
