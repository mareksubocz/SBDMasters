from core.action import Task
from core.service import Worker

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

NAME = "user"

app = Blueprint(NAME)


@app.route("/user/create")
async def user_create(request):
    token = app.action.random_token()
    app.action.push(name="user.create", token=token, data="lorem")
    return json({"result": "accepted", "token": token})


@app.route("/user/delete")
async def user_delete(request):
    token = app.action.random_token()
    app.action.push(name="user.delete", token=token, data="lorem")
    return json({"result": "accepted", "token": token})


class UserWorker(Worker):
    name = NAME

    def call(self, task: Task):
        logger.info(f"[{self.name}:{self.idx}] HAVE -->\
\t token={task.token} \t data={task.data}")

        # FIXME: jakas pseudo-automatyczna klasa?
        if task.name == "user.create":
            self.user_create(task)
        if task.name == "user.delete":
            self.user_delete(task)

    def user_create(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+created")

    def user_delete(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+deleted")


__blueprint__ = app
__worker__ = UserWorker
