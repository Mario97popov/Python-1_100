regions = ["north", "south", "east"]
pipelines = ["sales", "orders", "inventory"]

active_pipelines = ["sales", "inventory", "returns", "logistics"]
failed_pipelines = ["orders", "inventory", "logistics", "finance"]

print("--- Region/Pipeline Combinations ---")
counter = 0
for x in regions:
    for y in pipelines:
        print(f"{x} - {y}")
        counter += 1
print(f"Total combinations: {counter}")

print("\n--- Pipelines in both lists ---")
for x in active_pipelines:
    if x in failed_pipelines:
        print(x)

'''
Your script should:
1. Use nested loops to print every combination of region and pipeline
2. Count and print the total number of combinations at the end
3. Use a nested loop to find and print any pipeline that appears in
   both lists below:

   active_pipelines = ["sales", "inventory", "returns", "logistics"]
   failed_pipelines = ["orders", "inventory", "logistics", "finance"]

Expected output:
--- Region/Pipeline Combinations ---
north - sales
north - orders
north - inventory
south - sales
south - orders
south - inventory
east - sales
east - orders
east - inventory
Total combinations: 9

--- Pipelines in both lists ---
inventory
logistics
'''