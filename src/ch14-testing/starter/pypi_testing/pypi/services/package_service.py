from typing import List, Optional

from sqlalchemy.orm import subqueryload, joinedload

from pypi import DbSession
from pypi.data.packages import Package
from pypi.data.releases import Release


def package_count() -> int:
    session = DbSession.factory()
    return session.query(Package).count()


def release_count() -> int:
    session = DbSession.factory()
    return session.query(Release).count()


def latest_releases(limit=10) -> List[Package]:
    session = DbSession.factory()

    releases = session.query(Release) \
        .order_by(Release.created_date.desc()) \
        .limit(limit * 2)

    packages_in_order = [r.package_id for r in releases]
    package_ids = set(packages_in_order)

    packages = {p.id: p for p in session.query(Package).filter(Package.id.in_(package_ids))}

    results = []
    for r in releases:
        if len(results) >= limit:
            break

        results.append(packages[r.package_id])

    return results


def find_package_by_name(package_name: str) -> Optional[Package]:
    session = DbSession.factory()

    # .options(subqueryload(Package.releases))

    return session.query(Package) \
        .filter(Package.id == package_name) \
        .first()
