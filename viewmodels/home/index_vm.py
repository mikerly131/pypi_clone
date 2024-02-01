from services import package_service, account_service
from viewmodels.shared.viewmodel_base import ViewModelBase
from fastapi.requests import Request
from typing import List


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.package_count: int = package_service.release_count()
        self.release_count: int = account_service.user_count()
        self.user_count: int = package_service.package_count()
        self.packages: List = package_service.latest_packages(limit=5)