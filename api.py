from core.service import Worker, Services
from core.action import Task, Action
from core.shared import SharedMemory


class WorkerA(Worker):
    name = "A"
    pass


class WorkerB(Worker):
    name = "B"

    def call(self, task: Task):
        print(f"[{self.name}:{self.idx}] HAVE -->\
\t token={task.token} \t data={task.data}")
        self.action.set(token=task.token, data=str(task.data) + "+BBBB")


shared_memory_clean = SharedMemory()

services = Services(shared_memory_clean)

services.register(WorkerA)
services.register(WorkerA)

services.register(WorkerB)

action = Action(services.shared_memory)

tokens = []
for data in range(100):
    token = action.random_token()
    action.push(name="A", token=token, data=data)
    tokens.append(token)

    token = action.random_token()
    action.push(name="B", token=token, data=data)
    tokens.append(token)

services.run()
print("--- SERVICE ---")

import time

time.sleep(2)

for token in tokens:
    print(action.get(token))

services.wait()
