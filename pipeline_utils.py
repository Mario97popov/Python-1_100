def clean_name(name: str) -> str:
    return name.strip().title()

def assess_batch(record_count: int, null_percentage: float) -> str:
    if record_count < 1000:
        return "REJECT"
    elif null_percentage > 20.0:
        return "REJECT"
    elif null_percentage >= 10.0:
        return "WARNING"
    else:
        return "PASS"

def summarise(batches: list) -> None:
    print(f"Total batches: {len(batches)}")
    for status in ["PASS", "WARNING", "REJECT"]:
        count = sum(1 for b in batches if b == status)
        print(f"{status}: {count}")

if __name__ == "__main__":
    print(clean_name("  sales pipeline  "))
    print(assess_batch(8500, 12.7))
    summarise(["PASS", "WARNING", "REJECT", "PASS", "PASS"])