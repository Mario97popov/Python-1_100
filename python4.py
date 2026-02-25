pipeline_stages = ["extract", "validate", "transform", "load"]
failed_stage = "transform"

# your code here
print(f"Total stages: {len(pipeline_stages)}")
print(f"First: {pipeline_stages[0]} | Last: {pipeline_stages[-1]}")
print(f"Active stages: {pipeline_stages[:-1]}")
pipeline_stages.append("archive")
print(f"Stage added. Pipeline now has {len(pipeline_stages)} stages.")
if failed_stage in pipeline_stages:
    print(f"Failed at stage index: {pipeline_stages.index(failed_stage)}")
'''
You are managing a data pipeline with a list of stages.
Your script should:

1. Print the total number of stages
2. Print the first and last stage
3. Print all stages except the last one
4. Add a new stage called "archive" at the end of the list
5. Print the index position of the failed_stage inside the list

Expected output:
Total stages: 4
First: extract | Last: load
Active stages: ['extract', 'validate', 'transform']
Stage added. Pipeline now has 5 stages.
Failed at stage index: 2
'''