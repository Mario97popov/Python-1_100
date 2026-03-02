from datetime import datetime

pipeline_runs = [
    {"pipeline": "sales_pipeline", "run_date": "2024-01-15", "records": 8500},
    {"pipeline": "orders_pipeline", "run_date": "2024-03-22", "records": 3200},
    {"pipeline": "inventory_pipeline", "run_date": "2024-03-28", "records": 15000},
    {"pipeline": "returns_pipeline", "run_date": "2024-02-10", "records": 500},
]

for x in pipeline_runs:
    x["run_date"] = datetime.strptime(x["run_date"], "%Y-%m-%d").date()

march_runs = [x for x in pipeline_runs if x["run_date"].month == 3]
most_recent_march = max(march_runs, key=lambda x: x["run_date"])

print("--- March 2024 Runs ---")
march_runs = []
today = datetime.today().date()

for x in pipeline_runs:
    if x["run_date"].month == 3:
        march_runs.append(x)
        days_ago = (today - x["run_date"]).days
        print(f"{x['pipeline']} | {x['run_date']} | {days_ago} days ago")

most_recent_march = max(march_runs, key=lambda x: x["run_date"])


print(f"Most recent run: {most_recent_march['run_date']}")
'''
Your script should:
1. Add a timestamp to each run by converting run_date string to a
   datetime object
2. Print runs that happened in March 2024 only
3. Print how many days ago each March run was from today
4. Print the most recent run date across all pipelines

Expected output (will differ based on todays date):
--- March 2024 Runs ---
orders_pipeline | 2024-03-22 | X days ago
inventory_pipeline | 2024-03-28 | X days ago
Most recent run: 2024-03-28
'''