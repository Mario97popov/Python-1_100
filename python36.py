pipeline_runs = [
    {"name": "sales", "records": 8500, "error_rate": 0.032},
    {"name": "orders", "records": 3200, "error_rate": 0.0},
    {"name": "inventory", "records": 15000, "error_rate": 0.127},
    {"name": "returns", "records": 500, "error_rate": 0.0},
    {"name": "logistics", "records": 7200, "error_rate": 0.056},
]
records_sum = 0
print("Pipeline Report")
print("===============")
print(f"{'Name':<15}{'Records':>15}{'Error Rate':>15}")
for run in pipeline_runs:
    print(f"{run['name']:<15}{run['records']:>15,}{run['error_rate']:>15.2%}")
    records_sum += run['records']
print("===============")
print(f"{'Total records':<15}{records_sum:>15,}")

'''
Print a formatted report that looks exactly like this:

Pipeline Report
===============
Name            Records    Error Rate
sales             8,500         3.20%
orders            3,200         0.00%
inventory        15,000        12.70%
returns             500         0.00%
logistics         7,200         5.60%
===============
Total records:   34,400
'''