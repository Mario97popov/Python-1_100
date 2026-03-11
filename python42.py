pipeline = {
    "name": "sales_pipeline",
    "status": "running",
    "records": 8500,
    "errors": 3
}

defaults = {
    "owner": "unknown",
    "region": "global",
    "retries": 0
}

print(f"Name: {pipeline.get("name")}")

'''
Your script should:
1. Print the pipeline name using get() with a default of "unnamed"
2. Print a missing key "version" using get() with a default of "v1.0"
3. Update pipeline with all values from defaults
4. Add key "checksum" with value "abc123" only if it does not
   already exist using setdefault()
5. Remove and print the "errors" key using pop()
6. Print all keys, then all values, then all items

Expected output:
Name: sales_pipeline
Version: v1.0
Removed errors: 3
Keys: dict_keys(['name', 'status', 'records', 'owner', 'region', 'retries', 'checksum'])
Values: dict_values(['sales_pipeline', 'running', 8500, 'unknown', 'global', 0, 'abc123'])
Items: dict_items([('name', 'sales_pipeline'), ('status', 'running'), ('records', 8500), ('owner', 'unknown'), ('region', 'global'), ('retries', 0), ('checksum', 'abc123')])
'''