from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from .model import Base, engine


class Car(Base):
    __tablename__ = "car"

    id = Column('id', Integer, primary_key=True)
    parent_id = Column('parent_id', Integer, nullable=True)
    name = Column('name', String)

    def __init__(self, name: str = '', parent_id: int = ''):
        self.name = name
        self.parent_id = parent_id

    def __repr__(self):
        return f'Person(id={self.id}, name={self.name}, parent_id(self.parent_id))'


Base.metadata.create_all(engine)
