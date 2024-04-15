from fastapi import FastAPI
from semminar_6_last.api import app as api_app

app = FastAPI()

app.include_router(api_app)
