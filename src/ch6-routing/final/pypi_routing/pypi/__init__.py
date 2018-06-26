from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    init_includes(config)
    init_routing(config)

    return config.make_wsgi_app()


def init_includes(config):
    config.include('pyramid_chameleon')


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    # home controller
    config.add_route('home', '/')
    config.add_route('about', '/about')

    # package controller
    config.add_route('package_details', '/project/{package_name}')
    config.add_route('package_details/', '/project/{package_name}/')

    config.scan()
