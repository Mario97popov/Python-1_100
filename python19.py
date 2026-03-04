import os
import json

pipeline_runs = [
    {"pipeline": "sales_pipeline", "status": "completed", "records": 8500},
    {"pipeline": "orders_pipeline", "status": "failed", "records": 3200},
    {"pipeline": "inventory_pipeline", "status": "completed", "records": 15000},
]

if not os.path.exists("pipeline_output"):
    os.makedirs("pipeline_output")

for key in pipeline_runs:
    path = os.path.join("pipeline_output", f"{key['pipeline']}.json")
    with open(path, "w") as f:
        json.dump(key, f)

    print(f"Written: {path}")

print("\nFiles in pipeline_output:")
for file in os.listdir("pipeline_output"):
    print(f"- {file}")

'''
Your script should:
1. Create a folder called "pipeline_output" if it does not already exist
2. Write each pipeline run as its own separate JSON file inside that folder,
   named after the pipeline e.g. sales_pipeline.json
3. Print a confirmation for each file written
4. Then list all files in the folder and print them

Expected output:
Written: pipeline_output/sales_pipeline.json
Written: pipeline_output/orders_pipeline.json
Written: pipeline_output/inventory_pipeline.json

Files in pipeline_output:
- inventory_pipeline.json
- orders_pipeline.json
- sales_pipeline.json
'''