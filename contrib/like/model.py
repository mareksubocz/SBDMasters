from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.schema import Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from contrib.user.model import User
from contrib.note.model import Note
from contrib.comment.model import Comment


class Like(Base):

    __tablename__ = "likes"

    like_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.user_id))
    note_id = Column(Integer, ForeignKey(Note.note_id), nullable=True)
    comment_id = Column(Integer, ForeignKey(Comment.comment_id), nullable=True)
    score = Column(Integer)

    user = relationship("User", back_populates="likes")
