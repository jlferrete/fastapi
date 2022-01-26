from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_post():
    return { "data": "This is your posts"}