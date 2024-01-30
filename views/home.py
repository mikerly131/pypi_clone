from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()


@router.get('/')
@template(template_file='home/index.pt')
def index():
    return {
        'package_count': 274_000,
        'release_count': 2_435_232,
        'user_count': 87_232,
        'packages': [
            {'id': 'fastapi', 'summary': 'A great python web framework'},
            {'id': 'uvicorn', 'summary': 'An ASGI server'},
            {'id': 'httpx', 'summary': 'Requests for the async world'},
            ]
    }


@router.get('/about')
@template(template_file='home/about.pt')
def about():
    return {}