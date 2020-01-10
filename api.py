from core.action import Action
from core.shared import SharedMemory
from core.service import Services

from sanic import Sanic
from sanic.log import logger
from sanic.response import json

# https://www.youtube.com/watch?v=yAv5pLO37mE

# FIXME: prefix dla workera --> kolejka / user.create_user
# FIXME: register function /?

app = Sanic(name="dev")
shared_memory_clean = SharedMemory()
services = Services(shared_memory_clean)
app.action = Action(services.shared_memory)

import importlib


def register(path):
    contrib = importlib.import_module(path)
    services.register(contrib.__worker__)
    contrib.__blueprint__.action = app.action
    app.blueprint(contrib.__blueprint__)


# FIXME: read from configuration file
register("contrib.user")
register("contrib.worker_b")


@app.route("/pull")
async def pull(request):
    # FIXME: wiele naraz zwraca? teraz tylko [0]
    token = int(request.args["token"][0])
    print(f"\033[92m------->\033[m {token}")
    data = app.action.get(token)
    return json({"result": data})


if __name__ == "__main__":
    print("--- SERVICES ---")
    services.run()
    print("--- WEBSERVER ---")
    app.run(debug=True, access_log=True, host="0.0.0.0", port=8000)
    services.wait()  # FIXME: health check?
