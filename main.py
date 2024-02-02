from pathlib import Path
from fastapi import FastAPI
from fastapi_chameleon import global_init
from views import home, account, packages
from fastapi.staticfiles import StaticFiles
import uvicorn
from data_models import db_session

app = FastAPI()


def main():
    configure(dev_mode=True)
    uvicorn.run(app, host='127.0.0.1', port=8000)


def configure(dev_mode: bool):
    configure_templates(dev_mode)
    configure_routes()
    configure_db(dev_mode)


def configure_db(dev_mode: bool):
    file = (Path(__file__).parent / 'db' / 'pypi.sqlite').absolute()
    db_session.global_init(file.as_posix())


def configure_templates(dev_mode: bool):
    global_init('templates', auto_reload=dev_mode)


def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


# If run in production, will still configure app but not run it from here
if __name__ == '__main__':
    main()
else:
    configure(dev_mode=False)
