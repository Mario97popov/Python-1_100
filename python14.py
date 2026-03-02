class Pipeline:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.stages = []
        self.status = "idle"

    def add_stage(self, stage_name):
        self.stages.append(stage_name)

    def start(self):
        self.status = "running"
        print(f"{self.name} started by {self.owner}")

    def summary(self):
        print(f"Pipeline: {self.name}")
        print(f"Owner: {self.owner}")
        print(f"Status: {self.status}")
        print(f"Stages: {self.stages}")

p = Pipeline("sales_pipeline", "alice")
p.add_stage("extract")
p.add_stage("transform")
p.add_stage("load")
p.start()
p.summary()
'''
Create a class called Pipeline with the following:

- __init__ takes name and owner as parameters and sets them as instance variables
- An instance variable called stages that starts as an empty list
- An instance variable called status that starts as "idle"
- A method called add_stage(stage_name) that appends to stages
- A method called start() that sets status to "running" and prints:
  "{name} started by {owner}"
- A method called summary() that prints:
  Pipeline: {name}
  Owner: {owner}
  Status: {status}
  Stages: {stages}

Then run this code:
p = Pipeline("sales_pipeline", "alice")
p.add_stage("extract")
p.add_stage("transform")
p.add_stage("load")
p.start()
p.summary()

Expected output:
sales_pipeline started by alice
Pipeline: sales_pipeline
Owner: alice
Status: running
Stages: ['extract', 'transform', 'load']
'''