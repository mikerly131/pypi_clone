from fastapi import FastAPI
from fastapi_chameleon import global_init
from views import home, account, packages
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()


def main():
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8000)


def configure():
    configure_templates()
    configure_routes()


def configure_templates():
    global_init('templates')


def configure_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


# If run in production, will still configure app but not run it from here
if __name__ == '__main__':
    main()
else:
    configure()
