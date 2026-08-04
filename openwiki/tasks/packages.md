---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "packages Documentation"
description: "Documentation for tasks/packages.py"
tags: ["module", "packages"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tasks/packages.py`

## Overview
**Purpose**: Package tasks for pyinvoke.

**Architecture Role**: Infrastructure

**Dependencies**:
- `invoke.tasks`
- `invoke.context`

**Exported Symbols**:
- `build`
- `all`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
build --> task
build --> run
all --> task
@enduml
```

## Classes
## Functions
### Function `build`
- **Description**: Build the python package.
- **Inputs**:
  - `ctx`: Context
  - `format`: str
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `all`
- **Description**: Run all package tasks.
- **Inputs**:
  - `_`: Context
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
