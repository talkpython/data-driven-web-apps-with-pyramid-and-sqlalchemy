from pyramid.view import view_config
from pypi.viewmodels.utils.sitemap_viewmodel import SiteMapViewModel


# ################### Sitemap #################################

@view_config(route_name='sitemap.xml', renderer='pypi:templates/utils/sitemap_xml.pt')
def sitemap(request):
    vm = SiteMapViewModel(request, 1000)
    request.response.content_type = 'application/xml'
    return vm.to_dict()


# ################### Robots #################################

@view_config(route_name='robots.txt', renderer='pypi:templates/utils/robots.pt')
def robots(request):
    request.response.content_type = 'text/plain'
    return {}
