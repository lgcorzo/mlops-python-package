---
iso_doc_type: "Specification"
iso_viewpoint: "SequenceView"
type: "architecture"
title: "Runtime Sequences & Execution Flows"
description: "ISO 42010 SequenceView / ISO 15289 Specification documentation providing comprehensive Mermaid sequence diagrams for all pipelines."
tags: ["iso42010", "okf", "sequence_view", "mermaid", "runtime"]
timestamp: "2026-10-01T17:50:00Z"
generated: "agent:wiki-iso-documentation-standard"
verified: "true"
last_verified_commit: "073b5fd"
---

# Runtime Sequences & Execution Flows

> **Purpose**: Sequence diagrams illustrating the runtime interactions, message passing, and lifecycle flows across batch jobs and real-time streaming services.

---

## 1. Sequence 1: Batch Model Training & Registration

```mermaid
sequenceDiagram
    autonumber
    actor DS as Data Scientist
    participant TJ as TrainingJob
    participant PR as ParquetReader
    participant SCH as Pandera Schema
    participant MDL as BaselineSklearnModel
    participant MLF as MLflow Service
    participant S3 as Storage / Artifacts

    DS->>TJ: run()
    activate TJ
    TJ->>MLF: start_run(run_config)
    TJ->>PR: read(inputs_path)
    PR-->>TJ: raw_inputs_df
    TJ->>SCH: check(raw_inputs_df)
    SCH-->>TJ: validated_inputs
    TJ->>MDL: fit(validated_inputs, targets)
    activate MDL
    MDL-->>TJ: fitted_model
    deactivate MDL
    TJ->>MDL: predict(test_inputs)
    MDL-->>TJ: predictions
    TJ->>MLF: log_metrics(mse, rmse, r2)
    TJ->>MLF: log_model(fitted_model, artifact_path="model")
    MLF->>S3: save_artifact()
    TJ->>MLF: end_run()
    TJ-->>DS: Locals(model, metrics, run_id)
    deactivate TJ
```

---

## 2. Sequence 2: Hyperparameter Tuning Flow

```mermaid
sequenceDiagram
    autonumber
    actor DS as Data Scientist
    participant TU as TuningJob
    participant SRCH as OptunaSearcher
    participant SPLT as TimeSeriesSplitter
    participant MDL as Model
    participant MLF as MLflow Service

    DS->>TU: run()
    activate TU
    TU->>MLF: start_run("tuning_experiment")
    TU->>SRCH: search(model, metric, inputs, targets, cv=SPLT)
    activate SRCH
    loop For each hyperparameter trial
        SRCH->>SPLT: split(inputs, targets)
        SPLT-->>SRCH: train_fold, val_fold
        SRCH->>MDL: fit(train_fold)
        SRCH->>MDL: predict(val_fold)
        SRCH->>MLF: log_metric("trial_score", score)
    end
    SRCH-->>TU: Results(best_params, best_score)
    deactivate SRCH
    TU->>MLF: log_params(best_params)
    TU->>MLF: end_run()
    TU-->>DS: Locals(best_params)
    deactivate TU
```

---

## 3. Sequence 3: Model Evaluation & Champion Promotion Gate

```mermaid
sequenceDiagram
    autonumber
    actor Auditor as MLOps Engineer / Auditor
    participant PJ as PromotionJob
    participant REG as MlflowModelRegistry
    participant MLF as MLflow Client

    Auditor->>PJ: run(alias="champion", version=3)
    activate PJ
    PJ->>REG: get_model_version(name, version=3)
    REG-->>PJ: model_version_details
    PJ->>MLF: get_run(run_id)
    MLF-->>PJ: run_metrics (MSE, RMSE, R2)
    alt Candidate metrics meet promotion threshold
        PJ->>REG: set_model_alias(name, alias="champion", version=3)
        REG-->>PJ: Success
        PJ-->>Auditor: Model v3 successfully promoted to Champion
    else Threshold check fails
        PJ-->>Auditor: Promotion Rejected (Threshold criteria not met)
    end
    deactivate PJ
```

---

## 4. Sequence 4: Real-Time Kafka Streaming & Prediction Service

```mermaid
sequenceDiagram
    autonumber
    actor Client as External Client / Producer
    participant KAFKA as Kafka Input Topic
    participant APP as FastAPIKafkaService
    participant RL as RateLimiter
    participant SCH as Pandera Schema
    participant PRED as PredictionService
    participant OUT as Kafka Output Topic

    Client->>KAFKA: Produce Prediction Event
    KAFKA->>APP: _poll_message()
    activate APP
    APP->>RL: is_allowed(client_ip)
    alt Rate limit exceeded
        APP->>APP: Log warning & drop event
    else Request allowed
        APP->>SCH: check(input_payload)
        alt Valid payload
            SCH-->>APP: validated_df
            APP->>PRED: predict(validated_df)
            PRED-->>APP: prediction_response
            APP->>OUT: produce(output_topic, prediction_response)
            OUT-->>Client: Receive Prediction Result
        else Schema validation error
            APP->>APP: Route to Dead Letter Queue (DLQ)
        end
    end
    deactivate APP
```

---

> *Related: [Agent Specifications](agent_specifications.md) · [Tactical Design](tactical_design.md) · [Master Index](../index.md)*
