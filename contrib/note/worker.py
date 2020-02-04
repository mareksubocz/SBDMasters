from core.action import Task
from core.service import Worker, register

from contrib.models import User

# FIXME: jak potrzebna pamiec to odpowiednie inity w UserWorker?
class NoteWorker(Worker):
    name = "note"


__worker__ = NoteWorker

# --- CREATE ---


@register(__worker__, "note.create")
def note_create(worker, task: Task):
    username = task.data["username"]
    content = task.data["content"]

    print(f"username={username}")
    print(f"content={content}")

    if username is None or content is None:
        worker.action.set(
            token=task.token, data="Couldn't create the note, missing params"
        )
        return

    user = (
        worker.shared_memory["session"]
        .query(User)
        .filter(User.username == username)
        .first()
    )

    note = Note(user=user, content=content)
    worker.shared_memory["session"].add(note)
    worker.shared_memory["session"].commit()

    worker.action.set(token=task.token, data="Note created")
