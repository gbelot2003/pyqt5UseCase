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

def getCuentasByType(type):
    cuentas = Cuentas()
    return cuentas.getByType(type)
