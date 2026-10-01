---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "module"
title: "regression_model_template::jobs::promotion — Model Registry Promotion Gate"
source_path: "src/regression_model_template/jobs/promotion.py"
description: "Promotes evaluated candidate model versions to designated production aliases (e.g. champion) in MLflow."
tags: ["iso42010", "okf", "component_view", "promotion", "governance"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# regression_model_template::jobs::promotion — Model Registry Promotion Gate

> **Source**: `src/regression_model_template/jobs/promotion.py` (Lines: L1-L57)  
> **Layer**: Application  
> **Role**: Promotes qualified candidate model versions to target aliases (e.g. `champion`) in the MLflow Model Registry.

---

## 1. Class Diagram

```mermaid
classDiagram
    class PromotionJob {
        +str KIND = "PromotionJob"
        +str alias
        +int version
        +run() Locals
    }
    PromotionJob --|> Job : implements
```

---

> *Related: [HITL Governance](../../../security/hitl_governance.md) · [Registries](../io/registries.md)*
