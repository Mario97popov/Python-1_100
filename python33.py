from functools import reduce

pipeline_names = ["  sales_pipeline  ", "ORDERS_PIPELINE", "  Inventory_Pipeline"]
record_counts = [8500, 3200, 15000, 500, 7200]


print(f"Cleaned: {list(map(lambda x: x.strip().replace('_', ' ').title(), pipeline_names))}")
print(f"Above 5000: {list(filter(lambda x: x > 5000, record_counts))}")
print(f"Total records: {reduce(lambda x, y: x + y, record_counts)}")

# Convert the map object to a list and print it
'''
Using map(), filter(), and reduce() (not list comprehensions or loops):

1. Use map() to clean all pipeline names (strip and title case)
2. Use filter() to keep only record counts above 5000
3. Use reduce() to calculate the total of all record counts

Print all three results.

Expected output:
Cleaned: ['Sales Pipeline', 'Orders Pipeline', 'Inventory Pipeline']
Above 5000: [8500, 15000, 7200]
Total records: 34400
'''