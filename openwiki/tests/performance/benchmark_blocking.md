---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "benchmark_blocking Documentation"
description: "Documentation for tests/performance/benchmark_blocking.py"
tags: ["module", "benchmark_blocking"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `tests/performance/benchmark_blocking.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Infrastructure

**Dependencies**:
- `time`
- `asyncio`

**Exported Symbols**:
- `sync_prediction`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
sync_prediction --> print
sync_prediction --> sleep
sync_prediction --> print
@enduml
```

## Classes
## Functions
### Function `sync_prediction`
- **Description**: Simulates a CPU-bound synchronous prediction call.
- **Inputs**:
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented
