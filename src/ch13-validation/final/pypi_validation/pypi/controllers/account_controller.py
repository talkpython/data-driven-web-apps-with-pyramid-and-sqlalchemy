import pyramid.httpexceptions as x
from pyramid.request import Request
from pyramid.view import view_config
from pypi.infrastructure import cookie_auth
from pypi.services import user_service
from pypi.viewmodels.account.account_home_viewmodel import AccountHomeViewModel
from pypi.viewmodels.account.login_viewmodel import LoginViewModel
from pypi.viewmodels.account.register_viewmodel import RegisterViewModel


# ################### INDEX #################################


@view_config(route_name='account_home',
             renderer='pypi:templates/account/index.pt')
def index(request):
    vm = AccountHomeViewModel(request)
    if not vm.user:
        return x.HTTPFound('/account/login')

    return vm.to_dict()


# ################### REGISTER #################################

@view_config(route_name='register',
             renderer='pypi:templates/account/register.pt',
             request_method='GET')
def register_get(request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@view_config(route_name='register',
             renderer='pypi:templates/account/register.pt',
             request_method='POST')
def register_post(request: Request):
    vm = RegisterViewModel(request)
    vm.validate()

    if vm.error:
        return vm.to_dict()

    # create user
    user = user_service.create_user(vm.email, vm.name, vm.password)
    cookie_auth.set_auth(request, user.id)

    return x.HTTPFound('/account')


# ################### LOGIN #################################

@view_config(route_name='login',
             renderer='pypi:templates/account/login.pt',
             request_method='GET')
def login_get(request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@view_config(route_name='login',
             renderer='pypi:templates/account/login.pt',
             request_method='POST')
def login_post(request: Request):
    vm = LoginViewModel(request)
    vm.validate()

    if vm.error:
        return vm.to_dict()

    cookie_auth.set_auth(request, vm.user.id)
    return x.HTTPFound('/account')


# ################### LOGOUT #################################

@view_config(route_name='logout')
def logout(request):
    cookie_auth.logout(request)
    return x.HTTPFound('/')
