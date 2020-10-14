from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, func
from .model import Base, engine, Session

class Tipos(Base):
    __tablename__ = "tipos"
    
    id = Column('id', Integer, primary_key=True)
    code = Column('code', Integer)
    name = Column('name', String)

    def __init__(self, code: str = '', name: str = ''):
        self.code = code
        self.name = name
        
    def __repr__(self):
        return f'Tipos(id={self.id}, name={self.name}, code={self.code})'
    
    def Count(self):
        session = Session()
        count = session.query(func.count(Tipos.id)).scalar()
        session.flush()
        return count
    
    def GetAll(self):
        session = Session()
        return session.query(Tipos).all()
    
   
Base.metadata.create_all(engine)