import pyramid.httpexceptions as x
from pyramid.request import Request
from pyramid.view import view_config


# ################### INDEX #################################
from pypi.infrastructure import cookie_auth
from pypi.services import user_service


@view_config(route_name='account_home',
             renderer='pypi:templates/account/index.pt')
def index(request):
    user_id = cookie_auth.get_user_id_via_auth_cookie(request)
    user = user_service.find_user_by_id(user_id)
    if not user:
        return x.HTTPFound('/account/login')

    return {
        'user': user,
        'user_id': user.id
    }


# ################### REGISTER #################################

@view_config(route_name='register',
             renderer='pypi:templates/account/register.pt',
             request_method='GET')
def register_get(request):
    return {
        'email': None,
        'name': None,
        'password': None,
        'error': None,
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }


@view_config(route_name='register',
             renderer='pypi:templates/account/register.pt',
             request_method='POST')
def register_post(request: Request):
    email = request.POST.get('email')
    name = request.POST.get('name')
    password = request.POST.get('password')

    if not email or not name or not password:
        return {
            'email': email,
            'name': name,
            'password': password,
            'error': 'Some required fields are missing.',
            'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
        }

    # create user
    user = user_service.create_user(email, name, password)
    cookie_auth.set_auth(request, user.id)

    return x.HTTPFound('/account')


# ################### LOGIN #################################

@view_config(route_name='login',
             renderer='pypi:templates/account/login.pt',
             request_method='GET')
def login_get(request):
    return {
        'email': None,
        'password': None,
        'error': None,
        'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
    }


@view_config(route_name='login',
             renderer='pypi:templates/account/login.pt',
             request_method='POST')
def login_post(request: Request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = user_service.login_user(email, password)

    if not user:
        return {
            'email': email,
            'password': password,
            'error': 'The user could not found or the password is incorrect.',
            'user_id': cookie_auth.get_user_id_via_auth_cookie(request)
        }

    cookie_auth.set_auth(request, user.id)
    return x.HTTPFound('/account')
