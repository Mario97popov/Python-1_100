pipeline_string = "extract,validate,transform,load,archive"
log_line = "ERROR:sales_pipeline:could not connect to database"
file_list = ["sales_data.csv", "orders_data.txt", "inventory_data.csv", "returns_data.json"]

my_string = pipeline_string.split(",")
print(my_string)
my_string = " -> ".join(my_string)
print(my_string)
for item in file_list:
    if item.endswith(".csv"):
        print(item)

print(f"transform found at index: {pipeline_string.find('transform')}")
print(log_line.replace("ERROR", "CRITICAL"))
'''
Your script should:
1. Split pipeline_string into a list and print it
2. Take that list and join it back into a string using " -> " as separator
3. Print only the files from file_list that end with ".csv"
4. Print the position where "transform" starts in pipeline_string
5. Replace "ERROR" with "CRITICAL" in log_line and print it

Expected output:
['extract', 'validate', 'transform', 'load', 'archive']
extract -> validate -> transform -> load -> archive
sales_data.csv
inventory_data.csv
transform found at index: 16
CRITICAL:sales_pipeline:could not connect to database
'''