from core.action import Task
from core.service import Worker, register

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

NAME = "user"

app = Blueprint(NAME)


class UserWorker(Worker):
    name = NAME


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


__blueprint__ = app
__worker__ = UserWorker()


@register(__worker__, "user.create")
def user_create(worker, task: Task):
    worker.action.set(token=task.token, data=str(task.data) + "+created")


@register(__worker__, "user.delete")
def user_delete(worker, task: Task):
    worker.action.set(token=task.token, data=str(task.data) + "+deleted")
