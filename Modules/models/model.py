from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///Modules/models/users.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
