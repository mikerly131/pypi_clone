from typing import Optional
from fastapi.requests import Request

from utilities import cookie_auth


class ViewModelBase:
    def __init__(self, request: Request):
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[str] = None

        # Will set this from cookies once we have users
        self.is_logged_in = cookie_auth.get_user_id_from_auth_cookie(self.request)

    def to_dict(self) -> dict:
        return self.__dict__


