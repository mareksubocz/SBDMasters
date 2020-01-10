from core.action import Task
from core.service import Worker

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

app = Blueprint("worker_b")


@app.route("/worker_b")
async def worker_b(request):
    token = app.action.random_token()
    app.action.push(name="B", token=token, data="bbb")
    return json({"result": "accepted", "token": token})


class WorkerB(Worker):
    name = "B"

    def call(self, task: Task):
        logger.info(f"[{self.name}:{self.idx}] HAVE -->\
\t token={task.token} \t data={task.data}")
        self.action.set(token=task.token, data=str(task.data) + "+BBBB")


__blueprint__ = app
__worker__ = WorkerB()
