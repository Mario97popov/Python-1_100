class Pipeline:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.stages = []
        self.status = "idle"

    def add_stages(self, stage_name):
        for x in stage_name:
            self.stages.append(x)

    def start(self):
        self.status = "running"
        print(f"{self.name} started by {self.owner}")

    def summary(self):
        print(f"Pipeline: {self.name}")
        print(f"Owner: {self.owner}")
        print(f"Status: {self.status}")
        print(f"Stages: {self.stages}")

    def is_ready(self):
        if self.status == "running" and len(self.stages) > 0:
            return True
        else:
            return False

    def reset(self):
        self.status = "idle"
        self.stages = []
        print(f"{self.name} has been reset")

    def __str__(self):
        return f"Pipeline(name={self.name}, status={self.status}, stages={len(self.stages)})"

p = Pipeline("sales_pipeline", "alice")
p.add_stages(["extract", "transform", "load"])
p.start()
print(p)
print("Ready:", p.is_ready())
p.reset()
print(p)
print("Ready:", p.is_ready())

'''
Extend your Pipeline class from Task 14 with the following additions:

1. A method called add_stages(stage_list) that accepts a list and adds
   all stages at once instead of one by one

2. A method called reset() that clears stages back to an empty list
   and sets status back to "idle" and prints:
   "{name} has been reset"

3. A __str__ method that returns a single string so that
   print(p) produces:
   Pipeline(name=sales_pipeline, status=running, stages=3)
   where stages shows the COUNT not the list

4. A method called is_ready() that returns True if there is at least
   one stage and status is "running", otherwise False

Then run this code:
p = Pipeline("sales_pipeline", "alice")
p.add_stages(["extract", "transform", "load"])
p.start()
print(p)
print("Ready:", p.is_ready())
p.reset()
print(p)
print("Ready:", p.is_ready())

Expected output:
sales_pipeline started by alice
Pipeline(name=sales_pipeline, status=running, stages=3)
Ready: True
sales_pipeline has been reset
Pipeline(name=sales_pipeline, status=idle, stages=0)
Ready: False
'''