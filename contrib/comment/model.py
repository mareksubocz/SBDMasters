from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.schema import Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from contrib.user.model import User
from contrib.note.model import Note


class Comment(Base):

    __tablename__ = "comments"

    comment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.user_id))
    note_id = Column(Integer, ForeignKey(Note.note_id))
    content = Column(String(512))

    user = relationship("User", back_populates="comments")
