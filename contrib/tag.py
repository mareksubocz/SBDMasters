from core.action import Task
from core.service import Worker

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

NAME = "tag"

app = Blueprint(NAME)


@app.route("/tag/create")
async def tag_create(request):
    token = app.action.random_token()
    app.action.push(name="tag.create", token=token,
                    data={"tag": "funny"})
    return json({"result": "accepted", "token": token})


@app.route("/tag/delete")
async def tag_delete(request):
    token = app.action.random_token()
    app.action.push(name="tag.delete", token=token,
                    data={"tag_id": "2134"})
    return json({"result": "accepted", "token": token})


@app.route("/tag/add/note")
async def tag_add_note(request):
    token = app.action.random_token()
    app.action.push(name="tag.add.note", token=token,
                    data={"tag": "funny",
                          "note_id": "4321"})
    return json({"result": "accepted", "token": token})


@app.route("/tag/add/group")
async def tag_add_group(request):
    token = app.action.random_token()
    app.action.push(name="tag.add.group", token=token,
                    data={"tag": "funny",
                          "group_id": "4321"})
    return json({"result": "accepted", "token": token})


@app.route("/tag/remove/note")
async def tag_remove_note(request):
    token = app.action.random_token()
    app.action.push(name="tag.remove.note", token=token,
                    data={"tag_id": "746",
                          "note_id": "4321"})
    return json({"result": "accepted", "token": token})


@app.route("/tag/remove/group")
async def tag_remove_group(request):
    token = app.action.random_token()
    app.action.push(name="tag.remove.group", token=token,
                    data={"tag_id": "746",
                          "group_id": "4321"})
    return json({"result": "accepted", "token": token})


class TagWorker(Worker):
    name = NAME

    def call(self, task: Task):
        logger.info(f"[{self.name}:{self.idx}] HAVE -->\
\t token={task.token} \t data={task.data}")

        if task.name == "tag.create":
            self.tag_create(task)
        if task.name == "tag.delete":
            self.tag_delete(task)
        if task.name == "tag.add.note":
            self.tag_add_note(task)
        if task.name == "tag.add.group":
            self.tag_add_group(task)
        if task.name == "tag.remove.note":
            self.tag_remove_note(task)
        if task.name == "tag.remove.group":
            self.tag_remove_group(task)

    def tag_create(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+created")

    def tag_delete(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+deleted")

    def tag_add_note(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+added")

    def tag_add_group(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+added")

    def tag_remove_note(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+removed")

    def tag_remove_group(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+removed")


__blueprint__ = app
__worker__ = TagWorker
