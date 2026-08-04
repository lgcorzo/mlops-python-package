---
iso_doc_type: "Description"
iso_viewpoint: "ArchitectureDescription"
type: "concept"
title: "convert_links Documentation"
description: "Documentation for skills/validate/scripts/convert_links.py"
tags: ["module", "convert_links"]
timestamp: "2026-08-04T05:28:53Z"
generated: "agent:ast-documentation-generator"
verified: "true"
---

# Module: `skills/validate/scripts/convert_links.py`

## Overview
**Purpose**: Module providing various functionalities.

**Architecture Role**: Infrastructure

**Dependencies**:
- `re`
- `glob`
- `os`

**Exported Symbols**:
- `camel_to_snake`
- `resolve_wiki_link`
- `convert_file`
- `main`

## UML Class Diagram
```plantuml
@startuml
@enduml
```

## Call Graph
```plantuml
@startuml
camel_to_snake --> sub
camel_to_snake --> lower
camel_to_snake --> lower
camel_to_snake --> lower
camel_to_snake --> sub
resolve_wiki_link --> split
resolve_wiki_link --> normpath
resolve_wiki_link --> exists
resolve_wiki_link --> walk
resolve_wiki_link --> append
resolve_wiki_link --> join
resolve_wiki_link --> join
resolve_wiki_link --> relpath
resolve_wiki_link --> camel_to_snake
resolve_wiki_link --> splitext
resolve_wiki_link --> relpath
resolve_wiki_link --> lower
resolve_wiki_link --> lower
resolve_wiki_link --> lower
resolve_wiki_link --> lower
resolve_wiki_link --> join
resolve_wiki_link --> camel_to_snake
convert_file --> dirname
convert_file --> compile
convert_file --> sub
convert_file --> compile
convert_file --> sub
convert_file --> dirname
convert_file --> compile
convert_file --> sub
convert_file --> compile
convert_file --> sub
convert_file --> sub
convert_file --> open
convert_file --> read
convert_file --> strip
convert_file --> resolve_wiki_link
convert_file --> groups
convert_file --> startswith
convert_file --> normpath
convert_file --> startswith
convert_file --> startswith
convert_file --> append
convert_file --> group
convert_file --> split
convert_file --> join
convert_file --> exists
convert_file --> int
convert_file --> open
convert_file --> write
convert_file --> group
convert_file --> group
convert_file --> group
convert_file --> append
convert_file --> split
convert_file --> append
convert_file --> join
convert_file --> relpath
convert_file --> startswith
convert_file --> append
convert_file --> group
convert_file --> len
convert_file --> group
convert_file --> group
convert_file --> group
convert_file --> group
convert_file --> split
convert_file --> append
convert_file --> group
convert_file --> len
convert_file --> len
convert_file --> len
convert_file --> len
convert_file --> len
convert_file --> len
main --> abspath
main --> glob
main --> print
main --> print
main --> exists
main --> print
main --> join
main --> convert_file
main --> len
@enduml
```

## Classes
## Functions
### Function `camel_to_snake`
- **Description**: No description available.
- **Inputs**:
  - `name`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `resolve_wiki_link`
- **Description**: No description available.
- **Inputs**:
  - `link_content`: Any
  - `current_file_dir`: Any
  - `wiki_root`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `convert_file`
- **Description**: No description available.
- **Inputs**:
  - `file_path`: Any
  - `wiki_root`: Any
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented

### Function `main`
- **Description**: No description available.
- **Inputs**:
- **Output**: `Any`
- **Side Effects**: Not documented
- **Complexity**: Not documented
