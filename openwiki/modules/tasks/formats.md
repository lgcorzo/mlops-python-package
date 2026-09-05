---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: formats"
source_path: "tasks/formats.py"
description: "Format tasks for pyinvoke."
tags: ["module", "formats"]
timestamp: "2026-09-05T11:29:30Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: formats

* **Source Reference:** [tasks/formats.py](../../../tasks/formats.py)

# Module Overview

## Purpose

Format tasks for pyinvoke.

## Responsibilities

Format tasks for pyinvoke.

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`

# Each File Documentation

## Imported modules

* `invoke.context.Context`

* `invoke.tasks.task`

## Exported functions

* `imports`

* `sources`

* `all`

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

### Description

Format python imports with ruff.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `sources(ctx: Context) -> None`

### Description

Format python sources with ruff.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `all(_: Context) -> None`

### Description

Run all format tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
