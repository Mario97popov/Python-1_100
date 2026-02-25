import pandas as pd

data = {
    "source_name": ["customer_orders"],
    "record_count": [150000],
    "is_active": [True],
    "load_time_seconds": [3.75]
}

df = pd.DataFrame(data)

counter = 0

my_list = ["Source", "Records", "Active", "Load time"]

for key, value in df.items():
    print(f"{my_list[counter]}: {value[0]}")
    counter += 1