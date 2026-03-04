from operator import itemgetter

pipeline_names = ["sales_pipeline", "orders_pipeline", "inventory_pipeline", "returns_pipeline"]
record_counts = [8500, 3200, 15000, 500]

print("--- Pipeline Index ---")
for i, name in enumerate(pipeline_names, start=1):
    print(f"{i}. {name}")

print("\n--- Pipeline Records ---")
for names, counts in zip(pipeline_names, record_counts):
    print(f"{names}: {counts} records")

print("\n--- Highest Volume ---")
top_name, top_count = max(zip(pipeline_names, record_counts), key=lambda x: x[1])
print(f"{top_name}: {top_count} records")


'''
You have two separate lists that belong together:

pipeline_names = ["sales_pipeline", "orders_pipeline", "inventory_pipeline", "returns_pipeline"]
record_counts = [8500, 3200, 15000, 500]

Your script should:
1. Use enumerate to print each pipeline with its position number
2. Use zip to pair pipeline names with record counts and print them
3. Use zip to find and print the pipeline with the highest record count

Expected output:
--- Pipeline Index ---
1. sales_pipeline
2. orders_pipeline
3. inventory_pipeline
4. returns_pipeline

--- Pipeline Records ---
sales_pipeline: 8500 records
orders_pipeline: 3200 records
inventory_pipeline: 15000 records
returns_pipeline: 500 records

--- Highest Volume ---
inventory_pipeline: 15000 records
'''