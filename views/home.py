from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()


@router.get('/')
@template(template_file='home/index.pt')
def index(user: str = 'anon'):
    return {
        'user_name': user
    }


@router.get('/about')
@template(template_file='home/about.pt')
def about():
    return {}