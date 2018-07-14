from typing import List, Optional

from pypi.nosql.packages import Package
from pypi.nosql.releases import Release


def package_count() -> int:
    return Package.objects().count()


def release_count() -> int:
    return Release.objects().count()


def latest_releases(limit=10) -> List[Package]:
    releases = Release.objects() \
        .order_by('-created_date') \
        .limit(limit * 2)

    packages_in_order = [r.package_id for r in releases]
    package_ids = set(packages_in_order)

    packages = {p.id: p for p in Package.objects(id__in=package_ids)}

    results = []
    for r in releases:
        if len(results) >= limit:
            break

        results.append(packages[r.package_id])

    return results


def find_package_by_name(package_name: str) -> Optional[Package]:
    return Package.objects(id=package_name).first()


def find_releases_for_package(package_name: str) -> List[Release]:
    return Release.objects(package_id=package_name)\
        .order_by('-major_ver', '-minor_ver', '-build_ver') \
        .all()


def all_packages(limit: int) -> List[Package]:
    return list(Package.objects().limit(limit))
