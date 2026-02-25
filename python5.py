pipeline_metadata = {
    "name": "sales_pipeline",
    "records_processed": 120000,
    "status": "running",
    "retries": 2
}

print(f"Pipeline: {pipeline_metadata['name']} | Status: {pipeline_metadata['status']}")
pipeline_metadata['status'] = "completed"
print("Status updated.")
pipeline_metadata["records_failed"] = 340
print(f"Total fields: {len(pipeline_metadata)}")
for key, value in pipeline_metadata.items():
    print(f"{key} -> {value}")

print(pipeline_metadata.get("owner"))
print(pipeline_metadata.get("owner", "unknown"))
'''
You are working with a dictionary storing pipeline metadata.
Your script should:

1. Print the pipeline name and status
2. Update the status to "completed"
3. Add a new key "records_failed" with value 340
4. Print the total number of keys in the dictionary
5. Print all keys and their values, one per line, in this format:
   name -> sales_pipeline
   records_processed -> 120000
   status -> completed
   retries -> 2
   records_failed -> 340

Expected output:
Pipeline: sales_pipeline | Status: running
Status updated.
Total fields: 5
name -> sales_pipeline
records_processed -> 120000
status -> completed
retries -> 2
records_failed -> 340
'''