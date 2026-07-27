## 2026-04-18 - Synchronous Kafka Producer Flush in Message Loop
**Vulnerability:** Performance bottleneck and latency amplification from synchronous blocking network I/O in the core processing loop.
**Learning:** Re-flushing the confluent_kafka producer on every single message forces the application to block on round-trip network acknowledgment for every record, severely limiting throughput.
**Prevention:** Allow confluent_kafka to batch messages efficiently in memory by replacing `flush()` with a non-blocking `poll(0)` in the message processing loop, and calling `flush()` only during service shutdown to ensure graceful delivery of buffered messages.

## 2026-04-20 - Data Exposure in Kafka Consumer Result Logging
**Vulnerability:** Clear logging of raw prediction result which contains sensitive output data (e.g., list of inference values).
**Learning:** Logging entire prediction payloads at DEBUG level or any other level can expose sensitive inference outputs to log aggregation and monitoring systems, violating compliance and security standards.
**Prevention:** Avoid logging raw prediction output values. Instead, clone the dictionary and mask or summarize the sensitive prediction list (e.g., indicating the length of the list, such as `<masked_list_len_X>`) before passing it to the logger.

## 2026-07-27 - Automated Document Overwrites Without Differential Checking
**Vulnerability:** Widespread unintentional corruption and excessive churn in repository documentation when applying automated parsing updates.
**Learning:** Automatically writing to every markdown file without specifically filtering to files logically altered by git diffs violates "incremental update" policies and causes unnecessary build cycles and potential data loss on hand-curated sections.
**Prevention:** Strictly utilize source control diff mechanisms (`git diff`) to map changed code files directly to their corresponding documentation artifacts, avoiding sweeping directory writes.

## 2026-07-27 - Missing MLFlow PythonModel Predict Type Hints
**Vulnerability:** MyPy typing errors during CI evaluation of CustomSaver.Adapter.predict functions inside `src/regression_model_template/io/registries.py`.
**Learning:** When defining predict functions for MLflow PyFunc models in this codebase, type hints must either be removed or wrapped in list (e.g., `list[typing.Any]`) to properly support MLflow's schema validation, otherwise static type checkers like mypy will cause CI checks to fail with `no-untyped-def`.
**Prevention:** Always verify type hints when writing overriding mlflow functions (especially for arguments like `model_input`) and confirm compatibility against the test suite prior to committing.
