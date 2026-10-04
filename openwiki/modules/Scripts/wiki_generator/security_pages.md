---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: security_pages"
source_path: "Scripts/wiki_generator/security_pages.py"
description: "No description available."
tags: ["module", "security_pages"]
timestamp: "2026-10-04T13:34:09Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "d186315"
---
# Module Specification: security_pages

* **Source Reference:** [Scripts/wiki_generator/security_pages.py](../../../../Scripts/wiki_generator/security_pages.py)

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

* `get_security_architecture_md`

* `get_hitl_governance_md`

* `get_verification_triad_md`

* `get_compliance_audit_md`

### Detected Architecture Patterns

Detected roles: General Subsystem

## 2. UML Diagrams

### Class Diagram

_No classes found._

### Sequence Diagram

```plantuml
sequenceDiagram
    get_security_architecture_md->>make_frontmatter: invoke
    get_hitl_governance_md->>make_frontmatter: invoke
    get_verification_triad_md->>make_frontmatter: invoke
    get_compliance_audit_md->>make_frontmatter: invoke
```

### Component Diagram

```plantuml
component [security_pages] as Comp
Comp --> [make_frontmatter]
```

## 3. Class & Method Specifications

## Standalone Functions

### `get_security_architecture_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_hitl_governance_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_verification_triad_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

### `get_compliance_audit_md() -> Any`

### Description

No description available.

### Inputs

### Output

* **return type**: Any

## Used By

_Not used by any other module._
