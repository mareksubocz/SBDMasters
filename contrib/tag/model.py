from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.schema import Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Tag(Base):

    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True)
    name = Column(String(512))

    notes = relationship("Note", back_populates="tags")
