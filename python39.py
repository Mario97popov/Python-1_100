raw_logs = [
    "2024-03-28 | sales_pipeline | COMPLETED | 8500 records",
    "2024-03-28 | orders_pipeline | FAILED | 3200 records",
    "2024-03-29 | inventory_pipeline | COMPLETED | 15000 records",
    "2024-03-29 | returns_pipeline | FAILED | 500 records",
    "2024-03-30 | logistics_pipeline | COMPLETED | 7200 records",
]
keys = ["Date", "Pipeline", "Status", "Records"]

list_of_dicts = [
    {keys[i]: row.split(" | ")[i] for i in range(len(keys))}
    for row in raw_logs
]
print("--- Parsed Logs ---")
for x in list_of_dicts:
    x['Records'] = int(x['Records'].replace("records", "").strip())


for x in list_of_dicts:
    print(f"Date: {x['Date']} | Pipeline: {x['Pipeline']} | Status: {x['Status']} | Records: {x['Records']}")

print("\n--- Summary ---")
print("Total logs: ", len(list_of_dicts))
print("Completed: ", sum(1 for x in list_of_dicts if x['Status'] == "COMPLETED"))
print("Failed: ", sum(1 for x in list_of_dicts if x['Status'] == "FAILED"))
print("Total records: ", sum(x['Records'] for x in list_of_dicts))


'''
Parse each log line into its components and store them as a list
of dictionaries. Then print a summary.

Expected output:
--- Parsed Logs ---
Date: 2024-03-28 | Pipeline: sales_pipeline | Status: COMPLETED | Records: 8500
Date: 2024-03-28 | Pipeline: orders_pipeline | Status: FAILED | Records: 3200
Date: 2024-03-29 | Pipeline: inventory_pipeline | Status: COMPLETED | Records: 15000
Date: 2024-03-29 | Pipeline: returns_pipeline | Status: FAILED | Records: 500
Date: 2024-03-30 | Pipeline: logistics_pipeline | Status: COMPLETED | Records: 7200

--- Summary ---
Total logs: 5
Completed: 3
Failed: 2
Total records: 34400
'''