---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "docs Documentation"
description: "Documentation for tasks/docs.py"
tags: ["module", "docs"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tasks/docs.py`

## Overview
**Purpose**: Docs tasks for pyinvoke.

**Architecture Role**: Infrastructure

**Dependencies**:
- `invoke.tasks`
- `invoke.context`

**Exported Symbols**:
- `serve`
- `api`
- `all`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
serve --> run
api --> run
all --> task
@enduml
```

## Classes
## Functions
### Function `serve`
- **Description**: Serve the API docs with pdoc.
- **Inputs**:
  - `ctx`: Context
  - `format`: str
  - `port`: int
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `api`
- **Description**: Generate the API docs with pdoc.
- **Inputs**:
  - `ctx`: Context
  - `format`: str
  - `output_dir`: str
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `all`
- **Description**: Run all docs tasks.
- **Inputs**:
  - `_`: Context
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
