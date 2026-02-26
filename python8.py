raw_entries = [
    "  Sales_Pipeline  ",
    "CUSTOMERS_2024",
    "orders pipeline",
    "  INVENTORY_2024   ",
    "Returns_Pipeline  "
]

for each in raw_entries:
    each = each.strip().replace("_", " ").title()
    print(each)


'''
You received a list of raw pipeline name strings from an external source.
They are messy — inconsistent casing, extra whitespace, underscores instead
of spaces. Clean them and print each result.

Your script should process each entry and produce a standardised name by:
1. Stripping leading and trailing whitespace
2. Replacing underscores with spaces
3. Converting the result to title case

Expected output:
Sales Pipeline
Customers 2024
Orders Pipeline
Inventory 2024
Returns Pipeline

No functions required. Just a loop and string methods.
'''