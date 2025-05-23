from fastapi import FastAPI
from fastapi_crew.src.fastapi_crew import main

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/test")
def test():
    return {"message": "This is a simple test!  YES!  please? or??.....PLEASE!"}

@app.post("/map")
def map_site():
    return main.run("https://docs.crewai.com")