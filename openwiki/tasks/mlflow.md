---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "mlflow Documentation"
description: "Documentation for tasks/mlflow.py"
tags: ["module", "mlflow"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tasks/mlflow.py`

## Overview
**Purpose**: Mlflow tasks for pyinvoke.

**Architecture Role**: Infrastructure

**Dependencies**:
- `invoke.tasks`
- `invoke.context`

**Exported Symbols**:
- `doctor`
- `serve`
- `all`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
doctor --> run
serve --> run
all --> task
@enduml
```

## Classes
## Functions
### Function `doctor`
- **Description**: Run mlflow doctor.
- **Inputs**:
  - `ctx`: Context
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `serve`
- **Description**: Start the mlflow server.
- **Inputs**:
  - `ctx`: Context
  - `host`: str
  - `port`: str
  - `backend_uri`: str
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `all`
- **Description**: Run all mlflow tasks.
- **Inputs**:
  - `_`: Context
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
