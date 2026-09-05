---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: docs"
source_path: "tasks/docs.py"
description: "Docs tasks for pyinvoke."
tags: ["module", "docs"]
timestamp: "2026-09-05T05:14:18Z"
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

## Exported functions

* `serve`

* `api`

* `all`

## Exported interfaces

_No interfaces found._

## Public API

_See exported classes and functions._

## Internal architecture

_See architectural detected patterns and UML._

## Execution flow

_Execution flow depends on public API usage._

## Sequence explanation

_See sequence diagram._

## UML

_See diagrams below._

## Examples

_No module level examples available._

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

### Description

Serve the API docs with pdoc.

### Inputs

* `ctx`

  - **type**: Context

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `format`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: DOC_FORMAT

* `port`

  - **type**: int

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: 8088

### Output

* **return type**: None

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for serve

```

### `api(ctx: Context, format: str, output_dir: str) -> None`

### Description

Generate the API docs with pdoc.

### Inputs

* `ctx`

  - **type**: Context

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

* `format`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: DOC_FORMAT

* `output_dir`

  - **type**: str

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: Yes

  - **default value**: OUTPUT_DIR

### Output

* **return type**: None

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for api

```

### `all(_: Context) -> None`

### Description

Run all docs tasks.

### Inputs

* `_`

  - **type**: Context

  - **meaning**: Parameter description

  - **valid values**: Any valid value for the type

  - **optional?**: No

### Output

* **return type**: None

* **semantic meaning**: Result of the operation

* **possible null values**: Dependent on implementation

* **exceptions**: Unspecified

### Example

```python

# Example usage for all

```

## Used By

_Not used by any other module._
