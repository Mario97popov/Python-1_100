raw_records = "200000"
raw_load_time = "4.5"
pipeline_name = "sales_pipeline"

raw_records_new = int(raw_records)
raw_load_time_new = float(raw_load_time)

record_per_second = round(raw_records_new / raw_load_time_new, 2)

print(f"Pipeline:: {pipeline_name}")
print(f"Records processed: {raw_records_new}")
print(f"Load time: {raw_load_time_new}s")
print(f"Throughput: {record_per_second}")