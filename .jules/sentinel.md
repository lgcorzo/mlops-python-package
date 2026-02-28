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

## 2026-08-11 - Log Bloat and Information Leakage in Input Payloads

**Vulnerability:** The application was logging full raw input payloads (from HTTP requests and Kafka messages) at the `INFO` level. This could expose sensitive user data, personally identifiable information (PII), and cause log bloat or log DoS attacks.
**Learning:** Logging entire request objects at `INFO` is dangerous for both security and operational stability. Only safe summaries should be logged at `INFO`, while full details can be relegated to `DEBUG` for troubleshooting.
**Prevention:** Ensure that input payloads are logged at `DEBUG` level. For `INFO` level, compute safe summaries (e.g., extracting row counts or payload size). Always wrap the parsing logic for these summaries in a `try...except` block so that malformed or unexpected data structures do not crash the application.
