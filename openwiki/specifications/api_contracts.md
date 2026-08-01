---
iso_doc_type: "Specification"
iso_viewpoint: "ComponentView"
type: "specification"
title: "API & Interface Contracts"
description: "API Contracts detailing FastAPI REST endpoints, JSON validation schemas, and Kafka topic payload interfaces."
tags: ["iso15289", "specifications", "api", "rest", "kafka"]
timestamp: "2026-08-01T09:57:53Z"
generated: "agent:uml2-okf-documenter"
verified: "true"
last_verified_commit: "8f9670a"
---

# API & Interface Contracts: mlops-python-package

This document specifies the contracts for the external HTTP REST API endpoints and Kafka messaging topics.

## 1. REST HTTP API Contracts

The API runs by default on port `8100`.

### POST `/predict`
Submit input feature datasets to generate model predictions.

* **Headers:**
  - `Content-Type: application/json`
* **Request Payload Example (`PredictionRequest`):**
```json
{
  "input_data": {
    "dteday": ["2026-08-01", "2026-08-01"],
    "season": [1, 1],
    "yr": [0, 0],
    "mnth": [1, 1],
    "hr": [0, 12],
    "holiday": [false, false],
    "weekday": [6, 6],
    "workingday": [true, true],
    "weathersit": [1, 1],
    "temp": [0.5, 0.6],
    "atemp": [0.5, 0.6],
    "hum": [0.5, 0.5],
    "windspeed": [0.2, 0.2],
    "casual": [10, 20],
    "registered": [100, 200]
  }
}
```
* **Response Payload Example (`PredictionResponse`):**
```json
{
  "result": {
    "inference": [110.0, 220.0],
    "quality": 1.0,
    "error": null
  }
}
```

### GET `/health`
Check service status.
* **Response:**
```json
{
  "status": "healthy"
}
```

---

## 2. Kafka Topic Message Contracts

### Input Topic: `input_topic`
Consumes feature payloads.
* **Payload:** JSON-serialized string bytes matching the `input_data` dictionary structure in `PredictionRequest`.

### Output Topic: `output_topic`
Produces inference outputs.
* **Payload:** JSON-serialized string bytes matching the `result` dictionary structure in `PredictionResponse`.
