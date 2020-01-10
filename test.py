from core.service import Worker, Services, register
from core.shared import SharedMemory
from core.action import Task, Action


class WorkerTest(Worker):
    name = "test"


worker_test = WorkerTest()


@register(worker_test, "test.a1")
def test_a1(worker, task: Task):
    print("test_a1")
    worker.action.set(token=task.token, data=task.data * 10)


@register(worker_test, "test.a2")
def test_a2(worker, task: Task):
    print("test_a2")
    worker.action.set(token=task.token, data=task.data * 100)
    worker.action.push(name="test.a1", token=task.token + 1, data=0.1)


shared_memory_clean = SharedMemory()
services = Services(shared_memory_clean)
services.register(worker_test)
action = Action(services.shared_memory)

t1 = action.random_token()
t2 = action.random_token()
t3 = action.random_token()

action.push(name="test.a1", token=t1, data=1)
action.push(name="test.a1", token=t2, data=2)
action.push(name="test.a2", token=t3, data=3)

print(t1, t2, t3)

services.run()

import time

time.sleep(1)

d1 = action.get(token=t1)
d2 = action.get(token=t2)
d3 = action.get(token=t3)

d3s = action.get(token=t3 + 1)

print(d1, d2, d3, d3s)

assert d1 == 10
assert d2 == 20
assert d3 == 300

assert d3s == 1.0

services.wait()
