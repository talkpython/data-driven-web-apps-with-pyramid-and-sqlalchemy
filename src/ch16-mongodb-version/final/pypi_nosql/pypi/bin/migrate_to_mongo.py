import os

from pypi import DbSession
from pypi.nosql import mongo_setup

from pypi.data.users import User as SqlUser
from pypi.nosql.users import User as MongoUser

from pypi.data.packages import Package as SqlPackage
from pypi.nosql.packages import Package as MongoPackage

from pypi.data.releases import Release as SqlRelease
from pypi.nosql.releases import Release as MongoRelease


def main():
    init_dbs()
    migrate_users()
    migrate_packages()
    migrate_releases()


def migrate_users():
    if MongoUser.objects().count():
        return

    session = DbSession.factory()
    sql_users = session.query(SqlUser).all()
    for sut in sql_users:
        su: SqlUser = sut
        u = MongoUser()
        u.created_date = su.created_date
        u.hashed_password = su.hashed_password
        u.name = su.name
        u.email = su.email
        u.save()


def migrate_packages():
    if MongoPackage.objects().count():
        return

    session = DbSession.factory()
    sql_packages = session.query(SqlPackage).all()
    for sup in sql_packages:
        sp: SqlPackage = sup
        p = MongoPackage()
        p.id = sp.id
        p.created_date = sp.created_date
        p.summary = sp.summary
        p.description = sp.description
        p.home_page = sp.home_page
        p.docs_url = sp.docs_url
        p.package_url = sp.package_url

        p.author = sp.author_name
        p.author_email = sp.author_email

        p.license = sp.license
        p.maintainers = []  # Find, load, and copy over maintainer IDs.

        p.save()


def migrate_releases():
    if MongoRelease.objects().count():
        return

    session = DbSession.factory()
    sql_releases = session.query(SqlRelease).all()
    for srp in sql_releases:
        sr: SqlRelease = srp
        r = MongoRelease()
        r.created_date = sr.created_date
        r.comment = sr.comment
        r.major_ver = sr.major_ver
        r.minor_ver = sr.minor_ver
        r.build_ver = sr.build_ver
        r.url = sr.url
        r.size = sr.size
        r.package_id = sr.package_id

        r.save()


def init_dbs():
    db_file = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'db',
            'pypi.sqlite'
        ))
    DbSession.global_init(db_file)

    mongo_setup.global_init(db_name='pypi_nosql')


if __name__ == '__main__':
    main()
