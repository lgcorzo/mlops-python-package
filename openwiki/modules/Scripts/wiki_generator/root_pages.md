---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: root_pages"
source_path: "Scripts/wiki_generator/root_pages.py"
description: "No description available."
tags: ["module", "root_pages"]
timestamp: "2026-10-08T15:04:16Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "a2a679e"
---
# Module Specification: root_pages

* **Source Reference:** [Scripts/wiki_generator/root_pages.py](../../../../Scripts/wiki_generator/root_pages.py)

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

* `get_home_md`

* `get_readme_md`

* `get_sidebar_md`

* `get_index_md`

* `get_glossary_md`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    get_home_md->>make_frontmatter: invoke
    get_readme_md->>make_frontmatter: invoke
    get_index_md->>make_frontmatter: invoke
    get_glossary_md->>make_frontmatter: invoke
```

### Component Diagram

```plantuml
component [root_pages] as Comp
Comp --> [make_frontmatter]
```

## 3. Class & Method Specifications

## Standalone Functions

### `get_home_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_readme_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_sidebar_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_index_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_glossary_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

## Used By

_Not used by any other module._
