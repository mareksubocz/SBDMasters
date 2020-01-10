# FIXME: bash script
# https://stackoverflow.com/questions/46781471/why-postgresql-on-mac-asks-me-for-password-after-fresh-install

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SECRET_KEY = "omgomgomg"

engine = create_engine("postgres://postgres:passsword@localhost:5432/")
session = sessionmaker(bind=engine)()

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from passlib.hash import pbkdf2_sha256

from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer,
    BadSignature,
    SignatureExpired,
)

Base = declarative_base()


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(128))

    def hash_password(self, password):
        self.password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=60000):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({"id": self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = session.query(User).filter(User.id == data["id"]).first()
        return user


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
