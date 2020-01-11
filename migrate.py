# FIXME: bash script
# https://stackoverflow.com/questions/46781471/why-postgresql-on-mac-asks-me-for-password-after-fresh-install

from core.shared import PostgreSQLDatabase
from sqlalchemy.ext.declarative import declarative_base

Engine = PostgreSQLDatabase(engine_only=True)

from contrib.models import Base, User, Note, Comment, Like, Tag, Group

if __name__ == "__main__":
    print("start")
    Base.metadata.drop_all(Engine)
    Base.metadata.create_all(Engine)
    print("end")
