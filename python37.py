raw_data = [
    {"name": "sales", "records": "8500", "active": "True", "error_rate": "0.032"},
    {"name": "orders", "records": 42.7, "active": "False", "error_rate": "N/A"},
    {"name": "inventory", "records": "fifteen thousand", "active": "True", "error_rate": "0.127"},
    {"name": "returns", "records": "500", "active": "True", "error_rate": "0.0"},
    {"name": "logistics", "records": "", "active": "False", "error_rate": "0.056"},
]

for record in raw_data:
    try:
        error_rate = float(record["error_rate"])
    except ValueError:
        error_rate = "invalid"

    try:
        if isinstance(record["records"], float):
            records = "invalid"
        else:
            records = int(record["records"])
    except ValueError:
        records = "invalid"

    # COULD HAVE USED active = record["active"] == "True"
    try:
        if record['active'] == "True":
            active = True
        else:
            active = False
    except:
        active = False
    print(f"{record['name']} | records: {records} | active: {active} | error_rate: {error_rate}")


'''
Loop through raw_data and for each entry attempt to clean and
convert the fields. Print a result for each pipeline.

Rules:
- records must be a whole number, if conversion fails print "invalid"
- active must be a boolean, "True" -> True, anything else -> False
- error_rate must be a float, if conversion fails print "invalid"

Expected output:
sales | records: 8500 | active: True | error_rate: 0.032
orders | records: invalid | active: False | error_rate: invalid
inventory | records: invalid | active: True | error_rate: 0.127
returns | records: 500 | active: True | error_rate: 0.0
logistics | records: invalid | active: False | error_rate: 0.056
'''