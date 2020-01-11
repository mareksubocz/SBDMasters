from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.schema import Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from contrib.user.model import User


class Note(Base):

    __tablename__ = "notes"

    note_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.user_id))
    content = Column(String(512))

    user = relationship("User", back_populates="notes")
    comments = relationship("Comment")
    likes = relationship("Like")
    tags = relationship("Tag", back_populates="notes")
