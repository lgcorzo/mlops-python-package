## 2026-04-18 - Synchronous Kafka Producer Flush in Message Loop
**Vulnerability:** Performance bottleneck and latency amplification from synchronous blocking network I/O in the core processing loop.
**Learning:** Re-flushing the confluent_kafka producer on every single message forces the application to block on round-trip network acknowledgment for every record, severely limiting throughput.
**Prevention:** Allow confluent_kafka to batch messages efficiently in memory by replacing `flush()` with a non-blocking `poll(0)` in the message processing loop, and calling `flush()` only during service shutdown to ensure graceful delivery of buffered messages.

## 2026-04-20 - Data Exposure in Kafka Consumer Result Logging
**Vulnerability:** Clear logging of raw prediction result which contains sensitive output data (e.g., list of inference values).
**Learning:** Logging entire prediction payloads at DEBUG level or any other level can expose sensitive inference outputs to log aggregation and monitoring systems, violating compliance and security standards.
**Prevention:** Avoid logging raw prediction output values. Instead, clone the dictionary and mask or summarize the sensitive prediction list (e.g., indicating the length of the list, such as `<masked_list_len_X>`) before passing it to the logger.
