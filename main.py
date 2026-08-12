from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def hello_world():
    return {"message": "Hello World"}

@app.get("/test-function")
async def test_function():
    return {"test": "All right!"}
