pipelines = [
    {"name": "sales", "records": 8500, "errors": 3, "active": True},
    {"name": "orders", "records": 3200, "errors": 0, "active": False},
    {"name": "inventory", "records": 15000, "errors": 7, "active": True},
    {"name": "returns", "records": 500, "errors": 0, "active": True},
    {"name": "logistics", "records": 7200, "errors": 12, "active": False},
]

for pipeline in pipelines:
    if pipeline["active"] == False:
        print(f"{pipeline['name']} -> SKIP")
    elif pipeline["errors"] > 10:
        print(f"{pipeline['name']} -> CRITICAL")
    elif pipeline["errors"] == 0 and pipeline["records"] > 1000:
        print(f"{pipeline['name']} -> HEALTHY")
    elif pipeline["errors"] > 0 and pipeline["errors"] <= 10:
        print(f"{pipeline['name']} -> WARNING")
    elif pipeline["errors"] == 0 and pipeline["records"] <= 1000:
        print(f"{pipeline['name']} -> SMALL")

'''
Loop through the pipelines and for each one print a verdict
based on these combined conditions:

- Print "SKIP" if the pipeline is not active
- Print "CRITICAL" if active and errors > 10
- Print "HEALTHY" if active and errors == 0 and records > 1000
- Print "WARNING" if active and errors > 0 and errors <= 10
- Print "SMALL" if active and errors == 0 and records <= 1000

Expected output:
sales -> WARNING
orders -> SKIP
inventory -> CRITICAL
returns -> SMALL
logistics -> SKIP
'''