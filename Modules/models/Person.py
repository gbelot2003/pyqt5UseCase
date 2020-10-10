from sqlalchemy import Column, Integer, String, ForeignKey
from .model import Base, engine
from sqlalchemy.orm import sessionmaker


class Person(Base):
    __tablename__ = "person"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)

    def SessionTest(self):

        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)

        session = Session()
        user = Person()
        user.name = "alice"
        session.add(user)
        session.commit()
        session.close()

        users = session.query(Person).all()

        for user in users:
            print(user.name)

        session.close()
