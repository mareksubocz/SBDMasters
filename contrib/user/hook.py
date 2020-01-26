from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

from contrib.user.decorator import auth_verify

__hook__ = Blueprint("user")

# --- CREATE ---


@__hook__.route("/user/create", methods=["POST"])
async def hook_user_create(request):
    token = __hook__.action.random_token()

    # FIXME: filter / extension/python package
    # trzeba tu oczyscic to wszystko i wyslac tylko to co potrzebne
    # no i zabezpiecznie

    print(request.json)  # username + password

    __hook__.action.push(name="user.create", token=token, data=request.json)
    return json(
        {"result": "accepted", "token": token},
        headers={"Access-Control-Allow-Origin": "*"},
    )


# --- TOKEN ---


@__hook__.route("/user/token", methods=["POST"])
async def hook_user_token(request):
    token = __hook__.action.random_token()

    print(request.json)  # username + password

    __hook__.action.push(name="user.token", token=token, data=request.json)
    return json(
        {"result": "accepted", "token": token},
        headers={"Access-Control-Allow-Origin": "*"},
    )


# --- PROFILE ---


@__hook__.route("/user/profile")
async def hook_user_profile(request):
    token = __hook__.action.random_token()

    print(request.json)  # username

    __hook__.action.push(name="user.profile", token=token, data=request.json)
    return json(
        {"result": "accepted", "token": token},
        headers={"Access-Control-Allow-Origin": "*"},
    )


# --- CHECK ---


@__hook__.route("/user/check", methods=["POST"])
async def hook_user_check(request):
    if not auth_verify(__hook__.action.shared_memory["session"], request):
        print("DECLINED")
        return json(
            {"result": "declined", "message": "Not logged in"},
            headers={"Access-Control-Allow-Origin": "*"},
        )
    print(request.json)  # username + password
    print("ACCEPTED")
    return json(
        {"result": "accepted"}, headers={"Access-Control-Allow-Origin": "*"}
    )
