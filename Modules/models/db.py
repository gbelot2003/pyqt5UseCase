import sqlalchemy as sa
from sqlalchemy import orm

Session = orm.scoped_session(orm.sessionmaker())
Session.configure(bind=engine)
