monday_pipelines = {"sales", "orders", "inventory", "returns", "logistics"}
tuesday_pipelines = {"sales", "inventory", "finance", "logistics", "hr"}

print(f"Both days: {tuesday_pipelines & monday_pipelines}")
print(f"Either day: {tuesday_pipelines | monday_pipelines}")
print(f"Monday only: {monday_pipelines - tuesday_pipelines}")
print(f"Tuesday only: {tuesday_pipelines - monday_pipelines}")
print(f"Shared pipelines: {not(tuesday_pipelines.isdisjoint(monday_pipelines))}")
'''
Your script should use set operations (not loops) to answer
these questions about the two days of pipelines:

1. Which pipelines ran on both days?
2. Which pipelines ran on either day (all unique pipelines)?
3. Which pipelines ran on Monday but NOT Tuesday?
4. Which pipelines ran on Tuesday but NOT Monday?
5. Did Monday and Tuesday share any pipelines? Print True or False

Expected output:
Both days: {'sales', 'logistics', 'inventory'}
Either day: {'sales', 'orders', 'inventory', 'returns', 'logistics', 'finance', 'hr'}
Monday only: {'orders', 'returns'}
Tuesday only: {'finance', 'hr'}
Shared pipelines: True
'''