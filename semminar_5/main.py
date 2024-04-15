from fastapi import FastAPI
from semminar_5.api import router as task_router

app = FastAPI()

app.include_router(task_router)
