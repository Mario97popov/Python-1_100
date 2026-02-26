# your code here
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

print(assess_batch("orders_2024", 8500, 12.7))
print(assess_batch("returns_2024", 500, 5.0))
print(assess_batch("products_2024", 22000, 1.2))
'''
A pipeline needs a reusable function to assess batch quality.
Write a function called assess_batch that takes three parameters:
batch_name, record_count, and null_percentage.

The function should return a status string based on these rules:
- record_count below 1000 → return "REJECT: batch too small"
- null_percentage above 20.0 → return "REJECT: too many nulls"
- null_percentage between 10.0 and 20.0 (inclusive) → return "WARNING: elevated nulls"
- otherwise → return "PASS: batch looks clean"

Then call the function three times with these batches and print the result of each:
assess_batch("orders_2024", 8500, 12.7)
assess_batch("returns_2024", 500, 5.0)
assess_batch("products_2024", 22000, 1.2)

Expected output:
orders_2024 -> WARNING: elevated nulls
returns_2024 -> REJECT: batch too small
products_2024 -> PASS: batch looks clean
'''