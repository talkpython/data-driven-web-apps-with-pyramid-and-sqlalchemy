from pyramid.request import Request

from pypi.viewmodels.shared.viewmodel_base import ViewModelBase

fake_db = {
    'company/history': {
        'page_title': 'Company history',
        'page_details': 'Details about company history...',
    },
    'company/employees': {
        'page_title': 'Our team',
        'page_details': 'Details about company employees ...',
    },
}


class PageViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.subpath = request.matchdict.get('subpath')
        self.suburl = None
        if self.subpath:
            self.suburl = '/'.join(self.subpath)

        self.page = fake_db.get(self.suburl)

