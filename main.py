from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/helloworld")
async def hello_world():
    return {"message": "Hello World"}

@app.get("/test-function")
async def test_function():
    return {
        "test": True,
        "random_number": random.randint(0, 20000)
    }
