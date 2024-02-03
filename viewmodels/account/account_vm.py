from services import account_service
from viewmodels.shared.viewmodel_base import ViewModelBase
from fastapi.requests import Request


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.user = account_service.get_user_by_id(self.user_id)
