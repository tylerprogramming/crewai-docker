from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/test")
def test():
    return {"message": "This is a simple test!  YES!  please?"}