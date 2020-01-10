from core.action import Task
from core.service import Worker

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

NAME = "note"

app = Blueprint(NAME)


@app.route("/note/save")
async def note_save(request):
    token = app.action.random_token()
    app.action.push(name="note.save", token=token,
                    data={"url": "https://www.example.com",
                          "user_id": "1234"})
    return json({"result": "accepted", "token": token})


@app.route("/note/delete")
async def note_delete(request):
    token = app.action.random_token()
    app.action.push(name="note.delete", token=token,
                    data={"url_id": "1234"})
    return json({"result": "accepted", "token": token})


@app.route("/note/edit")
async def note_edit(request):
    token = app.action.random_token()
    app.action.push(name="note.edit", token=token,
                    data={"url": "https://www.google.com",
                          "url_id": "1234"})
    return json({"result": "accepted", "token": token})


class NoteWorker(Worker):
    name = NAME

    def call(self, task: Task):
        logger.info(f"[{self.name}:{self.idx}] HAVE -->\
\t token={task.token} \t data={task.data}")

        if task.name == "note.save":
            self.note_save(task)
        if task.name == "note.delete":
            self.note_delete(task)
        if task.name == "note.edit":
            self.note_edit(task)

    def note_save(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+saved")

    def note_delete(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+deleted")

    def note_edit(self, task: Task):
        self.action.set(token=task.token, data=str(task.data) + "+edited")


__blueprint__ = app
__worker__ = NoteWorker
