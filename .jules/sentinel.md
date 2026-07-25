## 2026-04-18 - Synchronous Kafka Producer Flush in Message Loop
**Vulnerability:** Performance bottleneck and latency amplification from synchronous blocking network I/O in the core processing loop.
**Learning:** Re-flushing the confluent_kafka producer on every single message forces the application to block on round-trip network acknowledgment for every record, severely limiting throughput.
**Prevention:** Allow confluent_kafka to batch messages efficiently in memory by replacing `flush()` with a non-blocking `poll(0)` in the message processing loop, and calling `flush()` only during service shutdown to ensure graceful delivery of buffered messages.
