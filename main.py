from fastapi import FastAPI
from Worker.Controller import router

app = FastAPI()
app.include_router(router)