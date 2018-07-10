from pyramid.view import view_config

from pypi.infrastructure import cookie_auth
from pypi.services import package_service, user_service


def get_test_packages():
    return [
        {'name': 'requests', 'version': '1.2.3'},
        {'name': 'sqlalchemy', 'version': '2.0.0'},
        {'name': 'pyramid', 'version': '1.7.7'},
    ]


@view_config(route_name='home', renderer='pypi:templates/home/index.pt')
def home_index(request):
    return {
        'packages': package_service.latest_releases(),
        'package_count': package_service.package_count(),
        'release_count': package_service.release_count(),
        'user_count': user_service.user_count(),
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }


@view_config(route_name='about', renderer='pypi:templates/home/about.pt')
def home_about(request):
    return {
           'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }
