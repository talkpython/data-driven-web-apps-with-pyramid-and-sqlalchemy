import datetime
import sqlalchemy
from pypi.data.modelbase import SqlAlchemyBase


class Auditing(SqlAlchemyBase):
    __tablename__ = 'auditing'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    description = sqlalchemy.Column(sqlalchemy.String)
