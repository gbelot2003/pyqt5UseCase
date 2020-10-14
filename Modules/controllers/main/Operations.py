from ...models import Person
from ...models.model import Session
from sqlalchemy import func, desc


def Count():
    person = Person()
    return person.Count()


def GetAll():
    person = Person()
    return person.GetAll()


def create(name):
    person = Person(name)
    session = Session()
    session.add(person)
    session.commit()
    session.close()
