from core.service import Worker, Services
from core.action import Task, Action
from core.shared import SharedMemory

from sanic import Sanic
from sanic.log import logger
from sanic.response import json

# https://www.youtube.com/watch?v=yAv5pLO37mE

# FIXME: blueprints
# FIXME: prefix dla workera --> kolejka / user.create_user


class WorkerA(Worker):
    name = "A"
    pass


class WorkerB(Worker):
    name = "B"

    def call(self, task: Task):
        logger.info(f"[{self.name}:{self.idx}] HAVE -->\
\t token={task.token} \t data={task.data}")
        self.action.set(token=task.token, data=str(task.data) + "+BBBB")


app = Sanic()
shared_memory_clean = SharedMemory()
services = Services(shared_memory_clean)

services.register(WorkerA)
services.register(WorkerA)
services.register(WorkerB)

action = Action(services.shared_memory)


@app.route("/worker_a")
async def worker_a(request):
    token = action.random_token()
    action.push(name="A", token=token, data="omg")
    return json({"result": "accepted", "token": token})


@app.route("/worker_b")
async def worker_b(request):
    token = action.random_token()
    action.push(name="B", token=token, data="omg")
    return json({"result": "accepted", "token": token})


@app.route("/pull")
async def pull(request):
    # FIXME: wiele naraz zwraca? teraz tylko [0]
    token = int(request.args["token"][0])
    print(f"\033[92m------->\033[m {token}")
    data = action.get(token)
    return json({"result": data})


if __name__ == "__main__":
    print("--- SERVICES ---")
    services.run()
    print("--- WEBSERVER ---")
    app.run(debug=True, access_log=True, host="0.0.0.0", port=8000)
    services.wait()  # FIXME: health check?
