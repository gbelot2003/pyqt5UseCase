from marshmallow_sqlalchemy import SQLAlchemySchema

from .db import Session


class BaseSchema(SQLAlchemySchema):
    class Meta:
        sqla_session = Session
