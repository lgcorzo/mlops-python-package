---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: checks"
source_path: "tasks/checks.py"
description: "Check tasks for pyinvoke."
tags: ["module", "checks"]
timestamp: "2026-08-11T05:39:15Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "ce3f2af"
---
# Module Specification: checks

* **Source Reference:** [tasks/checks.py](../../../tasks/checks.py)

## 1. Architectural Role & Responsibilities
Check tasks for pyinvoke.

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
Check poetry config files.

#### Inputs
* `ctx` (`Context`)

#### Outputs
* `None`

### `format(ctx: Context) -> None`
Check the formats with ruff.

#### Inputs
* `ctx` (`Context`)

#### Outputs
* `None`

### `type(ctx: Context) -> None`
Check the types with mypy.

#### Inputs
* `ctx` (`Context`)

#### Outputs
* `None`

### `code(ctx: Context) -> None`
Check the codes with ruff.

#### Inputs
* `ctx` (`Context`)

#### Outputs
* `None`

### `test(ctx: Context) -> None`
Check the tests with pytest.

#### Inputs
* `ctx` (`Context`)

#### Outputs
* `None`

### `security(ctx: Context) -> None`
Check the security with bandit.

#### Inputs
* `ctx` (`Context`)

#### Outputs
* `None`

### `coverage(ctx: Context) -> None`
Check the coverage with coverage.

#### Inputs
* `ctx` (`Context`)

#### Outputs
* `None`

### `all(_: Context) -> None`
Run all check tasks.

#### Inputs
* `_` (`Context`)

#### Outputs
* `None`

## Dependencies

* `invoke.context.Context`
* `invoke.tasks.task`

## Used By

_Not used by any other module._
