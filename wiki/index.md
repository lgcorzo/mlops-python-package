# Index of MLOps Python Package Wiki 🗂️

Welcome to the Open Knowledge Format (OKF) directory index for the MLOps Python Package. This index supports progressive disclosure, enabling humans and AI agents to discover available concept and story documents before traversing the repository.

## 🧭 Main Pages

- **[Home](Home)**: The central landing page describing system architecture, design patterns, context manager lifecycle, polymorphic discriminators, and design methodologies.
- **[Backlog Overview](backlog_mlops_regresion)**: Unified product roadmap and user story backlog for class diagram implementations.

## 🧠 Core Domain Concepts & User Stories

- **[Models User Story](Models_stories)**: Standardizing base ML models, configurations, and baseline RandomForest wrappers via scikit-learn.
- **[Metrics User Story](Metrics_stories)**: Unified metrics evaluation schemas and wrappers around standard scikit-learn performance statistics.
- **[Schemas User Story](Schemas_stories)**: Data validation contracts for inputs, targets, outputs, and feature importances using Pandera and Pydantic.

## 📥 Infrastructure, IO, and Environments

- **[Configs User Story](Configs_stories)**: YAML and OmegaConf based hyperparameter and setting loading logic.
- **[Datasetes User Story](Datasets_stories)**: IO mechanics for abstract and concrete readers/writers (such as ParquetReader and ParquetWriter).
- **[OSVariables User Story](OSvariables_stories)**: Pydantic settings singleton for secure loading of environment variables and MLflow configuration.
- **[Model Registries User Story](Regristries_stories)**: Interaction with artifacts stores and model deployment servers (MLflow registry).
- **[Services User Story](Services_stories)**: Orchestration and life cycle management of Logging, Alerts, and MLflow tracking systems.

## ⚙️ Orchestrated Workflows and Jobs

- **[High-Level Project Jobs User Story](Base_stories)**: The abstract `Job` class with built-in context manager for resource setup and teardown.
- **[Model Training Job User Story](Trainning_stories)**: Orchestrates fitting, tracking, and metric reporting for models.
- **[Model Tuning Job User Story](Tuning_stories)**: Evaluates hyperparameter spaces using splitters and searchers.
- **[Model Evaluations Job User Story](Evaluations_stories)**: Checks models against testing data and generates score reports.
- **[Model Explanations Job User Story](Explanations_stories)**: Produces global feature importances and local SHAP explanation values.
- **[Model Inference Job User Story](Inference_stories)**: Performs predictions over input files or batches.
- **[Promotions User Story](Promotions_stories)**: Implements candidate validation and promotion to production status.

## 🛠️ Auxiliary Tools & Utilities

- **[Hyperparameter Searchers User Story](Searchers_stories)**: Extensible strategy class for parameter search algorithms.
- **[Model Signature Generation User Story](Signers_stories)**: Generates deterministic structural signatures for input/output compatibility.
- **[Data Splitting Functionality User Story](Splitters_stories)**: Reproducible cross-validation and fold splitter interfaces.

---
*Generated in accordance with Open Knowledge Format (OKF) v0.1 guidelines.*

- [[kafka_app]]

## Source Code Documentation

- [[__main__]]
- [[base]]
- [[configs]]
- [[controller_init]]
- [[core_init]]
- [[datasets]]
- [[evaluations]]
- [[explanations]]
- [[inference]]
- [[io_init]]
- [[jobs_init]]
- [[kafka_app]]
- [[metrics]]
- [[models]]
- [[osvariables]]
- [[promotion]]
- [[registries]]
- [[regression_model_template_init]]
- [[schemas]]
- [[scripts]]
- [[searchers]]
- [[services]]
- [[settings]]
- [[signers]]
- [[splitters]]
- [[training]]
- [[tuning]]
- [[utils_init]]
