---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "okf_validate Documentation"
description: "Documentation for skills/validate/scripts/okf_validate.py"
tags: ["module", "okf_validate"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `skills/validate/scripts/okf_validate.py`

## Overview
**Purpose**: OKF v0.2 Conformance Checker for OpenWiki Documentation.

**Architecture Role**: Infrastructure

**Dependencies**:
- `sys`
- `typing`
- `re`
- `glob`
- `os`
- `argparse`

**Exported Symbols**:
- `extract_frontmatter`
- `check_frontmatter_fields`
- `check_absolute_paths`
- `check_mermaid_syntax`
- `validate_wiki`
- `main`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
extract_frontmatter --> split
extract_frontmatter --> _parse_yaml
extract_frontmatter --> startswith
extract_frontmatter --> len
check_frontmatter_fields --> get
check_frontmatter_fields --> get
check_frontmatter_fields --> append
check_frontmatter_fields --> append
check_frontmatter_fields --> append
check_frontmatter_fields --> append
check_frontmatter_fields --> append
check_frontmatter_fields --> join
check_frontmatter_fields --> join
check_frontmatter_fields --> sorted
check_frontmatter_fields --> sorted
check_absolute_paths --> enumerate
check_absolute_paths --> splitlines
check_absolute_paths --> search
check_absolute_paths --> append
check_mermaid_syntax --> enumerate
check_mermaid_syntax --> splitlines
check_mermaid_syntax --> strip
check_mermaid_syntax --> startswith
check_mermaid_syntax --> append
check_mermaid_syntax --> startswith
check_mermaid_syntax --> append
check_mermaid_syntax --> append
check_mermaid_syntax --> append
check_mermaid_syntax --> count
check_mermaid_syntax --> count
check_mermaid_syntax --> count
check_mermaid_syntax --> count
check_mermaid_syntax --> count
check_mermaid_syntax --> count
validate_wiki --> sorted
validate_wiki --> print
validate_wiki --> print
validate_wiki --> print
validate_wiki --> print
validate_wiki --> print
validate_wiki --> print
validate_wiki --> print
validate_wiki --> print
validate_wiki --> print
validate_wiki --> print
validate_wiki --> glob
validate_wiki --> print
validate_wiki --> relpath
validate_wiki --> extract_frontmatter
validate_wiki --> extend
validate_wiki --> print
validate_wiki --> print
validate_wiki --> len
validate_wiki --> print
validate_wiki --> join
validate_wiki --> strip
validate_wiki --> append
validate_wiki --> append
validate_wiki --> extend
validate_wiki --> check_absolute_paths
validate_wiki --> extend
validate_wiki --> extend
validate_wiki --> print
validate_wiki --> getcwd
validate_wiki --> open
validate_wiki --> read
validate_wiki --> append
validate_wiki --> check_frontmatter_fields
validate_wiki --> check_mermaid_syntax
validate_wiki --> len
validate_wiki --> len
main --> ArgumentParser
main --> add_argument
main --> add_argument
main --> parse_args
main --> validate_wiki
main --> exit
main --> isdir
main --> print
main --> exit
@enduml
```

## Classes
## Functions
### Function `extract_frontmatter`
- **Description**: Split YAML frontmatter from Markdown body.
- **Inputs**:
  - `content`: str
- **Output**: `tuple[dict[str, Any], str]`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `check_frontmatter_fields`
- **Description**: Validate required and optional frontmatter fields.
- **Inputs**:
  - `fm`: dict[str, Any]
  - `filepath`: str
  - `strict`: bool
- **Output**: `list[str]`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `check_absolute_paths`
- **Description**: Detect absolute file paths in the document body.
- **Inputs**:
  - `body`: str
  - `filepath`: str
- **Output**: `list[str]`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `check_mermaid_syntax`
- **Description**: Basic structural validation of Mermaid code blocks.
- **Inputs**:
  - `body`: str
  - `filepath`: str
- **Output**: `list[str]`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `validate_wiki`
- **Description**: Validate all .md files under wiki_path. Returns error count.
- **Inputs**:
  - `wiki_path`: str
  - `strict`: bool
- **Output**: `int`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `main`
- **Description**: No description available.
- **Inputs**:
- **Output**: `None`
- **Side Effects**: Not documented
- **Complexity**: Not documented
