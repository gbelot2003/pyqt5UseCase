from ...models import Grupos, Tipos, Cuentas
from ...models.model import Session
from sqlalchemy import func, desc


def getGrupos():
    grupos = Grupos()
    return grupos.GetAll()


def getTipos():
    tipos = Tipos()
    return tipos.GetAll()


def getCuentas():
    cuentas = Cuentas()
    return cuentas.GetAll()


def getCuentasById(id):
    cuentas = Cuentas()
    return Cuentas.getById(id)


def getCuentasByGroup(grupo):
    cuentas = Cuentas()
    return Cuentas.getByGroup(grupo)


def getCuentasByGroupAndType(grupo, tipo):
    cuentas = Cuentas()
    return Cuentas.getByGroupAndType(grupo, tipo)


def getCuentasByCode(code):
    cuentas = Cuentas()
    return Cuentas.getByCode(code)


def record(tipos_id, grupo_id, cuenta, parent_id, code, descripcion):
    print(str(code) + "sadsad")
    if (parent_id != None):
        cuentas = Cuentas(int(grupo_id), int(tipos_id), parent_id,
                          int(cuenta), str(code), str(descripcion))
    else:
        cuentas = Cuentas(int(grupo_id), int(tipos_id), '',
                          int(cuenta), str(code), str(descripcion))
    session = Session()
    session.add(cuentas)
    session.commit()
    session.flush()
