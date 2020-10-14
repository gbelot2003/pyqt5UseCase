from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, func
from .model import Base, engine, Session

class Cuentas(Base):
    __tablename__ = "cuentas"
    
    id = Column('id', Integer, primary_key=True)
    grupo_id = Column('grupo_id', Integer, nullable=False)
    tipo_id = Column('tipo_id', Integer, nullable=False)
    partent_id = Column('parent_id', Integer)
    cuenta = Column('cuenta', Integer, nullable=False)
    code = Column('code', String, nullable=False)
    descripcion = Column('descripcion', String, nullable=False)
    
    def __init__(self, grupo_id: int = '', tipo_id: int = '', parent_id: int = '', cuenta: int = '', code: str = '', descripcion: str = ''):
        self.grupo_id = grupo_id
        self.tipo_id = tipo_id
        self.partent_id = parent_id
        self.cuenta = cuenta
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
    def getByType(num):
        #print("asdasd" +  str(num))
        session = Session()
        return session.query(Cuentas).filter(Cuentas.tipo_id == num)
        
    
Base.metadata.create_all(engine)
