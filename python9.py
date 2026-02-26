raw_entries = [
    "  Sales_Pipeline  ",
    "CUSTOMERS_2024",
    "orders pipeline",
    "  INVENTORY_2024   ",
    "Returns_Pipeline  "
]

pipeline_records = [
    {"name": "orders_2024", "record_count": 8500, "null_percentage": 12.7},
    {"name": "returns_2024", "record_count": 500, "null_percentage": 5.0},
    {"name": "products_2024", "record_count": 22000, "null_percentage": 1.2},
    {"name": "customers_2024", "record_count": 3100, "null_percentage": 22.5},
    {"name": "inventory_2024", "record_count": 15000, "null_percentage": 10.0},
]

cleaned_raw_entries = [entry.strip().replace("_", " ").title() for entry in raw_entries]
names_only_records = [record["name"] for record in pipeline_records if record["record_count"] > 5000]
null_double = [record["record_count"] * 2 for record in pipeline_records if record["null_percentage"] < 10.0]
print(cleaned_raw_entries)
print(names_only_records)
print(null_double)

'''
Using list comprehensions (not regular for loops), produce the following:

1. A cleaned list from raw_entries using the same logic as Task 8
   (strip, replace underscores, title case) — one line

2. A list of names only from pipeline_records where record_count > 5000
   — one line

3. A list of record counts doubled for every batch where null_percentage < 10.0
   — one line

Then print all three lists.

Expected output:
['Sales Pipeline', 'Customers 2024', 'Orders Pipeline', 'Inventory 2024', 'Returns Pipeline']
['orders_2024', 'products_2024', 'customers_2024', 'inventory_2024']
[44000, 1000]
'''