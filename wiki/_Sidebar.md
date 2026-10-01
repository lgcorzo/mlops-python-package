## 🏠 Navigation

- [Home](Home.md)
- [Master Index](index.md)
- [Glossary](GLOSSARY.md)
- [Documentation Guide](README.md)

## 📊 Architecture (ISO 42010)

- [Business Context](architecture/business_context.md)
- [Strategic Design](architecture/strategic_design.md)
- [Tactical Design](architecture/tactical_design.md)
- [Lifecycle Job Specs](architecture/agent_specifications.md)
- [Runtime Sequences](architecture/runtime_sequences.md)
- [Data Model & Contracts](architecture/mission_data_model.md)
- [Infrastructure Adapters](architecture/infrastructure_adapters.md)

## 🔒 Security & Governance

- [Security Architecture](security/security_architecture.md)
- [HITL Governance](security/hitl_governance.md)
- [Verification Triad](security/verification_triad.md)
- [Compliance & Audit](security/compliance_audit.md)

## 📖 Operations & Quality

- [User Manual](operations/user_manual.md)
- [Production Operations](operations/production_operations.md)
- [Experiment Logs](operations/experiment_logs.md)
- [Test Plan & Report](quality/test_plan_report.md)

## 📦 Source Modules (1:1 Mirror)

### Package Root
- [__init__.md](modules/regression_model_template/__init__.md)
- [__main__.md](modules/regression_model_template/__main__.md)
- [init_data.md](modules/regression_model_template/init_data.md)
- [scripts.md](modules/regression_model_template/scripts.md)
- [settings.md](modules/regression_model_template/settings.md)

### controller
- [controller/__init__.md](modules/regression_model_template/controller/__init__.md)
- [kafka_app.md](modules/regression_model_template/controller/kafka_app.md)

### core (Domain)
- [core/__init__.md](modules/regression_model_template/core/__init__.md)
- [metrics.md](modules/regression_model_template/core/metrics.md)
- [models.md](modules/regression_model_template/core/models.md)
- [schemas.md](modules/regression_model_template/core/schemas.md)

### io (Infrastructure & I/O)
- [io/__init__.md](modules/regression_model_template/io/__init__.md)
- [configs.md](modules/regression_model_template/io/configs.md)
- [datasets.md](modules/regression_model_template/io/datasets.md)
- [osvariables.md](modules/regression_model_template/io/osvariables.md)
- [registries.md](modules/regression_model_template/io/registries.md)
- [services.md](modules/regression_model_template/io/services.md)

### jobs (Lifecycle Stages)
- [jobs/__init__.md](modules/regression_model_template/jobs/__init__.md)
- [base.md](modules/regression_model_template/jobs/base.md)
- [evaluations.md](modules/regression_model_template/jobs/evaluations.md)
- [explanations.md](modules/regression_model_template/jobs/explanations.md)
- [inference.md](modules/regression_model_template/jobs/inference.md)
- [promotion.md](modules/regression_model_template/jobs/promotion.md)
- [training.md](modules/regression_model_template/jobs/training.md)
- [tuning.md](modules/regression_model_template/jobs/tuning.md)

### utils (Utilities)
- [utils/__init__.md](modules/regression_model_template/utils/__init__.md)
- [searchers.md](modules/regression_model_template/utils/searchers.md)
- [signers.md](modules/regression_model_template/utils/signers.md)
- [splitters.md](modules/regression_model_template/utils/splitters.md)
