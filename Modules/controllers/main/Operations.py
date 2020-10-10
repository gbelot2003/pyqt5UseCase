from ...models import Person, Car
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
    car = Car(name)
    session = Session()
    session.add(person)
    session.add(car)
    session.commit()
    session.close()
