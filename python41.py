pipeline_stages = ["extract", "validate", "transform", "load"]
completed_stages = []

pipeline_stages.insert(0, 'connect')
pipeline_stages.append('archive')
print(f"Stages: {pipeline_stages}")
pipeline_stages.pop(0)
completed_stages.append('connect')
print(f"After pop - Stages: {pipeline_stages}")
print(f"Completed: {completed_stages}")
print(f"Validate count: {pipeline_stages.count('validate')}")
pipeline_stages.remove('transform')
pipeline_stages.reverse()
print(f"Reversed: {pipeline_stages}")

'''
Your script should:
1. Insert "connect" at the beginning of pipeline_stages
2. Append "archive" to the end of pipeline_stages
3. Print the current pipeline_stages
4. Move the first stage to completed_stages using pop()
5. Print pipeline_stages and completed_stages after the move
6. Count how many times "validate" appears in pipeline_stages
7. Remove "transform" from pipeline_stages
8. Reverse pipeline_stages in place and print it

Expected output:
Stages: ['connect', 'extract', 'validate', 'transform', 'load', 'archive']
After pop - Stages: ['extract', 'validate', 'transform', 'load', 'archive']
Completed: ['connect']
Validate count: 1
Reversed: ['archive', 'load', 'transform', 'validate', 'extract']
'''