import json

pipeline_runs = [
    {"pipeline": "sales_pipeline", "status": "completed", "records": 8500, "errors": 0},
    {"pipeline": "orders_pipeline", "status": "failed", "records": 3200, "errors": 14},
    {"pipeline": "inventory_pipeline", "status": "completed", "records": 15000, "errors": 2},
    {"pipeline": "returns_pipeline", "status": "failed", "records": 500, "errors": 31},
]

with open("pipeline_runs.json", "w") as f:
    json.dump(pipeline_runs, f)

with open("pipeline_runs.json", "r") as f:
    data = json.load(f)
    rejects = [row for row in data if row["status"] == "failed"]
    for x in rejects:
        print(f"{x['pipeline']} failed with {x['errors']} errors")
    print(f"Total runs: {len(data)}")
    print(f"Failed: {len(rejects)}")
    print(f"Success rate: {(len(data) - len(rejects)) / len(data) * 100}%")
'''
Your script should:
1. Write pipeline_runs to a file called "pipeline_runs.json"
2. Read it back from the file
3. Print only the failed pipelines in this format:
   orders_pipeline failed with 14 errors
   returns_pipeline failed with 31 errors
4. Print a summary at the end:
   Total runs: 4
   Failed: 2
   Success rate: 50.0%
'''