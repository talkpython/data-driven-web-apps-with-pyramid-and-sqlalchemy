from pyramid.request import Request

from pypi.services import user_service
from pypi.viewmodels.shared.viewmodel_base import ViewModelBase


class AccountHomeViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.user = user_service.find_user_by_id(self.user_id)
