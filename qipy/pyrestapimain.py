from multiprocessing import Process

#import pytest
#import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.get("/123")
async def read_main():
    return {"msg": "Просто мы работаем для Вас!"}


def run_server():
    uvicorn.run(app)
    
run_server()