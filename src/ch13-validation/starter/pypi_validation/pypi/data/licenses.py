import datetime
import sqlalchemy
from pypi.data.modelbase import SqlAlchemyBase


class License(SqlAlchemyBase):
    __tablename__ = 'licenses'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    description = sqlalchemy.Column(sqlalchemy.String)
