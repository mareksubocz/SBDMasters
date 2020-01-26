import sys
import random
from dataclasses import dataclass


@dataclass
class Task:
    name: str
    token: int
    data: object


"""
@dataclass
class Response:
    # FIXME: pole task?
    code: int
    data: object


# FIXME: create_response()? dla api?
# z data? statusem? kodem?
"""


class Action:
    shared_memory = None
    maxsize = 6666666666

    def __init__(self, shared_memory):
        self.shared_memory = shared_memory

    def random_token(self):
        return random.randint(0, Action.maxsize)
        # return random.randint(0, sys.maxsize)

    def push(self, name=None, token=None, data=None):
        obj = Task(name=name, token=token, data=data)
        self.shared_memory["queue"].push(obj, name=name.split(".")[0])

    def pull(self, name=None):
        return self.shared_memory["queue"].pull(name=name)

    def set(self, token=None, data=None):
        self.shared_memory["hashmap"].set(token, data)

    def get(self, token=None):
        return self.shared_memory["hashmap"].get(token)
