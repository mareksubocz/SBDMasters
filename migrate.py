# FIXME: bash script
# https://stackoverflow.com/questions/46781471/why-postgresql-on-mac-asks-me-for-password-after-fresh-install

from core.shared import PostgreSQLDatabase
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Engine = PostgreSQLDatabase()

from contrib.user.model import User

if __name__ == "__main__":
    Base.metadata.drop_all(Engine)
    Base.metadata.create_all(Engine)
