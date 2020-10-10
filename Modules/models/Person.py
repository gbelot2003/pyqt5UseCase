from sqlalchemy import Column, Integer, String, ForeignKey
from .model import Base, engine
from sqla_softdelete import SoftDeleteMixin


class Person(SoftDeleteMixin, Base):
    __tablename__ = "person"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)

    def __init__(self, name: str = ''):
        self.name = name

    def __repr__(self):
        return f'Person(id={self.id}, name={self.name})'
