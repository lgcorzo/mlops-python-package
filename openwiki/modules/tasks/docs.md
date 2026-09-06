---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: docs"
source_path: "tasks/docs.py"
description: "Docs tasks for pyinvoke."
tags: ["module", "docs"]
timestamp: "2026-09-06T06:26:18Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "4860b15"
---
# Module Specification: docs

* **Source Reference:** [tasks/docs.py](../../../tasks/docs.py)

# Module Overview

## Purpose

Docs tasks for pyinvoke.

## Responsibilities

Docs tasks for pyinvoke.

## Dependencies

* `invoke.context.Context`

* `invoke.tasks.task`

* `.cleans`

# Each File Documentation

## Imported modules

* `invoke.context.Context`

* `invoke.tasks.task`

* `.cleans`

## Exported interfaces

_Dependent on implementation_

## Exported functions

* `serve`

* `api`

* `all`

## Public API

_Dependent on implementation_

## Internal architecture

_Dependent on implementation_

## Execution flow

_Dependent on implementation_

## Sequence explanation

_Dependent on implementation_

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

## Examples

_Dependent on implementation_

## 3. Class & Method Specifications

## Standalone Functions

### `serve(ctx: Context, format: str, port: int) -> None`

### Description

Serve the API docs with pdoc.

### Inputs

* `ctx`

  - **type**: Context

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `format`

  - **type**: str

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: Yes

  - **default value**: DOC_FORMAT

* `port`

  - **type**: int

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: Yes

  - **default value**: 8088

### Output

* **return type**: None

* **semantic meaning**: _Dependent on implementation_

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

### `api(ctx: Context, format: str, output_dir: str) -> None`

### Description

Generate the API docs with pdoc.

### Inputs

* `ctx`

  - **type**: Context

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

* `format`

  - **type**: str

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: Yes

  - **default value**: DOC_FORMAT

* `output_dir`

  - **type**: str

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: Yes

  - **default value**: OUTPUT_DIR

### Output

* **return type**: None

* **semantic meaning**: _Dependent on implementation_

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

### `all(_: Context) -> None`

### Description

Run all docs tasks.

### Inputs

* `_`

  - **type**: Context

  - **meaning**: _Parameter description_

  - **valid values**: _Dependent on implementation_

  - **optional?**: No

### Output

* **return type**: None

* **semantic meaning**: _Dependent on implementation_

* **possible null values**: _Dependent on implementation_

* **exceptions**: _Dependent on implementation_

### Side Effects

_Dependent on implementation_

### Complexity

Time Complexity: _Dependent on implementation_

Space Complexity: _Dependent on implementation_

### Example

_Dependent on implementation_

## Used By

_Not used by any other module._
