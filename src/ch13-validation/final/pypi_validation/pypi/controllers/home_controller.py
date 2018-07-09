from pyramid.view import view_config
from pypi.viewmodels.home.home_index_viewmodel import HomeIndexViewModel
from pypi.viewmodels.shared.viewmodel_base import ViewModelBase


@view_config(route_name='home', renderer='pypi:templates/home/index.pt')
def home_index(request):
    vm = HomeIndexViewModel(request)
    return vm.to_dict()


@view_config(route_name='about', renderer='pypi:templates/home/about.pt')
def home_about(request):
    vm = ViewModelBase(request)
    return vm.to_dict()
