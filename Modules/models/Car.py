from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from .model import Base, engine


class Car(Base):
    __tablename__ = "car"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)

    def __init__(self, name: str = ''):
        self.name = name

    def __repr__(self):
        return f'Person(id={self.id}, name={self.name})'


Base.metadata.create_all(engine)
