## 2026-02-03 - Information Leakage in Exception Handling

**Vulnerability:** The application was catching all exceptions and returning their string representation (`str(e)`) directly to the client in the HTTP 500 response. This could expose sensitive internal details (stack traces, database info, file paths).
**Learning:** Developers often pass `str(e)` to `HTTPException` for convenience during debugging, but this practice frequently makes it into production code, leading to information leakage.
**Prevention:** In production, catch `Exception` and raise `HTTPException` with a generic message (e.g., "Internal Server Error"). Ensure full exception details are logged using `logger.exception()` for server-side debugging.

## 2026-02-05 - Information Leakage in Kafka Consumer

**Vulnerability:** The Kafka consumer and prediction callback were catching exceptions and embedding the raw exception message `str(e)` into the response payload sent to the output topic.
**Learning:** Even asynchronous background workers (like Kafka consumers) can leak information if they reflect input processing errors back to an output channel without sanitization.
**Prevention:** Use a dedicated `PredictionService` wrapper that catches exceptions, logs the full stack trace securely, and returns a generic "Internal Processing Error" message to the output topic.

## 2026-03-04 - Information Leakage in Application Error Fields

**Vulnerability:** The application was catching exceptions in logic callbacks and Kafka consumers, then assigning the raw exception string to a JSON `error` field in the successful response object. This leaked internal details even when the HTTP status code was 200 OK or when processing asynchronously via Kafka.
**Learning:** Checking for HTTP 500 handlers is not enough. Review application-level error handling where business logic manually constructs error objects.
**Prevention:** Ensure that any `result["error"]` or similar fields populated in catch blocks use generic messages, while the real exception is logged server-side.

## 2026-06-15 - Missing Security Middleware Defaults

**Vulnerability:** The FastAPI application lacked `CORSMiddleware` and `TrustedHostMiddleware`, leaving it open to CSRF/CORS attacks and Host Header attacks by default if not behind a proxy.
**Learning:** Developers often rely on external API gateways for these protections, but defense-in-depth requires the application to handle them as well. Testing middleware presence is tricky without a full HTTP client.
**Prevention:** Explicitly add security middleware with safe defaults (e.g., allow `*` initially but make it configurable). Verify middleware presence by inspecting `app.user_middleware` in unit tests.

## 2026-07-20 - Pydantic Validation Bypass in Kafka Consumers

**Vulnerability:** The Kafka consumer was initializing a Pydantic model with default values and then assigning fields directly (e.g., `model = Model(); model.field = data`). This bypasses Pydantic validation because `validate_assignment` is `False` by default, allowing invalid or malicious data (like excessive rows causing DoS) to be processed.
**Learning:** Pydantic models only validate arguments passed to `__init__` by default. Manual assignment after instantiation is unsafe for untrusted input.
**Prevention:** Always instantiate Pydantic models with the data as keyword arguments (e.g., `model = Model(field=data)`) to ensure validation logic runs.

## 2026-08-11 - Information Leakage, Log Bloat, and Log DoS in Input Payloads

**Vulnerability:** The application was logging the full contents of incoming Kafka messages and HTTP prediction requests at the `INFO` level. This risks exposing sensitive or PII data within logs, causing log bloat, and could lead to a Denial of Service (DoS) of the logging infrastructure by overwhelming it with massive payloads.
**Learning:** Production logs should generally not contain full raw user inputs, especially for data processing APIs where inputs can be large or sensitive. Verbose logging should be restricted to `DEBUG` levels.
**Prevention:** Log complete input payloads at `DEBUG` level only. Use `INFO` level logging to output safe, summarized information (like row and column counts) while ensuring extraction of summaries is wrapped in `try...except` to prevent application crashes from malformed data.


## 2026-10-24 - Missing Security Headers

**Vulnerability:** The FastAPI application was missing basic security HTTP headers (e.g., `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security`), leaving it vulnerable to MIME-type sniffing, Clickjacking, and Man-in-the-Middle attacks.
**Learning:** Default FastAPI configurations do not automatically set security headers. Explicit middleware is needed to inject these headers into all HTTP responses.
**Prevention:** Always add a custom middleware or use a specialized library to ensure all incoming responses get secure default headers (`nosniff`, `DENY`, HSTS).

## 2026-11-05 - DoS Risk in Kafka Consumers via Unnecessary Sleep

**Vulnerability:** The `_consume_messages` method contained a hardcoded `time.sleep(0.1)` inside the main `while` loop, creating an artificial bottleneck. This ignores the native blocking properties of `consumer.poll()` and needlessly limits message throughput, causing latency spikes and increasing the risk of Denial of Service (DoS) in high-volume environments.
**Learning:** Manual thread sleeping is rarely necessary when a library exposes built-in waiting/polling timeouts (like `poll(1.0)`). Stacking custom `sleep()` logic on top of native polling leads to poor application performance.
**Prevention:** Rely entirely on the consumer's `poll(timeout)` parameter to block while waiting for new messages efficiently. Avoid using arbitrary `time.sleep()` statements inside event loops or message-consuming pipelines unless explicitly needed for exponential backoff during error handling.

## 2026-12-01 - Algorithmic DoS Vulnerability on ML Endpoints

**Vulnerability:** The `/predict` HTTP endpoint lacked an application-level rate limiter, leaving it vulnerable to algorithmic Denial of Service (DoS) attacks. Because ML inference can be highly compute-intensive, an attacker could trivially exhaust server resources by sending rapid, valid requests from a single IP.
**Learning:** External API gateways are insufficient for defense-in-depth, especially when endpoints perform computationally expensive tasks like machine learning inference. Memory leaks must also be avoided when tracking IP histories.
**Prevention:** Implement a bounded, in-memory rate limiter using `collections.OrderedDict`. This ensures O(1) eviction of the oldest tracked IPs (e.g., capping at `MAX_TRACKED_IPS = 10000`) and limits the number of requests per window, preventing both compute exhaustion and memory bloat.

## 2026-12-05 - Algorithmic DoS Vulnerability via Unbounded Columns
**Vulnerability:** The `/predict` endpoint enforced a maximum row limit but did not limit the number of columns, allowing an attacker to submit wide payloads causing memory exhaustion and Algorithmic DoS.
**Learning:** When validating tabular or matrix-like data inputs, limits must be applied to all dimensions (both rows and columns) to properly bound memory usage.
**Prevention:** Always define and enforce strict limits on both row and column counts for incoming data structures.
