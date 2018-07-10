import os

import pypi
from pypi import DbSession
from pypi.data.packages import Package
from pypi.data.releases import Release


def main():
    init_db()
    while True:
        insert_a_package()


def insert_a_package():
    p = Package()
    p.id = input("Package name: ")
    p.summary = input("Package summary: ")
    p.author_name = input("Author name: ")
    p.author_email = input("Author email: ")
    p.license = input("license: ")

    r1 = Release()
    print("Release 1: ")
    r1.major_ver = int(input('Major version:'))
    r1.minor_ver = int(input('Minor version:'))
    r1.build_ver = int(input('Build version:'))
    r1.size = 100_000

    r2 = Release()
    print("Release 2: ")
    r2.major_ver = int(input('Major version:'))
    r2.minor_ver = int(input('Minor version:'))
    r2.build_ver = int(input('Build version:'))
    r2.size = 200_000

    p.releases.append(r1)
    p.releases.append(r2)

    session = DbSession.factory()

    session.add(p)

    session.commit()


def init_db():
    top_folder = os.path.dirname(pypi.__file__)
    rel_file = os.path.join('db', 'pypi.sqlite')
    db_file = os.path.join(top_folder, rel_file)
    DbSession.global_init(db_file)


if __name__ == '__main__':
    main()
