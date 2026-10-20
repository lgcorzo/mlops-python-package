---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "Module: test_hitl_governance"
source_path: "tests/controller/test_hitl_governance.py"
description: "Unit tests for Human-in-the-Loop (HITL) Policy enforcement and PR comment directives."
tags: ["module", "test_hitl_governance"]
timestamp: "2026-10-20T15:15:31Z"
generated: "agent:ast-documentation-generator"
verified: "true"
last_verified_commit: "275b872"
---
# Module Specification: test_hitl_governance

* **Source Reference:** [tests/controller/test_hitl_governance.py](../../../../tests/controller/test_hitl_governance.py)

# Module Overview

## Purpose

Unit tests for Human-in-the-Loop (HITL) Policy enforcement and PR comment directives.

## Responsibilities

Unit tests for Human-in-the-Loop (HITL) Policy enforcement and PR comment directives.

## Dependencies

* `re`

* `typing.Any`

* `typing.Dict`

# Each File Documentation

## Imported modules

* `re`

* `typing.Any`

* `typing.Dict`

## Exported classes

* `HITLPolicyEvaluator`

* `DarkGravityDirectiveHandler`

## Exported functions

* `test_hitl_branch_protection_policy_parameters`

* `test_hitl_merge_allowed_only_after_human_approval`

* `test_darkgravity_directive_status`

* `test_darkgravity_directive_validate`

* `test_darkgravity_directive_refine`

### Detected Architecture Patterns

Detected roles: Controller

## 2. UML Diagrams

### Class Diagram

```plantuml
classDiagram
    direction BT
    class HITLPolicyEvaluator {
        +can_agent_auto_merge(self: Any, pr_author: str, ci_status_green: bool, human_approvals: int, is_bot: bool) bool
    }
    class DarkGravityDirectiveHandler {
        +SANDBOX_BOUNDS: Any
        +parse_directive(self: Any, comment_text: str) Dict~(str, Any)~
        +execute_directive(self: Any, comment_text: str) Dict~(str, Any)~
    }
```

### Sequence Diagram

```plantuml
sequenceDiagram
    DarkGravityDirectiveHandler.parse_directive->>search: invoke
    DarkGravityDirectiveHandler.parse_directive->>lower: invoke
    DarkGravityDirectiveHandler.parse_directive->>group: invoke
    DarkGravityDirectiveHandler.parse_directive->>strip: invoke
    DarkGravityDirectiveHandler.execute_directive->>parse_directive: invoke
    test_hitl_branch_protection_policy_parameters->>HITLPolicyEvaluator: invoke
    test_hitl_branch_protection_policy_parameters->>can_agent_auto_merge: invoke
    test_hitl_merge_allowed_only_after_human_approval->>HITLPolicyEvaluator: invoke
    test_hitl_merge_allowed_only_after_human_approval->>can_agent_auto_merge: invoke
    test_darkgravity_directive_status->>DarkGravityDirectiveHandler: invoke
    test_darkgravity_directive_status->>parse_directive: invoke
    test_darkgravity_directive_status->>execute_directive: invoke
    test_darkgravity_directive_validate->>DarkGravityDirectiveHandler: invoke
    test_darkgravity_directive_validate->>parse_directive: invoke
    test_darkgravity_directive_validate->>execute_directive: invoke
    test_darkgravity_directive_refine->>DarkGravityDirectiveHandler: invoke
    test_darkgravity_directive_refine->>parse_directive: invoke
    test_darkgravity_directive_refine->>execute_directive: invoke
```

### Component Diagram

```plantuml
component [test_hitl_governance] as Comp
Comp --> [re]
Comp --> [Any]
Comp --> [Dict]
```

## 3. Class & Method Specifications

# Public Classes

### `HITLPolicyEvaluator`

## Overview

Evaluates HITL governance policies and PR merge gate restrictions.

## Constructor

* **`__init__(self: Any, required_approvals: int, enforce_admins: bool)`**

### Description

No description available.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `required_approvals`

  - **type**: int

  - **optional?**: Yes

  - **default value**: 1

* `enforce_admins`

  - **type**: bool

  - **optional?**: Yes

  - **default value**: True

### Output

* **return type**: None

* **semantic meaning**: Initialization

## Public Methods

* **`can_agent_auto_merge(self: Any, pr_author: str, ci_status_green: bool, human_approvals: int, is_bot: bool) -> bool`**

### Description

Determines whether a PR can be merged into protected main branch.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `pr_author`

  - **type**: str

  - **optional?**: No

* `ci_status_green`

  - **type**: bool

  - **optional?**: No

* `human_approvals`

  - **type**: int

  - **optional?**: No

* `is_bot`

  - **type**: bool

  - **optional?**: Yes

  - **default value**: True

### Output

* **return type**: bool

### `DarkGravityDirectiveHandler`

## Overview

Parses and executes interactive PR comment directives for @darkgravity bot.

## Attributes

* **`SANDBOX_BOUNDS`**

  - **Type**: Any

## Public Methods

* **`parse_directive(self: Any, comment_text: str) -> Dict[(str, Any)]`**

### Description

Parses @darkgravity directive commands from PR comments.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `comment_text`

  - **type**: str

  - **optional?**: No

### Output

* **return type**: Dict[(str, Any)]

* **`execute_directive(self: Any, comment_text: str) -> Dict[(str, Any)]`**

### Description

Executes directive logic within the sandboxed environment.

### Inputs

* `self`

  - **type**: Any

  - **optional?**: No

* `comment_text`

  - **type**: str

  - **optional?**: No

### Output

* **return type**: Dict[(str, Any)]

## Standalone Functions

### `test_hitl_branch_protection_policy_parameters() -> Any`

### Description

Verify HITL policy rules prevent automated agent merges without human review.

### Inputs

### Output

* **return type**: Any

### `test_hitl_merge_allowed_only_after_human_approval() -> Any`

### Description

Verify that merge is permitted only after 100% green CI AND >=1 human approval.

### Inputs

### Output

* **return type**: Any

### `test_darkgravity_directive_status() -> Any`

### Description

Test parsing and execution of @darkgravity /status directive.

### Inputs

### Output

* **return type**: Any

### `test_darkgravity_directive_validate() -> Any`

### Description

Test parsing and execution of @darkgravity /validate directive.

### Inputs

### Output

* **return type**: Any

### `test_darkgravity_directive_refine() -> Any`

### Description

Test parsing and execution of @darkgravity /refine directive with custom instructions.

### Inputs

### Output

* **return type**: Any

## Used By

_Not used by any other module._
