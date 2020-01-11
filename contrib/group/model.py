from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.schema import Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table = Table(
    "association",
    Base.metadata,
    Column("group_id", Integer, ForeignKey("groups.group_id")),
    Column("tag_id", Integer, ForeignKey("tags.tag_id")),
)


class Group(Base):

    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True)
    name = Column(String(512))

    tags = relationship("Tag", secondary=association_table)
