
from . import app
import uvicorn


def run():
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
