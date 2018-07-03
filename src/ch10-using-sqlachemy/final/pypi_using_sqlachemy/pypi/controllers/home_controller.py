from pyramid.view import view_config
from pypi.services import package_service, user_service


def get_test_packages():
    return [
        {'name': 'requests', 'version': '1.2.3'},
        {'name': 'sqlalchemy', 'version': '2.0.0'},
        {'name': 'pyramid', 'version': '1.7.7'},
    ]


@view_config(route_name='home', renderer='pypi:templates/home/index.pt')
def home_index(_):
    return {
        'packages': get_test_packages(),
        'package_count': package_service.package_count(),
        'release_count': package_service.release_count(),
        'user_count': user_service.user_count(),
    }


@view_config(route_name='about', renderer='pypi:templates/home/about.pt')
def home_about(_):
    return {}
