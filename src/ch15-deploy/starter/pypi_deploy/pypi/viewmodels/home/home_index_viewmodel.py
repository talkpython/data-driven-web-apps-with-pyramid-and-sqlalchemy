from pyramid.request import Request

from pypi.services import user_service, package_service
from pypi.viewmodels.shared.viewmodel_base import ViewModelBase


class HomeIndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.packages = package_service.latest_releases()
        self.package_count = package_service.package_count()
        self.release_count = package_service.release_count()
        self.user_count = user_service.user_count()
