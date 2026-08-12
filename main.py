from fastapi import FastAPI
import random

app = FastAPI()

# 127.0.0.1:800/
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 127.0.0.1:800/test
@app.get("/test")
async def test():
    return {
        "test": True,
        "random_number": random.randint(0, 1000)
    }
