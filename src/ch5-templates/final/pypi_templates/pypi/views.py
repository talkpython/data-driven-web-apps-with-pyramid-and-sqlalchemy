from pyramid.view import view_config


def get_test_packages():
    return [
        {'name': 'requests', 'version': '1.2.3'},
        {'name': 'sqlalchemy', 'version': '2.0.0'},
        {'name': 'pyramid', 'version': '1.7.7'},
    ]


@view_config(route_name='home', renderer='templates/home_index.pt')
def home_index(request):
    return {
        'packages': get_test_packages()
    }
