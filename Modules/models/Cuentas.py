from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, func
from .model import Base, engine, Session

class Cuentas(Base):
    __tablename__ = "cuentas"
    
    id = Column('id', Integer, primary_key=True)
    grupo_id = Column('grupo_id', Integer)
    tipo_id = Column('tipo_id', Integer)
    partent_id = Column('parent_id', Integer)
    code = Column('code', Integer)
    descripcion = Column('descripcion', String)
    
    def __init__(self, grupo_id: int = '', tipo_id: int = '', parent_id: int = '', code: int = '', descripcion: str = ''):
        self.grupo_id = grupo_id
        self.tipo_id = tipo_id
        self.partent_id = parent_id
        self.code = code
        self.descripcion = descripcion
        
    def Count(self):
        session = Session()
        count = session.query(func.count(Cuentas.id)).scalar()
        session.flush()
        return count
    
    def GetAll(self):
        session = Session()
        return session.query(Cuentas).all()
    
    @staticmethod
    def getByType():
        #print("asdasd")
        session = Session()
        return session.query(Cuentas).all()
        
    
Base.metadata.create_all(engine)