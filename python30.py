pipeline_runs = [
    {"name": "sales", "records": 8500, "errors": 3},
    {"name": "orders", "records": 3200, "errors": 0},
    {"name": "inventory", "records": 15000, "errors": 7},
    {"name": "returns", "records": 500, "errors": 7},
    {"name": "logistics", "records": 7200, "errors": 1},
]

pipeline_runs_sorted_asc = sorted(pipeline_runs, key=lambda x: x["records"])
print("--- By Records Ascending ---")
for x in pipeline_runs_sorted_asc:
    print(f"{x['name']}: {x['records']}")


pipeline_runs_sorted_desc = sorted(pipeline_runs, key=lambda x: x["records"], reverse=True)
print("\n--- By Records Descending ---")
for x in pipeline_runs_sorted_desc:
    print(f"{x['name']}: {x['records']}")

pipeline_runs_sorted_by_error = sorted(pipeline_runs, key=lambda x: (-x["errors"], x["name"]))

print("\n--- By Errors Descending Then Name ---")
for x in pipeline_runs_sorted_by_error:
    print(f"{x['name']}: {x['errors']} errors")

print("\n --- Names Alphabetically ---")
names_list = [item["name"] for item in pipeline_runs]
names_list.sort()
print(names_list)
'''
Your script should:
1. Print the pipelines sorted by records ascending
2. Print the pipelines sorted by records descending
3. Print the pipelines sorted by errors descending, then by name
   alphabetically when errors are equal
4. Print just the pipeline names sorted alphabetically

Expected output:
--- By Records Ascending ---
returns: 500
orders: 3200
logistics: 7200
sales: 8500
inventory: 15000

--- By Records Descending ---
inventory: 15000
sales: 8500
logistics: 7200
orders: 3200
returns: 500

--- By Errors Descending Then Name ---
inventory: 7 errors
returns: 7 errors
sales: 3 errors
logistics: 1 errors
orders: 0 errors

--- Names Alphabetically ---
['inventory', 'logistics', 'orders', 'returns', 'sales']
'''