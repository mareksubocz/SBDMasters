from core.action import Task
from core.service import Worker, register

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

NAME = "user"

# FIXME: jako folder (api.py umie importowac)
# FIXME: action_create.py? kazda w osobym pliku
# FIXME: jak potrzebna pamiec to odpowiednie inity w UserWorker?


class UserWorker(Worker):
    name = NAME


__hook__ = Blueprint(NAME)
__worker__ = UserWorker()

# --- CREATE ---


@__hook__.route("/user/create", methods=["POST"])
async def hook_user_create(request):
    token = __hook__.action.random_token()

    # FIXME: filter / extension/python package
    # trzeba tu oczyscic to wszystko i wyslac tylko to co potrzebne
    # no i zabezpiecznie

    print(request.json)

    __hook__.action.push(name="user.create", token=token, data=request.json)
    return json({"result": "accepted", "token": token})


# FIXME: special function to create 'RESPONSE' like
#         abort(400, message="Couldn't create the user, missing params")

from test_sql import User


@register(__worker__, "user.create")
def user_create(worker, task: Task):
    username = task.data["username"]
    password = task.data["password"]

    print(f"username={username}")
    print(f"password={password}")

    if username is None or password is None:
        worker.action.set(token=task.token,
                          data="Couldn't create the user, missing params")
        return
    if (worker.shared_memory["session"].query(User).filter_by(
            username=username).first() is not None):
        worker.action.set(token=task.token, data="User already exist")
        return

    user = User(username=username)
    user.hash_password(password)
    worker.shared_memory["session"].add(user)
    worker.shared_memory["session"].commit()

    reged_user = (worker.shared_memory["session"].query(User).filter(
        User.username == username).first())
    if not reged_user:
        worker.action.set(token=task.token, data="Error while creating user")

    worker.action.set(token=task.token, data="User created")


# --- DELETE ---


@__hook__.route("/user/delete")
async def hook_user_delete(request):
    token = __hook__.action.random_token()
    __hook__.action.push(name="user.delete", token=token, data="lorem")
    return json({"result": "accepted", "token": token})


@register(__worker__, "user.delete")
def user_delete(worker, task: Task):
    worker.action.set(token=task.token, data=str(task.data) + "+deleted")
