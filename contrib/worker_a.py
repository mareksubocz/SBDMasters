from core.action import Task
from core.service import Worker

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

__blueprint__ = Blueprint("worker_a")


@__blueprint__.route("/worker_a")
async def worker_a(request):
    token = __blueprint__.action.random_token()
    __blueprint__.action.push(name="A", token=token, data="omg")
    return json({"result": "accepted", "token": token})


class WorkerA(Worker):
    name = "A"

    def call(self, task: Task):
        logger.info(f"[{self.name}:{self.idx}] HAVE -->\
\t token={task.token} \t data={task.data}")
        self.action.set(token=task.token, data=str(task.data) + "+AAAA")


__worker__ = WorkerA
