---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: checks"
source_path: "tasks/checks.py"
description: "Check tasks for pyinvoke."
tags: ["module", "checks"]
timestamp: "2026-09-05T11:29:30Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: checks

* **Source Reference:** [tasks/checks.py](../../../tasks/checks.py)

# Module Overview

## Purpose

Check tasks for pyinvoke.

## Responsibilities

Check tasks for pyinvoke.

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`

# Each File Documentation

## Imported modules

* `invoke.context.Context`

* `invoke.tasks.task`

## Exported functions

* `poetry`

* `format`

* `type`

* `code`

* `test`

* `security`

* `coverage`

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
    format->>run: invoke
    type->>run: invoke
    code->>run: invoke
    test->>run: invoke
    security->>run: invoke
    coverage->>run: invoke
    all->>task: invoke
```

### Component Diagram

```plantuml
component [checks] as Comp
Comp --> [Context]
Comp --> [task]
```

## 3. Class & Method Specifications

## Standalone Functions

### `poetry(ctx: Context) -> None`

### Description

Check poetry config files.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `format(ctx: Context) -> None`

### Description

Check the formats with ruff.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `type(ctx: Context) -> None`

### Description

Check the types with mypy.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `code(ctx: Context) -> None`

### Description

Check the codes with ruff.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `test(ctx: Context) -> None`

### Description

Check the tests with pytest.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `security(ctx: Context) -> None`

### Description

Check the security with bandit.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `coverage(ctx: Context) -> None`

### Description

Check the coverage with coverage.

### Inputs

* `ctx`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

### `all(_: Context) -> None`

### Description

Run all check tasks.

### Inputs

* `_`

  - **type**: Context

  - **optional?**: No

### Output

* **return type**: None

## Used By

_Not used by any other module._
