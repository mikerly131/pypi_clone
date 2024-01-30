from fastapi import APIRouter
from fastapi_chameleon import template
from viewmodels.home.index_vm import IndexViewModel
from fastapi.requests import Request
from viewmodels.shared.viewmodel_base import ViewModelBase

router = APIRouter()


@router.get('/')
@template(template_file='home/index.pt')
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get('/about')
@template(template_file='home/about.pt')
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
