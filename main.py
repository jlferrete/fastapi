from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_post():
    return { "data": "This is your posts"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return{"new_post": f"Title: {payload['title']} Content: {payload['content']}"}