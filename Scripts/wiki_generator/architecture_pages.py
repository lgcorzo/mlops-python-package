from .config import make_frontmatter

def get_business_context_md():
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ContextView",
        concept_type="architecture",
        title="Business Context & Machine Learning Lifecycle",
        description="ISO 42010 ContextView / ISO 15289 Description documentation for the business rationale, ROI model, and MLOps lifecycle.",
        tags=["iso42010", "okf", "context_view", "business", "mlops"]
    )
    return fm + "\n\n" + """# Business Context & Machine Learning Lifecycle

> **Purpose**: Define the business rationale, return on investment (ROI), operational key performance indicators (KPIs), and lifecycle stages for the MLOps regression template.

---

## 1. Problem Statement & Value Proposition

Machine learning models deployed in production environments often suffer from **silent degradation**, **unreproducible experiments**, **schema mismatch vulnerabilities**, and **uncontrolled deployment drift**.

The `mlops-python-package` delivers an enterprise architecture that addresses these operational risks through:

1. **Deterministic Data Contracts**: Compile-time and runtime validation of all input features and target labels via Pandera and Pydantic v2.
2. **Auditable Experiment Lifecycle**: Comprehensive tracking of code versions, hyperparameter configurations, metrics, and model artifacts via MLflow.
3. **Decoupled Architecture**: Strict separation of core mathematical concepts (`core/`) from input/output mechanics (`io/`), operational jobs (`jobs/`), and streaming controllers (`controller/`).
4. **Governed Model Promotion**: Automated champion-challenger threshold evaluation before model artifact promotion to production aliases.
5. **Secure Serving**: High-throughput FastAPI endpoints with Kafka streaming integration, sliding-window rate limiting, and cryptographic payload signing.

---

## 2. ROI & Operational KPIs

| Metric | Target | Measurement Mechanism |
|:---|:---|:---|
| **Pipeline Reproducibility** | 100% | DVC pipeline execution & MLflow parameter tracking |
| **Schema Validation Coverage** | 100% | Pandera DataFrameModel validation at service boundaries |
| **Inference Latency** | < 15ms p99 | FastAPI async endpoint & Kafka batch streaming |
| **Test Suite Coverage** | ≥ 95% | 29 Pytest suites executed via CI/CD |
| **Audit Provenance** | 100% | Cryptographic SHA-256 signature via `InferSigner` |

---

## 3. The 6-Stage MLOps Lifecycle

```mermaid
flowchart LR
    A["1. Data Ingestion\n(Parquet / DVC)"] --> B["2. Model Training\n(Scikit-Learn Baseline)"]
    B --> C["3. Hyperparameter Tuning\n(Optuna / Grid)"]
    C --> D["4. Evaluation & XAI\n(Metrics & SHAP)"]
    D --> E["5. Promotion Gate\n(Champion vs Challenger)"]
    E --> F["6. Serving & Streaming\n(FastAPI / Kafka)"]

    classDef stage fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    class A,B,C,D,E,F stage;
```

1. **Data Ingestion**: Standardized reading of Parquet files via `ParquetReader` with lineage metadata.
2. **Model Training**: Executed by `TrainingJob`, fitting an extensible `Model` implementation.
3. **Hyperparameter Tuning**: Executed by `TuningJob`, optimizing hyperparameters over defined search spaces via Optuna.
4. **Evaluation & Explainability**: Executed by `EvaluationsJob` (evaluating against baseline thresholds) and `ExplanationsJob` (generating global and local SHAP feature attributions).
5. **Promotion Gate**: Executed by `PromotionJob`, validating challenger metrics against active production champion aliases.
6. **Production Serving**: Real-time batch and event-driven prediction serving via `FastAPIKafkaService`.

---

> *Related: [Strategic Design](strategic_design.md) · [Tactical Design](tactical_design.md) · [Master Index](../index.md)*
"""

def get_strategic_design_md():
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ContextView",
        concept_type="architecture",
        title="Strategic Design & Onion Architecture",
        description="ISO 42010 ContextView / ISO 15289 Description documentation for the system context, C4 levels 1-2, and Onion Architecture layers.",
        tags=["iso42010", "okf", "context_view", "c4", "onion_architecture"]
    )
    return fm + "\n\n" + """# Strategic Design & Onion Architecture

> **Purpose**: Detail the system boundary, high-level context, container interactions, and Onion Architecture layering of the MLOps Python Package.

---

## 1. C4 Level 1: System Context Diagram

```mermaid
C4Context
    title System Context Diagram — MLOps Python Package

    Person(data_scientist, "Data Scientist", "Trains, tunes, and evaluates regression models.")
    Person(operator, "MLOps / Platform Engineer", "Deploys, monitors, and operates streaming services.")
    System(mlops_pkg, "MLOps Python Package", "Executes end-to-end regression workflows, schema verification, and streaming inference.")

    System_Ext(mlflow_srv, "MLflow Tracking Server", "Centralized metric tracking and model artifact registry.")
    System_Ext(kafka_cluster, "Confluent Kafka Cluster", "Distributed event bus for incoming prediction events and results.")
    System_Ext(s3_store, "Object Storage (MinIO / S3)", "Stores raw Parquet data, processed datasets, and model binaries.")

    Rel(data_scientist, mlops_pkg, "Executes CLI jobs via", "Invoke / Python -m")
    Rel(operator, mlops_pkg, "Monitors health & streams via", "HTTP / Prometheus")
    Rel(mlops_pkg, mlflow_srv, "Logs runs & registers models", "REST API")
    Rel(mlops_pkg, kafka_cluster, "Consumes & Publishes events", "Kafka TCP")
    Rel(mlops_pkg, s3_store, "Reads/Writes Parquet files", "S3 / DVC")
```

---

## 2. C4 Level 2: Container Diagram

```mermaid
C4Container
    title Container Diagram — Internal Subsystems

    Container(core, "Core Domain", "Python / Pandera / Scikit-Learn", "Encapsulates mathematical abstractions: Model, Metric, Schemas.")
    Container(jobs, "Lifecycle Jobs", "Python / Pydantic", "Executes BaseJob, TrainingJob, TuningJob, EvaluationsJob, InferenceJob, PromotionJob.")
    Container(io, "IO Adapters", "Python / OmegaConf / Parquet", "Handles Datasets, Configs, Registries, OSVariables, Services.")
    Container(controller, "Streaming Controller", "FastAPI / Confluent Kafka", "Handles REST prediction endpoints and Kafka event consumers.")
    Container(utils, "Utilities", "Python / Optuna / SHA-256", "Provides Searchers, Signers, and Splitters.")

    Rel(jobs, core, "Uses mathematical abstractions", "Python Import")
    Rel(jobs, io, "Reads datasets & logs runs", "Service Context")
    Rel(jobs, utils, "Applies hyperparameter search & splitting", "Helper Call")
    Rel(controller, core, "Validates payloads against schemas", "Pandera Check")
    Rel(controller, io, "Loads models from registry", "Loader Adapter")
```

---

## 3. Onion Architecture Layers

The repository strictly enforces dependency inversion. Inner domain layers remain pure and completely oblivious to outer framework and infrastructure layers:

```mermaid
graph TD
    subgraph L4["Layer 4: Interface & Controllers"]
        CTRL["controller/kafka_app.py\nscripts.py\n__main__.py"]
    end
    subgraph L3["Layer 3: Infrastructure & Adapters"]
        IO["io/services.py (MLflow, Alerts)\nio/registries.py\nio/datasets.py\nio/configs.py"]
    end
    subgraph L2["Layer 2: Application Lifecycle Jobs"]
        JOBS["jobs/base.py\njobs/training.py\njobs/tuning.py\njobs/evaluations.py\njobs/inference.py\njobs/promotion.py"]
    end
    subgraph L1["Layer 1: Core Domain (Pure Mathematics)"]
        CORE["core/models.py (Model, BaselineSklearnModel)\ncore/metrics.py (Metric, SklearnMetric)\ncore/schemas.py (Pandera DataFrameModels)"]
    end

    CTRL --> IO
    CTRL --> JOBS
    IO --> CORE
    JOBS --> CORE
    JOBS --> IO

    classDef l1 fill:#312e81,stroke:#818cf8,stroke-width:2px,color:#f8fafc;
    classDef l2 fill:#1e3a5f,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef l3 fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#f8fafc;
    classDef l4 fill:#701a75,stroke:#f472b6,stroke-width:2px,color:#f8fafc;

    class CORE l1;
    class JOBS l2;
    class IO l3;
    class CTRL l4;
```

1. **Domain Layer (`core/`)**: Completely independent of database, framework, or network details. Defines abstract mathematical contracts for predictive estimators (`Model`), loss/scoring functions (`Metric`), and tabular structures (`Schema`).
2. **Application Layer (`jobs/`)**: Implements operational use cases. Each job subclasses `Job` (`jobs/base.py`), managing the setup, execution, and teardown lifecycle of distinct workflows.
3. **Infrastructure Layer (`io/`)**: Implements technology-specific adapters for external platforms, including MLflow tracking, OmegaConf YAML parsing, and Parquet file I/O.
4. **Interface Layer (`controller/`)**: Exposes streaming endpoints via Kafka and synchronous REST endpoints via FastAPI.

---

> *Related: [Tactical Design](tactical_design.md) · [Runtime Sequences](runtime_sequences.md) · [Master Index](../index.md)*
"""

def get_tactical_design_md():
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ComponentView",
        concept_type="architecture",
        title="Tactical Design & Design Patterns",
        description="ISO 42010 ComponentView / ISO 15289 Description documentation for micro-architecture, C4 Level 3 component breakdown, and design patterns.",
        tags=["iso42010", "okf", "component_view", "design_patterns", "uml"]
    )
    return fm + "\n\n" + """# Tactical Design & Design Patterns

> **Purpose**: Detail the micro-architectural design, design patterns, and C4 Level 3 component interactions across the codebase.

---

## 1. C4 Level 3: Component Diagram

```mermaid
classDiagram
    direction TB

    class Model {
        <<abstract>>
        +fit(inputs, targets) Model*
        +predict(inputs) Outputs*
        +explain_model() FeatureImportances*
        +explain_samples(inputs) SHAPValues*
    }

    class BaselineSklearnModel {
        +int max_depth
        +int n_estimators
        +Pipeline _pipeline
        +fit(inputs, targets) BaselineSklearnModel
        +predict(inputs) Outputs
    }
    BaselineSklearnModel --|> Model : implements

    class Metric {
        <<abstract>>
        +score(targets, outputs) float*
        +scorer(model, inputs, targets) float
        +to_mlflow() MlflowMetric
    }

    class SklearnMetric {
        +score(targets, outputs) float
    }
    SklearnMetric --|> Metric : implements

    class Job {
        <<abstract>>
        +LoggerService logger_service
        +AlertsService alerts_service
        +MlflowService mlflow_service
        +__enter__() Self
        +__exit__() bool
        +run() Locals*
    }

    class TrainingJob {
        +RunConfig run_config
        +ReaderKind inputs
        +ReaderKind targets
        +ModelKind model
        +run() Locals
    }
    TrainingJob --|> Job : implements

    class Reader {
        <<abstract>>
        +read() DataFrame*
        +lineage() Lineage*
    }
    class ParquetReader {
        +str path
        +read() DataFrame
    }
    ParquetReader --|> Reader : implements

    class Splitter {
        <<abstract>>
        +split(inputs, targets) TrainTestSplits*
        +get_n_splits(inputs, targets) int*
    }
    class TimeSeriesSplitter {
        +int gap
        +int n_splits
        +split(inputs, targets) TrainTestSplits
    }
    TimeSeriesSplitter --|> Splitter : implements

    TrainingJob --> Model : trains
    TrainingJob --> Reader : reads inputs
    TrainingJob --> Splitter : splits dataset
```

---

## 2. Design Patterns in Action

### 1. Strategy Pattern
The Strategy pattern defines interchangeable algorithm families:
- **Models (`core/models.py`)**: Client code in `jobs/training.py` or `jobs/inference.py` consumes the abstract `Model` interface. Any estimator (Random Forest, Gradient Boosting, Deep Neural Network) can be substituted transparently.
- **Metrics (`core/metrics.py`)**: Metrics (`MSE`, `MAE`, `R2`) implement the `Metric` interface, providing unified scoring and MLflow threshold export.
- **Splitters (`utils/splitters.py`)**: `TrainTestSplitter` and `TimeSeriesSplitter` encapsulate distinct cross-validation partitioning algorithms.
- **Readers & Writers (`io/datasets.py`)**: `ParquetReader` and `ParquetWriter` isolate specific tabular serialization logic.

### 2. Context Manager / Template Method Pattern
The `Job` base class (`jobs/base.py`) implements the Python context manager protocol (`__enter__` and `__exit__`):
- `__enter__`: Automatically initializes `LoggerService`, `AlertsService`, and `MlflowService`.
- `__exit__`: Manages clean teardown, logs execution duration, and broadcasts failure notifications if unhandled exceptions occur.
- `run()`: The template method overridden by concrete jobs (`TrainingJob`, `TuningJob`, etc.).

### 3. Singleton Pattern
The `Singleton` metaclass in `io/osvariables.py` ensures that runtime environment settings (`Env`) are parsed exactly once from `.env` files and shared immutably across all worker threads.

---

> *Related: [Strategic Design](strategic_design.md) · [Data Model](mission_data_model.md) · [Master Index](../index.md)*
"""

def get_agent_specifications_md():
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="architecture",
        title="Lifecycle Job Specifications & Contracts",
        description="ISO 42010 ComponentView / ISO 15289 Specification documentation detailing the functional contracts of all 6 MLOps lifecycle jobs.",
        tags=["iso42010", "okf", "component_view", "specification", "jobs"]
    )
    return fm + "\n\n" + """# Lifecycle Job Specifications & Contracts

> **Purpose**: Formal specification of the inputs, outputs, execution logic, and error behaviors for all 6 operational jobs in `jobs/`.

---

## 1. Unified Job Matrix

| Job Name | Module Source | Primary Responsibility | Key Inputs | Primary Outputs |
| :--- | :--- | :--- | :--- | :--- |
| **`TrainingJob`** | `jobs/training.py` | Model training & artifact logging | Raw Parquet datasets, model config | Trained model, MLflow run, metrics |
| **`TuningJob`** | `jobs/tuning.py` | Hyperparameter optimization | Search space grid, metric objective | Best parameters, trial metrics |
| **`EvaluationsJob`** | `jobs/evaluations.py` | Validation against threshold gates | Test inputs, targets, model alias | Evaluation report, threshold pass/fail |
| **`ExplanationsJob`** | `jobs/explanations.py` | SHAP interpretability extraction | Sample inputs, registered model | Global importance & sample SHAP values |
| **`InferenceJob`** | `jobs/inference.py` | Batch prediction & cryptographic signing | Unlabeled inputs, model version | Output predictions, SHA-256 signature |
| **`PromotionJob`** | `jobs/promotion.py` | Champion-challenger alias promotion | Candidate model version, target alias | Updated MLflow model alias tag |

---

## 2. Detailed Job Contracts

### `TrainingJob` (`jobs/training.py`)
- **Inputs**: `inputs` (`ParquetReader`), `targets` (`ParquetReader`), `model` (`ModelKind`), `run_config` (`RunConfig`).
- **Execution Flow**:
  1. Reads `inputs` and `targets` DataFrames and validates against Pandera schemas.
  2. Partitions data using the configured `Splitter`.
  3. Fits the underlying `Model` on train splits.
  4. Computes train and test evaluation metrics.
  5. Logs parameters, metrics, and serialized model artifact to active MLflow run.
- **Exceptions**: `pandera.errors.SchemaError`, `FileNotFoundError`.

### `TuningJob` (`jobs/tuning.py`)
- **Inputs**: `inputs`, `targets`, `model`, `searcher` (`OptunaSearcher` / `GridCVSearcher`), `metric`.
- **Execution Flow**:
  1. Orchestrates cross-validated hyperparameter trials over parameter grids.
  2. Evaluates scoring metrics on validation folds.
  3. Records trial histories and identifies optimal hyperparameter set.
  4. Logs best parameters and trials dataframe to MLflow.

### `EvaluationsJob` (`jobs/evaluations.py`)
- **Inputs**: `inputs`, `targets`, `model_type`, `run_config`.
- **Execution Flow**:
  1. Ingests evaluation test splits.
  2. Generates predictions using designated model artifact.
  3. Evaluates all configured metrics (`RegressionMetricsEnum`).
  4. Compares results against predefined `Threshold` constraints.

### `ExplanationsJob` (`jobs/explanations.py`)
- **Inputs**: `inputs_samples`, `models_explanations`, `samples_explanations`, `alias_or_version`.
- **Execution Flow**:
  1. Instantiates `shap.TreeExplainer` over model tree estimators.
  2. Calculates global mean absolute SHAP feature importances.
  3. Computes local SHAP attribution values per input sample.
  4. Writes outputs to Parquet datasets matching `SHAPValuesSchema` and `FeatureImportancesSchema`.

### `InferenceJob` (`jobs/inference.py`)
- **Inputs**: `inputs` (`ReaderKind`), `outputs` (`WriterKind`), `loader` (`LoaderKind`), `alias_or_version`.
- **Execution Flow**:
  1. Loads model artifact via `Loader` adapter.
  2. Validates incoming tabular input against `InputsSchema`.
  3. Generates prediction outputs matching `OutputsSchema`.
  4. Signs input-output bundle using `InferSigner` and writes result to destination storage.

### `PromotionJob` (`jobs/promotion.py`)
- **Inputs**: `alias` (`str`), `version` (`int | None`).
- **Execution Flow**:
  1. Queries MLflow Model Registry for the specified registered model.
  2. Validates that candidate model passed all evaluation criteria.
  3. Re-assigns designated model alias (e.g. `champion`) to target version.

---

> *Related: [Runtime Sequences](runtime_sequences.md) · [Tactical Design](tactical_design.md) · [Master Index](../index.md)*
"""

def get_runtime_sequences_md():
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="SequenceView",
        concept_type="architecture",
        title="Runtime Sequences & Execution Flows",
        description="ISO 42010 SequenceView / ISO 15289 Specification documentation providing comprehensive Mermaid sequence diagrams for all pipelines.",
        tags=["iso42010", "okf", "sequence_view", "mermaid", "runtime"]
    )
    return fm + "\n\n" + """# Runtime Sequences & Execution Flows

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
"""

def get_infrastructure_adapters_md():
    fm = make_frontmatter(
        doc_type="Description",
        viewpoint="ComponentView",
        concept_type="architecture",
        title="Infrastructure Adapters & Platform Integrations",
        description="ISO 42010 ComponentView / ISO 15289 Description documentation detailing external platform adapters in io/ and controller/.",
        tags=["iso42010", "okf", "component_view", "infrastructure", "adapters"]
    )
    return fm + "\n\n" + """# Infrastructure Adapters & Platform Integrations

> **Purpose**: Document external connectivity adapters, storage systems, message brokers, and telemetry backends.

---

## 1. External Infrastructure Topology

```mermaid
graph LR
    subgraph CoreApp["MLOps Python Package"]
        IO_SRV["io/services.py"]
        IO_REG["io/registries.py"]
        IO_DATA["io/datasets.py"]
        CTRL["controller/kafka_app.py"]
    end

    subgraph ExternalServices["External Infrastructure Platforms"]
        MLFLOW[("MLflow Tracking & Registry")]
        KAFKA{"Confluent Kafka Broker"}
        S3[("MinIO / S3 Object Store")]
        DVC["Data Version Control (DVC)"]
        NOTIF["Notification Gateway (Alerts)"]
    end

    IO_SRV -->|Tracking URI & REST API| MLFLOW
    IO_REG -->|Model Registry API| MLFLOW
    IO_DATA -->|Parquet Read/Write| S3
    IO_DATA -->|Pointers & Metadata| DVC
    CTRL -->|TCP 9092 & Consumer Groups| KAFKA
    IO_SRV -->|Desktop / Webhook Alerts| NOTIF

    classDef core fill:#1e293b,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef ext fill:#111827,stroke:#34d399,stroke-width:2px,color:#f8fafc;
    class IO_SRV,IO_REG,IO_DATA,CTRL core;
    class MLFLOW,KAFKA,S3,DVC,NOTIF ext;
```

---

## 2. Infrastructure Adapters Breakdown

### 1. MLflow Tracking & Registry (`io/services.py`, `io/registries.py`)
- **Protocol**: HTTP/REST and Python MLflow Client (`mlflow.tracking.MlflowClient`).
- **Configuration**: Injected via `osvariables.py` (`MLFLOW_TRACKING_URI`, `MLFLOW_REGISTRY_URI`).
- **Features**: Experiment isolation, metric logging (`MSE`, `RMSE`, `R2`), artifact versioning, and champion-challenger alias assignment.

### 2. Parquet Storage & DVC Integration (`io/datasets.py`)
- **Format**: Apache Parquet columnar binary with snappy compression.
- **Implementations**:
  - `ParquetReader`: Enforces optional row limits and extracts dataset lineage metadata.
  - `ParquetWriter`: Atomically writes DataFrames to persistent storage.
- **DVC Sync**: Datasets in `data/` are tracked using `.dvc` sidecar files committed to Git.

### 3. Kafka Streaming Broker (`controller/kafka_app.py`)
- **Client**: `confluent-kafka` (C-optimized `librdkafka` bindings).
- **Topology**: Input topic for incoming JSON requests; output topic for prediction responses.
- **Resilience**: Consumer poll loop with automatic partition assignment, graceful shutdown handlers, and error recovery.

### 4. Logging & Alerting Services (`io/services.py`)
- **`LoggerService`**: Configures Loguru sinks with structured serialization and level filtering.
- **`AlertsService`**: Dispatches system notifications upon pipeline failures.

---

> *Related: [Tactical Design](tactical_design.md) · [Production Operations](../operations/production_operations.md) · [Master Index](../index.md)*
"""

def get_mission_data_model_md():
    fm = make_frontmatter(
        doc_type="Specification",
        viewpoint="ComponentView",
        concept_type="architecture",
        title="Mission Data Model & Schema Contracts",
        description="ISO 42010 ComponentView / ISO 15289 Specification documentation detailing Pandera schemas, Pydantic contracts, and serialization protocols.",
        tags=["iso42010", "okf", "component_view", "schemas", "data_contracts"]
    )
    return fm + "\n\n" + """# Mission Data Model & Schema Contracts

> **Purpose**: Formal definition of tabular data contracts, feature schemas, prediction structures, and configuration schemas.

---

## 1. Pandera Tabular Schemas (`core/schemas.py`)

Every tabular dataset passing through a pipeline boundary is validated against strict Pandera `DataFrameModel` definitions:

```mermaid
classDiagram
    direction TB

    class Schema {
        +check(data: DataFrame) DataFrame$
    }

    class InputsSchema {
        +UInt32 instant (Index)
        +DateTime dteday
        +UInt8 season
        +UInt8 yr
        +UInt8 mnth
        +UInt8 hr
        +UInt8 holiday
        +UInt8 weekday
        +UInt8 workingday
        +UInt8 weathersit
        +float temp
        +float atemp
        +float hum
        +float windspeed
    }
    InputsSchema --|> Schema : inherits

    class TargetsSchema {
        +UInt32 instant (Index)
        +UInt32 cnt
    }
    TargetsSchema --|> Schema : inherits

    class OutputsSchema {
        +UInt32 instant (Index)
        +UInt32 prediction
    }
    OutputsSchema --|> Schema : inherits

    class FeatureImportancesSchema {
        +str feature
        +float importance
    }
    FeatureImportancesSchema --|> Schema : inherits

    class SHAPValuesSchema {
        +float base_values
        +float values
    }
    SHAPValuesSchema --|> Schema : inherits
```

---

## 2. API & Streaming Payloads (`controller/kafka_app.py`)

### `PredictionRequest`
Encapsulates an incoming payload submitted via HTTP POST `/predict` or consumed from Kafka:
```json
{
  "input_data": {
    "instant": [1],
    "dteday": ["2011-01-01 00:00:00"],
    "season": [1],
    "yr": [0],
    "mnth": [1],
    "hr": [0],
    "holiday": [0],
    "weekday": [6],
    "workingday": [0],
    "weathersit": [1],
    "temp": [0.24],
    "atemp": [0.2879],
    "hum": [0.81],
    "windspeed": [0.0]
  }
}
```

### `PredictionResponse`
Encapsulates the predicted target value returned to the client:
```json
{
  "result": {
    "prediction": [16]
  }
}
```

---

## 3. Cryptographic Signature Payload (`utils/signers.py`)

The `InferSigner` generates a SHA-256 hash attesting to prediction inputs and outputs:
```text
Signature: 8f9b3e1c2a4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f
```

---

> *Related: [Security Architecture](../security/security_architecture.md) · [Core Schemas](../modules/regression_model_template/core/schemas.md) · [Master Index](../index.md)*
"""
