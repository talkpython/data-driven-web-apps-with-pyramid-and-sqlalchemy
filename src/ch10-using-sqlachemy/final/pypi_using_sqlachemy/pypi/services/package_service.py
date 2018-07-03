from typing import List

from pypi import DbSession
from pypi.data.packages import Package
from pypi.data.releases import Release


def package_count() -> int:
    session = DbSession.factory()
    return session.query(Package).count()


def release_count() -> int:
    session = DbSession.factory()
    return session.query(Release).count()


