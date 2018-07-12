from pyramid.request import Request

from pypi.services import package_service
from pypi.viewmodels.shared.viewmodel_base import ViewModelBase


class SiteMapViewModel(ViewModelBase):
    def __init__(self, request: Request, limit):
        super().__init__(request)
        self.packages = package_service.all_packages(limit)
        self.last_updated_text = "2018-07-15"
        self.site = "{}://{}".format(request.scheme, request.host)