from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_post():
    return { "data": "This is your posts"}

@app.post("/createposts")
def create_posts(new_post: Post): 
    print(new_post.rating)
    return{"data": "new_post"}