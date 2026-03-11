def parse_log_line(line):
    """Takes a raw log string and returns a parsed dictionary with typed values."""
    keys = ["date", "pipeline", "status", "records"]
    my_dict = dict(zip(keys, line.split(" | ")))
    my_dict["records"] = int(my_dict["records"].replace("records", "").strip())
    return my_dict

def is_valid_batch(records, null_percentage):
    """Returns True if batch meets minimum quality thresholds."""
    if records >= 1000 and null_percentage <= 20.0:
        return True
    else:
        return False

def format_summary(name, records, status):
    """Returns a formatted summary string for a pipeline run."""
    return f"[{status}] {name}: {records} records"

def calculate_error_rate(errors, total):
    """Returns error rate as a percentage string, or 0.0% if total is zero."""
    result = (errors / total) * 100
    return f"{round(result, 2)}%"

my_dict = parse_log_line("2024-03-28 | sales_pipeline | COMPLETED | 8500 records")
print(my_dict)
print(is_valid_batch(my_dict['records'], 12.7))
print(is_valid_batch(my_dict['records'], 20.1))
print(format_summary(my_dict['pipeline'], my_dict['records'], my_dict['status']))
print(calculate_error_rate(200, my_dict['records']))
print(calculate_error_rate(0, my_dict['records']))
'''
Write a utility module with four functions that a data pipeline
would actually use. Each function must have a docstring.

1. parse_log_line(line)
   Takes a string in this format:
   "2024-03-28 | sales_pipeline | COMPLETED | 8500 records"
   Returns a dictionary with keys: date, pipeline, status, records
   records must be an integer

2. is_valid_batch(records, null_percentage)
   Returns True if records >= 1000 and null_percentage <= 20.0
   Otherwise returns False

3. format_summary(name, records, status)
   Returns a formatted string:
   "[STATUS] name: X,XXX records"

4. calculate_error_rate(errors, total)
   Returns the error rate as a percentage rounded to 2 decimal places
   If total is 0 return 0.0 to avoid division by zero

Then test each function by calling it and printing the result.

Expected output:
{'date': '2024-03-28', 'pipeline': 'sales_pipeline', 'status': 'COMPLETED', 'records': 8500}
True
False
[COMPLETED] sales_pipeline: 8,500 records
2.35%
0.0%
'''