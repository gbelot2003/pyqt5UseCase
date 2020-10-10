from ...models import Person, Car
from ...models.model import Session


def create(name):
    person = Person(name)
    car = Car(name)
    session = Session()
    session.add(person)
    session.add(car)
    session.commit()
    session.close()
