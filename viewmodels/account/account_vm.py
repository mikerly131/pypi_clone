from data_models.user import User
from viewmodels.shared.viewmodel_base import ViewModelBase
from fastapi.requests import Request


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user = User('Michael', 'michael@gmail.com', '39fjei0edkv0fb9jd')
