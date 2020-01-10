from core.action import Task
from core.service import Worker

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

NAME = "group"

app = Blueprint(NAME)


@app.route("/group/save")
async def group_create(request):
    token = app.action.random_token()
    app.action.push(name="group.save", token=token,
                    data={"name": "Scheduling"})
    return json({"result": "accepted", "token": token})


@app.route("/group/delete")
async def group_delete(request):
    token = app.action.random_token()
    app.action.push(name="group.delete", token=token,
                    data={"group_id": "1234"})
    return json({"result": "accepted", "token": token})


@app.route("/group/edit")
async def group_edit(request):
    token = app.action.random_token()
    app.action.push(name="group.edit", token=token,
                    data={"name": "ML",
                          "group_id": "1234"})
    return json({"result": "accepted", "token": token})


class GroupWorker(Worker):
    name = NAME

    def call(self, task: Task):
        logger.info(f"[{self.name}:{self.idx}] HAVE -->\
\t token={task.token} \t data={task.data}")

        if task.name == "group.create":
            self.group_create(task)
        if task.name == "group.delete":
            self.group_delete(task)
        if task.name == "group.edit":
            self.group_edit(task)

    def group_create(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+created")

    def group_delete(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+deleted")

    def group_edit(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+edited")


__blueprint__ = app
__worker__ = GroupWorker
