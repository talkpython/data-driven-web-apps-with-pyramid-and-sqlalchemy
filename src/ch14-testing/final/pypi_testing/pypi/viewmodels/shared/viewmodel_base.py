from pyramid.request import Request

from pypi.infrastructure import request_dict, cookie_auth


class ViewModelBase:
    def __init__(self, request: Request):
        self.request = request
        self.request_dict = request_dict.create(request)
        self.error: str = None
        self.user_id: int = cookie_auth.get_user_id_via_auth_cookie(request)

    def to_dict(self):
        return self.__dict__
