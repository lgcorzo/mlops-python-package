---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: architecture_pages"
source_path: "Scripts/wiki_generator/architecture_pages.py"
description: "No description available."
tags: ["module", "architecture_pages"]
timestamp: "2026-10-04T13:34:09Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "d186315"
---
# Module Specification: architecture_pages

* **Source Reference:** [Scripts/wiki_generator/architecture_pages.py](../../../../Scripts/wiki_generator/architecture_pages.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

* `config.make_frontmatter`

# Each File Documentation

## Imported modules

* `config.make_frontmatter`

## Exported functions

* `get_business_context_md`

* `get_strategic_design_md`

* `get_tactical_design_md`

* `get_agent_specifications_md`

* `get_runtime_sequences_md`

* `get_infrastructure_adapters_md`

* `get_mission_data_model_md`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    get_business_context_md->>make_frontmatter: invoke
    get_strategic_design_md->>make_frontmatter: invoke
    get_tactical_design_md->>make_frontmatter: invoke
    get_agent_specifications_md->>make_frontmatter: invoke
    get_runtime_sequences_md->>make_frontmatter: invoke
    get_infrastructure_adapters_md->>make_frontmatter: invoke
    get_mission_data_model_md->>make_frontmatter: invoke
```

### Component Diagram

```plantuml
component [architecture_pages] as Comp
Comp --> [make_frontmatter]
```

## 3. Class & Method Specifications

## Standalone Functions

### `get_business_context_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_strategic_design_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_tactical_design_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_agent_specifications_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_runtime_sequences_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_infrastructure_adapters_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_mission_data_model_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

## Used By

_Not used by any other module._
