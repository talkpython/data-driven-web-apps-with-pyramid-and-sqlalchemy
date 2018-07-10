from pyramid.view import view_config
from pyramid.request import Request
import pyramid.httpexceptions as x

from pypi.infrastructure import cookie_auth
from pypi.services import package_service


@view_config(route_name='package_details',
             renderer='pypi:templates/packages/details.pt')
@view_config(route_name='package_details/',
             renderer='pypi:templates/packages/details.pt')
def details(request: Request):
    package_name = request.matchdict.get('package_name')

    package = package_service.find_package_by_name(package_name)
    if not package:
        raise x.HTTPNotFound()

    latest_version = '0.0.0'
    latest_release = None
    if package.releases:
        latest_release = package.releases[0]
        latest_version = '{}.{}.{}'.format(
            latest_release.major_ver,
            latest_release.minor_ver,
            latest_release.build_ver
        )

    return {
        'package': package,
        'latest_version': latest_version,
        'latest_release': latest_release,
        'release_version': latest_version,
        'maintainers': [],
        'is_latest': True,
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }


# /{num}
@view_config(route_name='popular',
             renderer='pypi:templates/packages/details.pt')
def popular(request: Request):
    num = int(request.matchdict.get('num', -1))
    if not (1 <= num or num <= 10):
        raise x.HTTPNotFound()

    return {
        'package_name': "The {}th popular package".format(num),
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }
