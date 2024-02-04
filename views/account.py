from fastapi import APIRouter, status
from fastapi_chameleon import template

from services import account_service
from utilities import cookie_auth
from viewmodels.account.login_vm import LoginViewModel
from viewmodels.account.register_vm import RegisterViewModel
from viewmodels.account.account_vm import AccountViewModel
from fastapi.requests import Request
from fastapi.responses import RedirectResponse


router = APIRouter()


@router.get('/account')
@template(template_file='account/index.pt')
async def get_account(request: Request):
    vm = AccountViewModel(request)
    await vm.load()
    return vm.to_dict()


@router.get('/account/register')
@template(template_file='account/register.pt')
def register_get(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.post('/account/register')
@template(template_file='account/register.pt')
async def register_post(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()
    if vm.error:
        return vm.to_dict()
    # Create account
    account = account_service.create_account(vm.name, vm.email, vm.password)
    # Login user
    response = RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)

    return response


@router.get('/account/login')
@template(template_file='account/login.pt')
def login_get(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post('/account/login')
@template(template_file='account/login.pt')
async def login_post(request: Request):
    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user = account_service.login_account(vm.email, vm.password)
    if not user:
        vm.error = 'The account does not exist or the password is wrong'
        return vm.to_dict()

    response = RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, user.id)

    return response


@router.get('/account/logout')
def logout():
    response = RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)
    return response
