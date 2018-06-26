from pyramid.view import view_config
from pyramid.request import Request
import pyramid.httpexceptions as x


# /project/{package_name}/

@view_config(route_name='package_details',
             renderer='pypi:templates/packages/details.pt')
@view_config(route_name='package_details/',
             renderer='pypi:templates/packages/details.pt')
def details(request: Request):
    package_name = request.matchdict.get('package_name')
    if not package_name:
        raise x.HTTPNotFound()

    return {
        'package_name': package_name
    }
