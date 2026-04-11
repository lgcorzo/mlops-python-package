# US [Model Tuning Job](./backlog_mlops_regresion.md) : Perform hyperparameter tuning for a model. the best hyperparameters for a model

- [US Model Tuning Job : Define a job for finding the best hyperparameters for a model](#us-model-tuning-job--define-a-job-for-finding-the-best-hyperparameters-for-a-model)
  - [classes relations](#classes-relations)
  - [**User Stories: Tuning Job Management**](#user-stories-tuning-job-management)
    - [**1. User Story: Configure Tuning Job**](#1-user-story-configure-tuning-job)
    - [**2. User Story: Read Input and Target Data**](#2-user-story-read-input-and-target-data)
    - [**3. User Story: Log Data Lineage**](#3-user-story-log-data-lineage)
    - [**4. User Story: Run Hyperparameter Search**](#4-user-story-run-hyperparameter-search)
    - [**5. User Story: Identify Best Hyperparameters**](#5-user-story-identify-best-hyperparameters)
    - [**6. User Story: Notify Completion of Tuning**](#6-user-story-notify-completion-of-tuning)
    - [**Common Acceptance Criteria**](#common-acceptance-criteria)
    - [**Definition of Done (DoD):**](#definition-of-done-dod)
  - [Code location](#code-location)
  - [Test location](#test-location)

------------

## classes relations

```mermaid
classDiagram
    direction LR
    class TuningJob {
        +KIND: T.Literal["TuningJob"] = "TuningJob"
        +run_config: services.MlflowService.RunConfig
        +inputs: datasets.ReaderKind
        +targets: datasets.ReaderKind
        +model: models.ModelKind
        +metric: metrics.MetricKind
        +splitter: splitters.SplitterKind
        +searcher: searchers.SearcherKind
        +run() base.Locals
    }

    class Job {
        <<abstract>>
        +run()* base.Locals
    }
    TuningJob --|> Job : inherits

    class MlflowService {
        +client() mt.MlflowClient
        +run_context(run_config) RunContext
        +registry_name: str
    }

    class ReaderKind {
        <<interface>>
        +read() pd.DataFrame
        +lineage(data, name, targets) mt.Dataset
    }

    class ModelKind {
        <<interface>>
        +fit(inputs, targets)
        +predict(inputs) pd.DataFrame
    }

    class MetricKind {
        <<interface>>
        +score(targets, outputs) float
    }

    class SplitterKind {
        <<interface>>
        +split(inputs, targets) Iterator
    }

    class SearcherKind {
        <<interface>>
        +search(model, metric, inputs, targets, cv) Results
    }

    TuningJob --> MlflowService : "uses"
    TuningJob --> ReaderKind : "uses"
    TuningJob --> ModelKind : "uses"
    TuningJob --> MetricKind : "uses"
    TuningJob --> SplitterKind : "uses"
    TuningJob --> SearcherKind : "uses"
```

## **User Stories: Tuning Job Management**

---

### **1. User Story: Configure Tuning Job**

**Title:**  
As a **data scientist**, I want to configure a tuning job with the required parameters for hyperparameter optimization, so that I can effectively manage the hyperparameter tuning process.

**Description:**  
The `TuningJob` class allows the setup of parameters such as input data readers, target data readers, the model to be tuned, the metric to be optimized, and the hyperparameter search strategy.

**Acceptance Criteria:**  

- The job can be initialized with all the necessary parameters.
- Default values are properly configured for optional parameters.

---

### **2. User Story: Read Input and Target Data**

**Title:**  
As a **data engineer**, I want to read input and target datasets from specified sources, so that I can prepare them for hyperparameter tuning.

**Description:**  
In the `run` method, input and target data are read using the designated data readers, and the integrity of this data is validated.

**Acceptance Criteria:**  

- The job successfully reads and validates input and target datasets.
- The shapes of the datasets are logged for monitoring purposes.

------------

### **3. User Story: Log Data Lineage**

**Title:**  
As a **compliance officer**, I want to log the lineage of input and target datasets used in the tuning job, so that we are able to trace the data in model tuning for auditing.

**Description:**  
Lineage information is logged in MLflow for both input and target datasets used in the hyperparameter tuning process.

**Acceptance Criteria:**  

- The lineage of both the input and target datasets is logged appropriately using the MLflow tracking system.
- Logged lineage includes sufficient details to trace the origin of the data.

------------

### **4. User Story: Run Hyperparameter Search**

**Title:**  
As a **data scientist**, I want to execute a hyperparameter search using the specified searcher, so that I can find the best hyperparameters for the model.

**Description:**  
The job invokes the hyperparameter searcher to find optimal hyperparameters based on evaluation against the provided metric.

**Acceptance Criteria:**  

- The hyperparameter search is performed successfully using the configured searcher.
- Results from the search, including performance metrics, should be logged.

------------

### **5. User Story: Identify Best Hyperparameters**

**Title:**  
As a **data scientist**, I want to identify the best hyperparameters as part of the tuning process, so that I can use them for model training.

**Description:**  
The results of the hyperparameter search should include the best score and best parameters, which are then logged.

**Acceptance Criteria:**  

- The job captures and logs the best hyperparameters found and the associated performance score.
- This information should be available for review and future reference.

------------

### **6. User Story: Notify Completion of Tuning**

**Title:**  
As a **user**, I want to receive a notification when the tuning job is finished, so that I can review the tuning results promptly.

**Description:**  
At the conclusion of the job execution, the tuning job sends a notification detailing the completion of the process and the best score achieved.

**Acceptance Criteria:**  

- Notifications include information about the best hyperparameter score.
- The alerts service successfully communicates the tuning job's completion.

------------

### **Common Acceptance Criteria**

1. **Implementation Requirements:**
   - The `TuningJob` class correctly implements the run method defined in the base `Job` class.
   - Services (logging, MLflow, alerts) should be initialized correctly in the job.

2. **Error Handling:**
   - Clear error messages should be logged for any issues encountered during data reading, hyperparameter tuning, or logging steps.

3. **Testing:**
   - Unit tests validate job setup, data reading, hyperparameter search execution, and notification delivery.
   - Tests ensure effective handling of edge cases and error scenarios.

4. **Documentation:**
   - Each method and class should feature comprehensive docstrings that describe their purpose and functionality.
   - Users should have access to clear examples for configuring and utilizing the tuning job.

---

### **Definition of Done (DoD):**

- The `TuningJob` class is fully implemented and operational as per the acceptance criteria.
- All functionalities are tested for accuracy and reliability.
- Documentation is complete, providing clear guidance for users.

## Code location

[src/regression_model_template/jobs/tuning.py](../src/regression_model_template/jobs/tuning.py)

## Test location

[tests/jobs/test_tuning.py](../tests/jobs/test_tuning.py)
