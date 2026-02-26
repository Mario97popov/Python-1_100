import os

pipeline_log = [
    "orders_2024 -> records: 8500 | nulls: 12.7%",
    "returns_2024 -> ERROR: could not parse values",
    "products_2024 -> ERROR: could not parse values",
    "customers_2024 -> records: 3100 | nulls: 22.5%",
    "inventory_2024 -> ERROR: could not parse values",
]


with open("pipeline_log.txt", "w") as f:
    for line in pipeline_log:
        f.write(line + "\n")

with open("pipeline_log.txt", "r") as f:
    lines = f.readlines()

errors = [line.strip() for line in lines if "ERROR" in line]
print("--- Error Report ---")
for error in errors:
    print(error)
print(f"Total errors: {len(errors)}")

'''
Your script should:
1. Write all lines in pipeline_log to a file called "pipeline_log.txt",
   each entry on its own line
2. Read the file back and print only the lines that contain "ERROR"
3. Print a summary at the end

Expected output:
--- Error Report ---
returns_2024 -> ERROR: could not parse values
products_2024 -> ERROR: could not parse values
inventory_2024 -> ERROR: could not parse values
Total errors: 3
'''