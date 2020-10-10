from sqlalchemy import Column, Integer, String, ForeignKey
from .model import Base, engine
from sqlalchemy.orm import sessionmaker


class Person(Base):
    __tablename__ = "person"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)

    