def assess_batch(name_batch: str, record_count:int, null_percentage:float):
    my_string = name_batch
    if record_count < 1000:
        my_string += " -> REJECT: batch too small"
    elif null_percentage > 20.0:
        my_string += " -> REJECT: too many nulls"
    elif null_percentage >= 10.0:
        my_string += " -> WARNING: elevated nulls"
    else:
        my_string += " -> PASS: batch looks clean"
    return my_string

batches = [
    {"name": "orders_2024", "record_count": 8500, "null_percentage": 12.7},
    {"name": "returns_2024", "record_count": 500, "null_percentage": 5.0},
    {"name": "products_2024", "record_count": 22000, "null_percentage": 1.2},
    {"name": "customers_2024", "record_count": 3100, "null_percentage": 22.5},
    {"name": "inventory_2024", "record_count": 15000, "null_percentage": 10.0},
]

Total_batches = 0
Passed = 0
Rejected = 0
Warnings = 0

for batch in batches:
    string_to_check = assess_batch(batch["name"], batch["record_count"], batch["null_percentage"])
    print(string_to_check)
    Total_batches += 1
    if "REJECT" in string_to_check:
        Rejected += 1
    elif "REJECT" in string_to_check:
        Rejected += 1
    elif "WARNING" in string_to_check:
        Warnings += 1
    elif "PASS" in string_to_check:
        Passed += 1

print(f"Total batches: {Total_batches}")
print(f"Passed: {Passed}")
print(f"Rejected: {Rejected}")
print(f"Warnings: {Warnings}")

'''
You have a list of batch dictionaries. Loop through all of them and for
each batch print a summary line, then at the end print overall stats.

Expected output:
orders_2024 -> WARNING: elevated nulls
returns_2024 -> REJECT: batch too small
products_2024 -> PASS: batch looks clean
customers_2024 -> REJECT: too many nulls
inventory_2024 -> WARNING: elevated nulls

Total batches: 5
Passed: 1
Rejected: 2
Warnings: 2

You must reuse your assess_batch function from Task 6.
'''