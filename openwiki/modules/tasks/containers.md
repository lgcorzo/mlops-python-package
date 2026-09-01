---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: containers"
source_path: "tasks/containers.py"
description: "Container tasks for pyinvoke."
tags: ["module", "containers"]
timestamp: "2026-09-01T16:59:35Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "193029c"
---
# Module Specification: containers

* **Source Reference:** [tasks/containers.py](../../../tasks/containers.py)

# Module Overview

## Purpose

Container tasks for pyinvoke.

## Responsibilities

Container tasks for pyinvoke.

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`

* `.packages`

# Each File Documentation

## Imported modules

* `invoke.context.Context`

* `invoke.tasks.task`

* `.packages`

## Exported functions

* `compose`

* `build`

* `run`

* `all`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    compose->>run: invoke
    build->>task: invoke
    build->>run: invoke
    run->>run: invoke
    all->>task: invoke
```

### Component Diagram

```plantuml
component [containers] as Comp
Comp --> [Context]
Comp --> [task]
Comp --> [packages]
```

## 3. Class & Method Specifications

## Standalone Functions

### `compose(ctx: Context) -> None`

### Description

Start up docker compose.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `build(ctx: Context, tag: str) -> None`

### Description

Build the container image.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

* `tag`

  - **type**: str

  - **optional?**: Yes

  - **default value**: IMAGE_TAG

### Output

* **return type**: None

### `run(ctx: Context, tag: str) -> None`

### Description

Run the container image.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

* `tag`

  - **type**: str

  - **optional?**: Yes

  - **default value**: IMAGE_TAG

### Output

* **return type**: None

### `all(_: Context) -> None`

### Description

Run all container tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
