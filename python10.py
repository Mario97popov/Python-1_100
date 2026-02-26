raw_batches = [
    {"name": "orders_2024", "record_count": "8500", "null_percentage": "12.7"},
    {"name": "returns_2024", "record_count": "five hundred", "null_percentage": "5.0"},
    {"name": "products_2024", "record_count": "22000", "null_percentage": "N/A"},
    {"name": "customers_2024", "record_count": "3100", "null_percentage": "22.5"},
    {"name": "inventory_2024", "record_count": "", "null_percentage": "10.0"},
]

for batch in raw_batches:
    try:
        batch["record_count"] = int(batch["record_count"])
        batch["null_percentage"] = float(batch["null_percentage"])
        print(f"records: {batch['record_count']} | nulls: {batch['null_percentage']}%")
    except ValueError:
        print("ERROR: could not parse values")

'''
You are receiving batch metadata as raw strings from an external source.
Some values are malformed. Your script should loop through each batch,
attempt to convert record_count to int and null_percentage to float,
and handle any conversion errors gracefully without crashing.

Expected output:
orders_2024 -> records: 8500 | nulls: 12.7%
returns_2024 -> ERROR: could not parse values
products_2024 -> ERROR: could not parse values
customers_2024 -> records: 3100 | nulls: 22.5%
inventory_2024 -> ERROR: could not parse values
'''