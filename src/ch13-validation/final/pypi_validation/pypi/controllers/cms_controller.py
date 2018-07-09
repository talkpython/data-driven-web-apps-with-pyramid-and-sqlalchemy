from pyramid.httpexceptions import HTTPNotFound
from pyramid.request import Request
from pyramid.view import view_config
from pypi.viewmodels.cms.page_viewmodel import PageViewModel


@view_config(route_name='cms_page', renderer='pypi:templates/cms/page.pt')
def cms_page(request: Request):
    vm = PageViewModel(request)
    if not vm.page:
        raise HTTPNotFound()

    return vm.to_dict()
