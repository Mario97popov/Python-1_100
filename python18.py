from collections import Counter, defaultdict

pipeline_runs = [
    {"pipeline": "sales_pipeline", "status": "completed", "region": "north"},
    {"pipeline": "orders_pipeline", "status": "failed", "region": "south"},
    {"pipeline": "sales_pipeline", "status": "completed", "region": "south"},
    {"pipeline": "inventory_pipeline", "status": "failed", "region": "north"},
    {"pipeline": "sales_pipeline", "status": "failed", "region": "north"},
    {"pipeline": "orders_pipeline", "status": "completed", "region": "south"},
    {"pipeline": "returns_pipeline", "status": "completed", "region": "north"},
]

counts = Counter(run["pipeline"] for run in pipeline_runs)

groups = defaultdict(list)
for run in pipeline_runs:
    groups[run["region"]].append(run["pipeline"])

print("--- Run Counts ---")
for pipeline, count in counts.items():
    print(f"{pipeline}: {count}")

print()

print("--- By Region ---")
for region, pipelines in groups.items():
    print(f"{region}: {pipelines}")

'''
Your script should:
1. Use Counter to count how many times each pipeline appears
2. Use defaultdict to group pipeline names by region
3. Print both results

Expected output:
--- Run Counts ---
sales_pipeline: 3
orders_pipeline: 2
inventory_pipeline: 1
returns_pipeline: 1

--- By Region ---
north: ['sales_pipeline', 'inventory_pipeline', 'sales_pipeline', 'returns_pipeline']
south: ['orders_pipeline', 'sales_pipeline', 'orders_pipeline']
'''