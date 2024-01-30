from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()


@router.get('/account')
def get_account():
    return {}


@router.get('/account/register')
def register():
    return {}


@router.get('/account/login')
def register():
    return {}


@router.get('/account/logout')
def register():
    return {}