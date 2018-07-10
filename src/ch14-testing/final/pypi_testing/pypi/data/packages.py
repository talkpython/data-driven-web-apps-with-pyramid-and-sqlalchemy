import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm
from pypi.data.modelbase import SqlAlchemyBase
from pypi.data.releases import Release


class Package(SqlAlchemyBase):
    __tablename__ = 'packages'

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    last_updated = sa.Column(sa.DateTime, default=datetime.datetime.now)
    summary = sa.Column(sa.String, nullable=True)
    description = sa.Column(sa.String, nullable=True)

    home_page = sa.Column(sa.String, nullable=True)
    docs_url = sa.Column(sa.String, nullable=True)
    package_url = sa.Column(sa.String, nullable=True)

    author_name = sa.Column(sa.String, nullable=True)
    author_email = sa.Column(sa.String, nullable=True, index=True)

    license = sa.Column(sa.String, index=True)

    releases = orm.relation("Release", order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc(),
    ], back_populates='package')

    def __repr__(self):
        return '<Package {}>'.format(self.id)
