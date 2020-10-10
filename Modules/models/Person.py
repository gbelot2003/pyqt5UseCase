from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from .model import Base, engine, Session
from sqlalchemy import func


class Person(Base):
    __tablename__ = "person"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)

    def __init__(self, name: str = ''):
        self.name = name

    def Count(self):
        session = Session()
        count = session.query(func.count(Person.name)).scalar()
        session.flush()
        return count

    def GetAll(self):
        session = Session()
        return session.query(Person).all()


Base.metadata.create_all(engine)
