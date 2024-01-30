from fastapi import APIRouter
from fastapi_chameleon import template
from viewmodels.account.login_vm import LoginViewModel
from viewmodels.account.register_vm import RegisterViewModel
from viewmodels.account.account_vm import AccountViewModel
from fastapi.requests import Request


router = APIRouter()


@router.get('/account')
@template(template_file='account/index.pt')
def get_account(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
@template(template_file='account/register.pt')
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.get('/account/login')
@template(template_file='account/login.pt')
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get('/account/logout')
def logout():
    return {}
