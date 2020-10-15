from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, func, desc
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
        return session.query(func.count(Cuentas.id)).scalar()

    def GetAll(self):
        session = Session()
        return session.query(Cuentas).all()

    def GetCuentasFilter(self):
        session = Session()
        return session.query(Cuentas).order_by(Cuentas.code.desc())

    @staticmethod
    def getById(id):
        session = Session()
        return session.query(Cuentas).filter_by(id=id).first()

    @staticmethod
    def getByType(num):
        #print("asdasd" +  str(num))
        session = Session()
        return session.query(Cuentas).filter(Cuentas.tipo_id == num)

    @staticmethod
    def getByGroup(num):
        session = Session()
        return session.query(Cuentas).filter(Cuentas.grupo_id == num)

    @staticmethod
    def getByGroupAndType(grupo, tipo):
        session = Session()
        return session.query(Cuentas).filter(Cuentas.grupo_id == grupo).filter(Cuentas.tipo_id == tipo)

    @staticmethod
    def getByCode(code):
        session = Session()
        return session.query(Cuentas).filter_by(code=code).first()


Base.metadata.create_all(engine)
