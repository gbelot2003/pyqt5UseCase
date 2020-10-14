from ...models import Grupos, Tipos
from ...models.model import Session
from sqlalchemy import func, desc

def getGrupos():
    grupos = Grupos()
    return grupos.GetAll()

def getTipos():
    tipos = Tipos()
    return tipos.GetAll()