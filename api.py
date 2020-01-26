from core.action import Action
from core.shared import SharedMemory
from core.service import Services

from sanic import Sanic
from sanic.log import logger
from sanic.response import json

# https://www.youtube.com/watch?v=yAv5pLO37mE

app = Sanic(name="dev")
shared_memory_clean = SharedMemory()
services = Services(shared_memory_clean)
app.action = Action(services.shared_memory)

import importlib


def register(path, num_count=1):
    contrib = importlib.import_module(path)
    for _ in range(num_count):
        # FIXME: tutaj allocuj a nie w pliku! (instacja)
        services.register(contrib.__worker__())
    contrib.__hook__.action = app.action
    app.blueprint(contrib.__hook__)


# FIXME: metoda sanitizyacji wiadomosci w kolejce i hashmapie?????

# FIXME: read from configuration file
register("contrib.user", num_count=3)
register("contrib.worker_b")
register("contrib.note")
register("contrib.tag")
register("contrib.group")


# FIXME: move to core?
@app.route("/pull", methods=["GET", "POST"])
async def pull(request):
    # FIXME: wiele naraz zwraca? teraz tylko [0]
    # FIXME: mozliwosc robienia tu post hook-a????? dla modulow
    #        naprzyklad dla nadania auth_token
    # FIXME: -1 (odrzucony) -2 (przetwarzany) + gdy timeout
    if "token" not in request.json:
        print("\033[91mTOKEN EMPTY\033[m")
        return json(
            {"result": "declined"}, headers={"Access-Control-Allow-Origin": "*"}
        )
    token = int(request.json["token"][0])
    print(f"\033[92m------->\033[m {token}")
    data = app.action.get(token)
    response = json(
        {"result": data}, headers={"Access-Control-Allow-Origin": "*"}
    )
    if isinstance(data, dict) and "auth_token" in data:
        response.cookies["auth_token"] = data["auth_token"]
    return response


if __name__ == "__main__":
    print("--- SERVICES ---")
    services.run()
    print("--- WEBSERVER ---")
    app.run(debug=True, access_log=True, host="0.0.0.0", port=8000)
    services.wait()  # FIXME: health check?
