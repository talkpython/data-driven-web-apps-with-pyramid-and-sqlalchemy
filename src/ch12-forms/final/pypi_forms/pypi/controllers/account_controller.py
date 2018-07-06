from pyramid.view import view_config


# ################### INDEX #################################

@view_config(route_name='account_home',
             renderer='pypi:templates/account/index.pt')
def index(_):
    return {}


# ################### REGISTER #################################

@view_config(route_name='register',
             renderer='pypi:templates/account/register.pt',
             request_method='GET')
def register_get(_):
    return {}


@view_config(route_name='register',
             renderer='pypi:templates/account/register.pt',
             request_method='POST')
def register_post(request):
    return {}
