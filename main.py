from fastapi import FastAPI

app = FastAPI()

# 127.0.0.1:800/
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 127.0.0.1:800/test
@app.get("/test")
async def test():
    return {"test": "All right!"}