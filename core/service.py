import sys
import random
import functools
import multiprocessing

from core.action import Task, Action


class Worker:
    idx = None
    shared_memory = None
    action = None
    hooks = {}

    name = "__main__"

    def __init__(self):
        self.idx = random.randint(0, sys.maxsize)

    def connect(self, shared_memory):
        self.shared_memory = shared_memory
        self.action = Action(self.shared_memory)

    @classmethod
    def prepare(cls, _shared_memory):
        _shared_memory["queue"].create(cls.name)
        return _shared_memory

    def run(self, shared_memory):
        self.connect(shared_memory)
        print(f"--- WORKER* --- (idx={self.name}:{self.idx})")
        while True:
            try:
                self.call(self.action.pull(name=self.name))
            except BaseException:
                # FIXME: worker padl!
                break

    def call(self, task: Task):
        print(f"[\033[94m{self.name}\033[m:{str(self.idx)[0:4]}+] HAVE -->\
\t name=\033[92m{task.name}\033[m \t token={task.token} \t data={task.data}")
        try:
            self.hooks[task.name](self, task)
        except BaseException as e:
            print(f"--> \033[91mFAILED\033[m: {task.name} `{str(e)}`")

    @classmethod
    def register(cls, action_name, func):
        cls.hooks[action_name] = func


def register(worker, action_name):
    print(f"--- register={action_name} ---")

    def decorator_register(func):
        @functools.wraps(func)
        def wrapper_register(*args, **kwargs):
            value = func(*args, **kwargs)
            return value

        worker.register(action_name=action_name, func=wrapper_register)
        return wrapper_register

    return decorator_register


class Services:
    processes = []
    shared_memory = None

    def __init__(self, shared_memory):
        self.shared_memory = shared_memory

    def register(self, cls):
        proc = multiprocessing.Process(target=cls.run,
                                       args=(self.shared_memory, ))
        self.shared_memory = cls.prepare(self.shared_memory)
        self.processes.append(proc)

    def run(self):
        for proc in self.processes:
            proc.start()

    def wait(self):
        for proc in self.processes:
            proc.join()
