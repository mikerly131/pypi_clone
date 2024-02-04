from typing import Optional

from services import account_service
from viewmodels.shared.viewmodel_base import ViewModelBase
from fastapi.requests import Request


class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.name: Optional[str] = None
        self.password: Optional[str] = None
        self.email: Optional[str] = None

    # Process and validate the registration form
    async def load(self):
        form = await self.request.form()
        self.name = form.get('name')
        self.password = form.get('password')
        self.email = form.get('email')

        if not self.name or not self.name.strip():
            self.error = "Your name is required."
        elif not self.email or not self.email.strip():
            self.error = "Your email is required."
        elif not self.password or  len(self.password) < 5:
            self.error = "Your password must be at least 5 characters."
        elif await account_service.get_user_by_email(self.email):
            self.error = "Please login, already registered."
