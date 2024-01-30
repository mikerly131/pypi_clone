from fastapi import APIRouter
from fastapi_chameleon import template
from fastapi.requests import Request
from viewmodels.packages.details_vm import DetailsViewModel

router = APIRouter()


@router.get('/project/{package_name}')
@template(template_file='packages/details.pt')
def index(package_name: str, request: Request):
    vm = DetailsViewModel(package_name, request)
    return vm.to_dict()