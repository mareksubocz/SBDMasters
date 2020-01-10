import sys
import random
from dataclasses import dataclass


@dataclass
class Task:
    token: int
    data: object


class Action:
    shared_memory = None

    def __init__(self, shared_memory):
        self.shared_memory = shared_memory

    def random_token(self):
        return random.randint(0, sys.maxsize)

    def push(self, name=None, token=None, data=None):
        obj = Task(token=token, data=data)
        self.shared_memory["queue"].push(obj, name=name)

    def pull(self, name=None):
        return self.shared_memory["queue"].pull(name=name)

    def set(self, token=None, data=None):
        self.shared_memory["hashmap"].set(token, data)

    def get(self, token=None):
        return self.shared_memory["hashmap"].get(token)
