filename = "sales_pipeline_2024_03_28.csv"

print(f"Extension: {filename[-3:]}")
print(f"Name: {filename[:-4]}")
print(f"Year: {filename[15:19]}")
print(f"Month: {filename[20:22]}")
print(f"Day: {filename[23:25]}")

'''
Without using split() or any string methods, use only slicing and
indexing to extract information from the filename.

Your script should:
1. Print the file extension (last 3 characters)
2. Print the full filename without the extension (everything except last 4 characters)
3. Print the year (characters at index 15 to 19)
4. Print the month (characters at index 20 to 22)
5. Print the day (characters at index 23 to 25)

Expected output:
Extension: csv
Name: sales_pipeline_2024_03_28
Year: 2024
Month: 03
Day: 28
'''