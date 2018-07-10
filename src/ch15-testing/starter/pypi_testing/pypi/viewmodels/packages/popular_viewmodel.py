from pyramid.request import Request
from pypi.viewmodels.shared.viewmodel_base import ViewModelBase


class PopularPackageViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.num = int(self.request_dict.get('num', -1))
        self.package_name = "The {}th most popular package".format(self.num)
