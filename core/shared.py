import multiprocessing


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
        if token in self.memory:
            return self.memory[token]
        return -1
