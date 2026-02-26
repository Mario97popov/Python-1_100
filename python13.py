def log_event(message, level="INFO", **kwargs):
    extras = (" | " + " | ".join(f"{k}={v}" for k, v in kwargs.items())) if kwargs else ""
    return f"[{level}] {message}{extras}"



print(log_event("pipeline started"))
print(log_event("records loaded", level="INFO"))
print(log_event("null threshold exceeded", level="WARNING", pipeline="sales_pipeline"))
print(log_event("connection failed", level="ERROR", pipeline="orders_pipeline", retries=3))
'''
Write a function called log_event that can handle all of these calls:

log_event("pipeline started")
log_event("records loaded", level="INFO")
log_event("null threshold exceeded", level="WARNING", pipeline="sales_pipeline")
log_event("connection failed", level="ERROR", pipeline="orders_pipeline", retries=3)

Expected output:
[INFO] pipeline started
[INFO] records loaded
[WARNING] null threshold exceeded | pipeline=sales_pipeline
[ERROR] connection failed | pipeline=orders_pipeline | retries=3

Rules:
- level should default to "INFO" if not provided
- any extra keyword arguments (like pipeline, retries) should be printed
  as key=value pairs separated by " | "
- the function must work for any number of extra keyword arguments,
  not just the ones shown above
'''