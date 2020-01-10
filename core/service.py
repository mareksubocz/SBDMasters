import sys
import random
import multiprocessing

from core.action import Task, Action


class Worker:
    idx = None
    shared_memory = None
    action = None

    name = "__main__"

    def __init__(self, shared_memory):
        self.idx = random.randint(0, sys.maxsize)
        self.shared_memory = shared_memory
        self.action = Action(self.shared_memory)
        self.run()

    @classmethod
    def prepare(cls, _shared_memory):
        _shared_memory["queue"].create(cls.name)
        return _shared_memory

    def run(self):
        print(f"--- WORKER* --- (idx={self.name}:{self.idx})")
        while True:
            try:
                self.call(self.action.pull(name=self.name))
            except BaseException:
                # FIXME: worker padl!
                break

    def call(self, task: Task):
        print(f"[{self.name}:{self.idx}] HAVE -->\
\t token={task.token} \t data={task.data}")
        self.action.set(token=task.token, data=str(task.data) + "+done")


class Services:
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
