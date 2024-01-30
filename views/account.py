from fastapi import APIRouter
from fastapi_chameleon import template
from viewmodels.account.login_vm import LoginViewModel
from viewmodels.account.register_vm import RegisterViewModel
from viewmodels.account.account_vm import AccountViewModel
from fastapi.requests import Request


router = APIRouter()


@router.get('/account')
def get_account(request: Request):
    vm = AccountViewModel(request)
    return {}


@router.get('/account/register')
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.get('/account/login')
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get('/account/logout')
def register():
    return vm.to_dict()