from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, func
from .model import Base, engine, Session

class Grupos(Base):
    __tablename__ = "grupos"
    
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
        
    def __init__(self, name: str = ''):
        self.name = name
    
    def Count(self):
        session = Session()
        count = session.query(func.count(Grupos.id)).scalar()
        session.flush()
        return count
    
    def GetAll(self):
        session = Session()
        return session.query(Grupos).all()
    
    
Base.metadata.create_all(engine)