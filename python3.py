batch_name = "transactions_2024"
record_count = 8500
null_percentage = 12.7

if record_count < 1000:
    print("REJECT: batch too small")
elif null_percentage > 20:
    print("REJECT: too many nulls")
elif null_percentage >= 10:
    print("WARNING: null rate acceptable but elevated")
else:
    print(f"Batch: {batch_name} | Records: {record_count} | Nulls: {null_percentage}%")
