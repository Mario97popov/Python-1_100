total_records = 0
pipeline_log = []

def process_batch(name, records):
    global pipeline_log
    global total_records
    total_records += records
    pipeline_log.append(name)
    return print(f"Processed {name}: {records} records")


process_batch("sales", 8500)
process_batch("orders", 3200)
process_batch("inventory", 15000)

print(f"Total records: {total_records}")
print(f"Pipelines: {pipeline_log}")
'''
Your script should:
1. Write a function called process_batch that takes name and records
   as parameters and does the following:
   - adds records to total_records
   - appends the name to pipeline_log
   - returns a formatted string: "Processed name: X records"

2. Call process_batch three times with this data:
   ("sales", 8500)
   ("orders", 3200)
   ("inventory", 15000)

3. Print the return value of each call
4. Print the final total_records and pipeline_log after all calls

Expected output:
Processed sales: 8500 records
Processed orders: 3200 records
Processed inventory: 15000 records
Total records: 26700
Pipelines: ['sales', 'orders', 'inventory']
'''