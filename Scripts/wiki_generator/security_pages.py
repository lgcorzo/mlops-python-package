from .config import make_frontmatter

def get_security_architecture_md():
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="SecurityView",
        concept_type="security",
        title="Security Architecture & Threat Mitigation",
        description="ISO 42010 SecurityView / ISO 15289 Description documentation for STRIDE threat modeling, model signing, and rate limiting.",
        tags=["iso42010", "okf", "security_view", "security", "threat_model"]
    )
    return fm + "\n\n" + """# Security Architecture & Threat Mitigation

> **Purpose**: Detail the threat analysis, defense-in-depth security controls, input validation gates, and cryptographic protections implemented across the system.

---

## 1. STRIDE Threat Model & Defense Matrix

| Threat Category | Potential Attack Vector | System Defense Mechanism | Source File Citation |
| :--- | :--- | :--- | :--- |
| **Spoofing** | Unauthorized clients submitting fake predictions | JWT / Bearer token validation, mTLS in container overlay | `controller/kafka_app.py:L69-L79` |
| **Tampering** | Model artifact poisoning or payload modification | SHA-256 hash attestation via `InferSigner` | `utils/signers.py:L21-L51` |
| **Repudiation** | Disputing historical inferences or training runs | Immutable MLflow run history and signed prediction logs | `io/services.py:L162-L252` |
| **Information Disclosure** | Leakage of PII or dataset values into application logs | Loguru message sanitization, log-leakage regression tests | `tests/controller/test_log_leakage.py:L1-L60` |
| **Denial of Service (DoS)** | Exhaustion of compute via unbounded payloads or floods | Sliding-window `RateLimiter` & max column checks (`MAX_TRACKED_IPS`) | `controller/kafka_app.py:L82-L112` |
| **Elevation of Privilege** | Code injection via untrusted configuration serialization | OmegaConf strict YAML schema parsing (no `eval` / `pickle`) | `io/configs.py:L16-L68` |

---

## 2. Sliding-Window Rate Limiting (`controller/kafka_app.py`)

To protect inference endpoints against volumetric Denial of Service (DoS), the `RateLimiter` enforces request quotas per client IP:

```mermaid
graph TD
    REQ["Incoming Request (Client IP)"] --> CHECK{"Request Count in Window < 100?"}
    CHECK -->|Yes| ALLOW["Record Timestamp & Allow Request"]
    CHECK -->|No| REJECT["Raise 429 Too Many Requests"]

    subgraph MemoryCleanup["Memory Bound Protection"]
        EVICT["Evict oldest IPs when tracked > 10,000"]
    end
    ALLOW -.-> EVICT
```

- **Algorithm**: In-memory sliding window using double-ended queues (`collections.deque`).
- **Quota**: Default 100 requests per 60-second window.
- **Resource Bound**: Upper bound on tracked IP cache (`MAX_TRACKED_IPS = 10,000`) prevents memory exhaustion attacks.

---

## 3. Cryptographic Model Attestation (`utils/signers.py`)

The `InferSigner` computes a deterministic SHA-256 digest over serialized input-output pairs:

$$\text{Signature} = \text{SHA256}(\text{JSON}(\text{Inputs}) \mathbin{\Vert} \text{JSON}(\text{Outputs}))$$

This guarantees that inference results can be cryptographically verified against historical records during external compliance audits.

---

> *Related: [HITL Governance](hitl_governance.md) · [Verification Triad](verification_triad.md) · [Master Index](../index.md)*
"""

def get_hitl_governance_md():
    fm = make_frontmatter(
        doc_type="Policy",
        viewpoint="SecurityView",
        concept_type="security",
        title="Human-in-the-Loop (HITL) Governance Policy",
        description="ISO 42010 SecurityView / ISO 15289 Policy documentation establishing mandatory human verification gates for model promotions and pull requests.",
        tags=["iso42010", "okf", "policy", "hitl", "governance"]
    )
    return fm + "\n\n" + """# Human-in-the-Loop (HITL) Governance Policy

> **Policy Directive**: Automated agents and CI/CD pipelines are strictly prohibited from automatically merging code into `main` or promoting machine learning models to production aliases without explicit human sign-off.

---

## 1. Governance Principles

1. **Non-Autonomous Production Promotion**: Model promotion to the `champion` alias requires human review of evaluation metrics and XAI reports.
2. **Mandatory Human PR Review**: Autonomous factory agents (Dark Gravity / ZeroClaw / Jules) may create feature branches and open PRs, but **merges into default branches MUST be a manual human action**.
3. **Four-Vertex Promotion Mesh**: Prior to promoting any candidate model, four quality gates must be satisfied:

```mermaid
graph TD
    V1["Vertex 1: Metrics Validation\n(MSE / RMSE threshold check)"] --> V2["Vertex 2: Fairness & XAI Audit\n(SHAP attribution review)"]
    V2 --> V3["Vertex 3: Security & Signature Gate\n(InferSigner attestation)"]
    V3 --> V4["Vertex 4: Human Sign-off\n(Data Scientist / Lead approval)"]
    V4 --> PROMOTE["Promote to 'champion' in MLflow"]

    classDef vertex fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef action fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#f8fafc;
    class V1,V2,V3,V4 vertex;
    class PROMOTE action;
```

---

## 2. Threshold Check Criteria

| Metric | Promotion Condition | Rationale |
|:---|:---|:---|
| **$R^2$ Score** | $R^2_{\text{challenger} \ge R^2_{\text{champion}$ | Model explanatory power must not regress. |
| **RMSE** | $\text{RMSE}_{\text{challenger} \le \text{RMSE}_{\text{champion} \times 1.02$ | Absolute error must remain within 2% margin. |
| **SHAP Drift** | Top-3 features match baseline ranking | Prevents anomalous feature weight distortions. |
| **Schema Compatibility** | 100% Pandera validation | Guarantees zero input contract breakage. |

---

> *Related: [Verification Triad](verification_triad.md) · [Compliance Audit](compliance_audit.md) · [Master Index](../index.md)*
"""

def get_verification_triad_md():
    fm = make_frontmatter(
        doc_type="Policy",
        viewpoint="SecurityView",
        concept_type="security",
        title="Verification Triad — Three-Vertex Quality Gates",
        description="ISO 42010 SecurityView / ISO 15289 Policy documentation establishing the Logical, Architectural, and Security quality verification gates.",
        tags=["iso42010", "okf", "policy", "verification_triad", "quality_gates"]
    )
    return fm + "\n\n" + """# Verification Triad — Three-Vertex Quality Gates

> **Purpose**: Define the 3-vertex quality verification triad governing all code modifications and pull requests before deployment.

---

## 1. The Verification Triad Model

```mermaid
flowchart TD
    subgraph Triad["The 3-Vertex Quality Verification Triad"]
        L["Logical Vertex\n(29 Pytest suites, ≥95% coverage)"]
        A["Architectural Vertex\n(Ruff, Mypy, DVC pipeline DAG)"]
        S["Security Vertex\n(Sanitization, DoS benchmarks, signing)"]
    end

    L --- A
    A --- S
    S --- L

    Triad --> GATE{"All 3 Gates Green?"}
    GATE -->|Yes| APPROVE["Permit Human Merge / Deployment"]
    GATE -->|No| REJECT["Block CI/CD Pipeline"]

    classDef triad fill:#1e293b,stroke:#818cf8,stroke-width:2px,color:#f8fafc;
    class L,A,S triad;
```

---

## 2. Vertex Specifications

### Vertex 1: Logical Quality Gate
- **Tooling**: `pytest`, `pytest-cov`, `pytest-mock`.
- **Criteria**:
  - All 29 unit and integration test suites in `tests/` pass with zero failures.
  - Overall codebase test coverage reaches or exceeds 95%.
  - Execution spans controller, core, io, jobs, performance, and utility submodules.

### Vertex 2: Architectural Quality Gate
- **Tooling**: `ruff` (linter and formatter), `mypy` (strict static typing), `dvc` (DAG validation).
- **Criteria**:
  - Zero linting errors under standard rules (`ruff check .`).
  - Zero type inconsistency errors under strict type checking (`mypy src/`).
  - Data pipelines defined in `dvc.yaml` execute deterministically via `dvc repro`.

### Vertex 3: Security & Sanitization Quality Gate
- **Tooling**: Security test suites, Bandit AST scanner, memory benchmarks.
- **Criteria**:
  - Zero sensitive data or raw payload leakage into application logs (`tests/controller/test_log_leakage.py`).
  - Rate limiting sliding window prevents DoS floods (`tests/controller/test_rate_limiter.py`, `test_kafka_app_dos.py`).
  - Cryptographic signatures generated and verified on inference outputs.

---

> *Related: [Security Architecture](security_architecture.md) · [HITL Governance](hitl_governance.md) · [Test Plan](../quality/test_plan_report.md)*
"""

def get_compliance_audit_md():
    fm = make_frontmatter(
        doc_type="Report",
        viewpoint="SecurityView",
        concept_type="security",
        title="Compliance & Audit Trail Specification",
        description="ISO 42010 SecurityView / ISO 15289 Report documentation for EU AI Act conformity assessment and MLOps auditability.",
        tags=["iso42010", "okf", "report", "compliance", "eu_ai_act"]
    )
    return fm + "\n\n" + """# Compliance & Audit Trail Specification

> **Purpose**: Document regulatory compliance alignments, specifically addressing EU AI Act (Regulation 2024/1689) requirements for high-risk AI lifecycle management.

---

## 1. EU AI Act Conformity Assessment

| EU AI Act Article | Regulatory Requirement | Repository Implementation Mechanism |
|:---|:---|:---|
| **Article 10** | **Data Governance**: Datasets must be relevant, representative, and validated. | DVC immutable versioning, Parquet schema enforcement, Pandera validation. |
| **Article 11** | **Technical Documentation**: Comprehensive technical records before market placement. | ISO 42010 / 15289 wiki documentation with 1:1 codebase mirroring. |
| **Article 12** | **Record-Keeping & Logging**: Automatic logging of events over the system lifecycle. | MLflow run parameter tracking, Loguru structured logs, SHA-256 signatures. |
| **Article 13** | **Transparency**: Output must be interpretable to deployers and users. | SHAP TreeExplainer feature attributions generated by `ExplanationsJob`. |
| **Article 14** | **Human Oversight**: High-risk AI systems must allow effective human intervention. | Human-in-the-Loop (HITL) merge policy and model promotion gates. |
| **Article 15** | **Accuracy & Robustness**: Resilient against errors, faults, and adversarial inputs. | 29 Pytest suites, Pandera schema guards, rate-limited FastAPI endpoints. |

---

## 2. Audit Trail Data Flow

```mermaid
sequenceDiagram
    autonumber
    participant Pipeline as MLOps Job
    participant DVC as DVC Data Registry
    participant MLF as MLflow Server
    participant Signer as InferSigner
    participant Audit as Compliance Auditor

    Pipeline->>DVC: Capture input data git-hash
    Pipeline->>MLF: Log code commit, params & metrics
    Pipeline->>Signer: Sign input-output bundle
    Signer-->>Pipeline: SHA-256 signature
    Pipeline->>MLF: Persist signed artifacts
    Audit->>MLF: Inspect run provenance & metrics
    Audit->>DVC: Reconstruct exact training dataset
    Audit-->>Audit: Confirm 100% reproducible audit trail
```

---

> *Related: [HITL Governance](hitl_governance.md) · [Security Architecture](security_architecture.md) · [Master Index](../index.md)*
"""
