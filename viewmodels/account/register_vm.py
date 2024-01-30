from typing import Optional
from viewmodels.shared.viewmodel_base import ViewModelBase
from fastapi.requests import Request


class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.name: Optional[str] = None
        self.password: Optional[str] = None
        self.email: Optional[str] = None
