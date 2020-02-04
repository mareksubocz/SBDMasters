from core.action import Task
from core.service import Worker, register

from contrib.models import User


# FIXME: jak potrzebna pamiec to odpowiednie inity w UserWorker?
class UserWorker(Worker):
    name = "user"


__worker__ = UserWorker

# --- CREATE ---

# FIXME: special function to create 'RESPONSE' like
#         abort(400, message="Couldn't create the user, missing params")


@register(__worker__, "user.create")
def user_create(worker, task: Task):
    username = task.data["username"]
    password = task.data["password"]
    name = task.data["name"]

    print(f"username={username}")
    print(f"password={password}")
    print(f"name={name}")

    if username is None or password is None or name is None:
        worker.action.set(
            token=task.token, data="Couldn't create the user, missing params"
        )
        return
    if (
        worker.shared_memory["session"]
        .query(User)
        .filter_by(username=username)
        .first()
        is not None
    ):
        worker.action.set(token=task.token, data="User already exist")
        return

    user = User(username=username, name=name)
    user.hash_password(password)
    worker.shared_memory["session"].add(user)
    worker.shared_memory["session"].commit()

    reged_user = (
        worker.shared_memory["session"]
        .query(User)
        .filter(User.username == username)
        .first()
    )
    if not reged_user:
        worker.action.set(token=task.token, data="Error while creating user")

    worker.action.set(token=task.token, data="User created")


# --- TOKEN ---


@register(__worker__, "user.token")
def user_token(worker, task: Task):
    username = task.data["username"]
    password = task.data["password"]

    print(f"username={username}")
    print(f"password={password}")

    user = (
        worker.shared_memory["session"]
        .query(User)
        .filter(User.username == username)
        .first()
    )

    if not user or not user.verify_password(password):
        worker.action.set(token=task.token, data="Wrong password")
        print("WRONG PASSWORD")
        return

    auth_token = user.generate_auth_token().decode("ascii")
    worker.action.set(token=task.token, data={"auth_token": auth_token})
    print("SENDING AUTH_TOKEN")


# --- PROFILE ---


@register(__worker__, "user.profile")
def user_profile(worker, task: Task):
    username = task.data["username"]

    print(f"username={username}")

    user = (
        worker.shared_memory["session"]
        .query(User)
        .filter(User.username == username)
        .first()
    )

    print("----------------->", user.notes)
    worker.action.set(token=task.token, data="lol")


# --- DEBUG ---


@register(__worker__, "user.debug")
def user_profile(worker, task: Task):
    from time import sleep

    sleep(3)
    worker.action.set(token=task.token, data="lol")
