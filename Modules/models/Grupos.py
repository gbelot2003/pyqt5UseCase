from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from .model import Base, engine

class Grupos():
    __table__ = "grupos"
    
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
        
    def __init__(self, name: str = ''):
        self.name = name

    def __repr__(self):
        return f'Grupos(id={self.id}, name={self.name})'
    
    def Count(self):
        session = Session()
        count = session.query(func.count(Grupos.id)).scalar()
        session.flush()
        return count
    
    def GetAll(self):
        self.query.all()
    
    def findById(self, id):
        self.query.get(id)
    
    Base.metadata.create_all(engine)