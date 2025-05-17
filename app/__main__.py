import logging

import uvicorn
from fastapi import FastAPI

from app.api.v1.endpoints import init_ep_something
from app.container import AppContainer

app = FastAPI()
init_ep_something(app)

if __name__ == "__main__":
    container = AppContainer()
    container.wire(packages=['app'])
    uvicorn.run(app, host="0.0.0.0", port=8090, log_level=logging.DEBUG)
