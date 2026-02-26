import csv

batches = [
    {"name": "orders_2024", "record_count": 8500, "null_percentage": 12.7, "status": "WARNING"},
    {"name": "returns_2024", "record_count": 500, "null_percentage": 5.0, "status": "REJECT"},
    {"name": "products_2024", "record_count": 22000, "null_percentage": 1.2, "status": "PASS"},
    {"name": "customers_2024", "record_count": 3100, "null_percentage": 22.5, "status": "REJECT"},
    {"name": "inventory_2024", "record_count": 15000, "null_percentage": 10.0, "status": "WARNING"},
]

with open('batches.csv', "w", newline="") as f:
    fieldnames = ["name", "record_count", "null_percentage", "status"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(batches)

with open('batches.csv', "r") as f:
    lines = csv.DictReader(f)
    rejects = [row for row in lines if row["status"] == "REJECT"]

print("--- Rejected Batches ---")
for row in rejects:
    print(f"{row['name']} | records: {row['record_count']} | nulls: {row['null_percentage']}%")

print(f"Total rejected: {len(rejects)}")
'''
Your script should:
1. Write the batches list to a CSV file called "batches.csv" with a header row
2. Read the file back and print only rows where status is "REJECT"
3. Print a summary at the end

Expected output:
--- Rejected Batches ---
returns_2024 | records: 500 | nulls: 5.0%
customers_2024 | records: 3100 | nulls: 22.5%
Total rejected: 2
'''