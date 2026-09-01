---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: packages"
source_path: "tasks/packages.py"
description: "Package tasks for pyinvoke."
tags: ["module", "packages"]
timestamp: "2026-09-01T16:59:35Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "193029c"
---
# Module Specification: packages

* **Source Reference:** [tasks/packages.py](../../../tasks/packages.py)

# Module Overview

## Purpose

Package tasks for pyinvoke.

## Responsibilities

Package tasks for pyinvoke.

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`

* `.cleans`

# Each File Documentation

## Imported modules

* `invoke.context.Context`

* `invoke.tasks.task`

* `.cleans`

## Exported functions

* `build`

* `all`

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

### Description

Build the python package.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

* `format`

  - **type**: str

  - **optional?**: Yes

  - **default value**: BUILD_FORMAT

### Output

* **return type**: None

### `all(_: Context) -> None`

### Description

Run all package tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
