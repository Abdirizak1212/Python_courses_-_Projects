from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my Notes API!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}