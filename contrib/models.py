from sqlalchemy.schema import Table
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

association_nt_table = Table(
    "association_nt",
    Base.metadata,
    Column("note_id", Integer, ForeignKey("notes.note_id")),
    Column("tag_id", Integer, ForeignKey("tags.tag_id")),
)

association_gt_table = Table(
    "association_gt",
    Base.metadata,
    Column("group_id", Integer, ForeignKey("groups.group_id")),
    Column("tag_id", Integer, ForeignKey("tags.tag_id")),
)


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


class Note(Base):

    __tablename__ = "notes"

    note_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.user_id))
    content = Column(String(512))

    user = relationship("User", back_populates="notes")
    comments = relationship("Comment")
    likes = relationship("Like")
    tags = relationship("Tag",
                        secondary=association_nt_table,
                        back_populates="notes")


class Comment(Base):

    __tablename__ = "comments"

    comment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.user_id))
    note_id = Column(Integer, ForeignKey(Note.note_id))
    content = Column(String(512))

    user = relationship("User", back_populates="comments")


class Like(Base):

    __tablename__ = "likes"

    like_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.user_id))
    note_id = Column(Integer, ForeignKey(Note.note_id), nullable=True)
    comment_id = Column(Integer, ForeignKey(Comment.comment_id), nullable=True)
    score = Column(Integer)

    user = relationship("User", back_populates="likes")


class Tag(Base):

    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True)
    name = Column(String(512))

    notes = relationship("Note",
                         secondary=association_nt_table,
                         back_populates="tags")


class Group(Base):

    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True)
    name = Column(String(512))

    tags = relationship("Tag", secondary=association_gt_table)
