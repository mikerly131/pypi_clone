from typing import Optional
from fastapi.requests import Request


class ViewModelBase:
    def __init__(self, request: Request):
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[str] = None

        # Will set this from cookies once we have users
        self.is_logged_in = False

    def to_dict(self) -> dict:
        return self.__dict__


