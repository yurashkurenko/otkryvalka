from multiprocessing import Process

#import pytest
#import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


def run_server():
    uvicorn.run(app)
    
run_server()