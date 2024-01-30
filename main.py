from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def index():
    return {
        "message": "Hellow World!"
    }


uvicorn.run(app)
