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


# /project/{package_name}/releases
@view_config(route_name='releases',
             renderer='pypi:templates/packages/releases.pt')
@view_config(route_name='releases/',
             renderer='pypi:templates/packages/releases.pt')
def releases(request: Request):
    package_name = request.matchdict.get('package_name')
    if not package_name:
        raise x.HTTPNotFound()

    return {
        'package_name': package_name,
        'releases': []
    }


# /project/{package_name}/releases/{release_version}
@view_config(route_name='release_version',
             renderer='pypi:templates/packages/details.pt')
def release_version(request: Request):
    package_name = request.matchdict.get('package_name')
    release_ver = request.matchdict.get('release_version')
    if not package_name:
        raise x.HTTPNotFound()

    return {
        'package_name': package_name,
        'release_version': release_ver,
        'releases': []
    }


# /{num}
@view_config(route_name='popular',
             renderer='pypi:templates/packages/details.pt')
def popular(request: Request):
    num = int(request.matchdict.get('num', -1))
    if not (1 <= num or num <= 10):
        raise x.HTTPNotFound()

    return {
        'package_name': "The {}th popular package".format(num)
    }
