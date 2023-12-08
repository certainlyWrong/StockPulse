
import uvicorn

from stockpulse.app import app


# TODO pesquisar boirlerplate para projetos usando FastAPI


def run():
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
