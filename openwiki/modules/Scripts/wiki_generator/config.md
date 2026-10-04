---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: config"
source_path: "Scripts/wiki_generator/config.py"
description: "No description available."
tags: ["module", "config"]
timestamp: "2026-10-04T13:34:09Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "d186315"
---
# Module Specification: config

* **Source Reference:** [Scripts/wiki_generator/config.py](../../../../Scripts/wiki_generator/config.py)

# Module Overview

## Purpose

No description available.

## Responsibilities

No description available.

## Dependencies

_No dependencies found._

# Each File Documentation

## Exported functions

* `make_frontmatter`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    make_frontmatter->>join: invoke
```

### Component Diagram

```plantuml
component [config] as Comp
```

## 3. Class & Method Specifications

## Standalone Functions

### `make_frontmatter(doc_type: Any, viewpoint: Any, concept_type: Any, title: Any, description: Any, tags: Any, source_path: Any) -> Any`

### Description

No description available.

### Inputs

* `doc_type`

  - **type**: Any

  - **optional?**: No

* `viewpoint`

  - **type**: Any

  - **optional?**: No

* `concept_type`

  - **type**: Any

  - **optional?**: No

* `title`

  - **type**: Any

  - **optional?**: No

* `description`

  - **type**: Any

  - **optional?**: No

* `tags`

  - **type**: Any

  - **optional?**: No

* `source_path`

  - **type**: Any

  - **optional?**: Yes

  - **default value**: None

### Output

* **return type**: Any

## Used By

* [architecture_pages.py](../../Scripts/wiki_generator/architecture_pages.md)

* [module_pages.py](../../Scripts/wiki_generator/module_pages.md)

* [operations_pages.py](../../Scripts/wiki_generator/operations_pages.md)

* [quality_pages.py](../../Scripts/wiki_generator/quality_pages.md)

* [root_pages.py](../../Scripts/wiki_generator/root_pages.md)

* [security_pages.py](../../Scripts/wiki_generator/security_pages.md)
