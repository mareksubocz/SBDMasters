from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from passlib.hash import pbkdf2_sha256

from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer,
    BadSignature,
    SignatureExpired,
)

Base = declarative_base()

# FIXME: LOAD FROM FILE!!!!!!!!
SECRET_KEY = "omgomgomg"


class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(128))

    notes = relationship("Note", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    likes = relationship("Like", back_populates="user")

    def hash_password(self, password):
        self.password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=60000):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({"user_id": self.user_id})

    @staticmethod
    def verify_auth_token(session, token):
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = (session.query(User).filter(
            User.user_id == data["user_id"]).first())
        return user
