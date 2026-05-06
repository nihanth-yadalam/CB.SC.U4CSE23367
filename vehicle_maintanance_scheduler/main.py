from fastapi import FastAPI
from logging_middleware.log_service import Log

app= FastAPI()
l1 = Log(stack="backend", level="info", package="controller", message="app started")
l1.logdata()
l1.send()

@app.get("/")
def welcome():
    l2 = Log(stack="backend", level="info", package="controller", message="hit welcome endpoint")
    l2.logdata()
    l2.send()
    return {"message": "welcome to vehicle maintenance scheduler"}


