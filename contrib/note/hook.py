from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

from contrib.user.decorator import auth_verify

__hook__ = Blueprint("note")

# --- CREATE ---


@__hook__.route("/note/create", methods=["POST"])
async def hook_note_create(request):
    username = request.json["username"]

    if not auth_verify(
        __hook__.action.shared_memory["session"], request, username=username
    ):
        print("DECLINED")
        return json(
            {"result": "declined", "message": "Not logged in"},
            headers={"Access-Control-Allow-Origin": "*"},
        )

    token = __hook__.action.random_token()

    # FIXME: filter / extension/python package
    # trzeba tu oczyscic to wszystko i wyslac tylko to co potrzebne
    # no i zabezpiecznie

    print(request.json)  # username + password

    __hook__.action.push(name="note.create", token=token, data=request.json)
    return json(
        {"result": "accepted", "token": token},
        headers={"Access-Control-Allow-Origin": "*"},
    )
