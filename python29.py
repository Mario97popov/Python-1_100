pipeline_names = ["sales", "orders", "inventory", "returns", "logistics"]
record_counts = [8500, 3200, 15000, 500, 7200]
raw_statuses = ["  COMPLETED  ", "FAILED  ", "  completed", "Failed", "COMPLETED"]

dic1 = {name: count for name, count in zip(pipeline_names, record_counts)}
dic2 = {name: status.strip().title() for name, status in zip(pipeline_names, raw_statuses)}
dic3 = {name: count for name, count in zip(pipeline_names, record_counts) if count > 5000}

print(dic1)
print(dic2)
print(dic3)
'''
Using dictionary comprehensions (not regular loops) produce the following:

1. A dictionary mapping each pipeline name to its record count
2. A dictionary mapping each pipeline name to its cleaned status
   (stripped and title cased)
3. A dictionary containing only pipelines with more than 5000 records
   mapping name to record count

Then print all three dictionaries.

Expected output:
{'sales': 8500, 'orders': 3200, 'inventory': 15000, 'returns': 500, 'logistics': 7200}
{'sales': 'Completed', 'orders': 'Failed', 'inventory': 'Completed', 'returns': 'Failed', 'logistics': 'Completed'}
{'sales': 8500, 'inventory': 15000, 'logistics': 7200}
'''