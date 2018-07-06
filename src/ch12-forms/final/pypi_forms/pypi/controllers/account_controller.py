from pyramid.view import view_config


# ################### INDEX #################################

@view_config(route_name='account_home',
             renderer='pypi:templates/account/index.pt')
def index(request):
    return {}
