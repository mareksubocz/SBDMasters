import sys
import random
import multiprocessing
from dataclasses import dataclass

# ERROR: https://www.youtube.com/watch?v=4HX6nSlBGss


@dataclass
class Task:
    token: int
    data: object


class SharedMemory:
    manager = None
    memory = {}

    def __init__(self):
        self.manager = multiprocessing.Manager()
        self.memory = {
            "queue": MemoryQueue(self.manager),
            "hashmap": MemoryHashmap(self.manager),
        }

    def __getitem__(self, key):
        return self.memory[key]


class MemoryQueue:
    manager = None
    memory = {}

    def __init__(self, manager):
        self.manager = manager

    def create(self, name="__main__"):
        self.memory[name] = self.manager.Queue()

    def push(self, data, name="__main__"):
        self.memory[name].put(data)

    def pull(self, name="__main__"):
        return self.memory[name].get()  # blocking


class MemoryHashmap:
    manager = None
    memory = None

    def __init__(self, manager):
        self.manager = manager
        self.memory = self.manager.dict()

    def set(self, token, data):
        self.memory[token] = data

    def get(self, token):
        return self.memory[token]


class Action:
    shared_memory = None

    def __init__(self, shared_memory):
        self.shared_memory = shared_memory

    def random_token(self):
        return random.randint(0, sys.maxsize)

    def push(self, name=None, token=None, data=None):
        obj = Task(token=token, data=data)
        self.shared_memory["queue"].push(obj, name=name)


class Worker:
    idx = None
    shared_memory = None

    name = "__main__"

    def __init__(self, shared_memory):
        self.idx = random.randint(0, sys.maxsize)
        self.shared_memory = shared_memory
        self.run()

    @classmethod
    def prepare(cls, _shared_memory):
        _shared_memory["queue"].create(cls.name)
        return _shared_memory

    def run(self):
        print(f"--- WORKER* --- (idx={self.idx})")
        while True:
            try:
                self.call(self.shared_memory["queue"].pull(name=self.name))
            except BaseException:
                # FIXME: worker padl!
                break

    def call(self, task: Task):
        print(f"[{self.name}:{self.idx}] HAVE -->\
\t token={task.token} \t data={task.data}")


class WorkerA(Worker):
    name = "A"
    pass


class WorkerB(Worker):
    name = "B"
    pass


class ProcessBag:
    processes = []
    shared_memory = None

    def __init__(self, shared_memory):
        self.shared_memory = shared_memory

    def register(self, cls):
        proc = multiprocessing.Process(target=cls, args=(self.shared_memory, ))
        self.shared_memory = cls.prepare(self.shared_memory)
        self.processes.append(proc)

    def run(self):
        for proc in self.processes:
            proc.start()

    def wait(self):
        for proc in self.processes:
            proc.join()


shared_memory_clean = SharedMemory()

bag = ProcessBag(shared_memory_clean)

bag.register(WorkerA)
bag.register(WorkerA)

bag.register(WorkerB)

action = Action(bag.shared_memory)

for data in range(100):
    action.push(name="A", token=action.random_token(), data=data)

bag.run()
print("--- SERVICE ---")

import time

time.sleep(2)

for data in range(100):
    action.push(name="A", token=action.random_token(), data=data)
    action.push(name="B", token=action.random_token(), data=data)

bag.wait()
