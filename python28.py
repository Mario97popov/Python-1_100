company_data = {
    "company": "DataCorp",
    "pipelines": [
        {"name": "sales", "runs": 42, "errors": 3},
        {"name": "orders", "runs": 31, "errors": 0},
        {"name": "inventory", "runs": 58, "errors": 7},
    ],
    "owner": "alice"
}

print(f"Company: {company_data["company"]} | Owner: {company_data["owner"]}")

for x in company_data['pipelines']:
    print(f"{x['name']}: {x['runs']}")

print(f"Total runs: {sum(pipeline['runs'] for pipeline in company_data['pipelines'])}")

my_var = max(company_data["pipelines"], key=lambda x: x["errors"])

print(f"Most errors: {my_var['name']}")

'''
Your script should navigate the nested structure to:
1. Print the company name and owner
2. Print the name and runs for each pipeline
3. Print the total number of runs across all pipelines
4. Print the name of the pipeline with the most errors

Expected output:
Company: DataCorp | Owner: alice
sales: 42 runs
orders: 31 runs
inventory: 58 runs
Total runs: 131
Most errors: inventory
'''