from fastapi import FastAPI
from fastapi.params import Body, Optional
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 0}, {"title": "favorite foods", "content": "I like pizza", "id": 1}]

@app.get("/")  # This is called a decorator
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return { "data": "These are your posts" }

# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)): # dict is the data type being passed in, payload is what it is called, Body is from fastapi
#     print(payload)
#     return {"new_post": f"title {payload['title']} content: {payload['content']}"}
@app.post("/posts")
def create_posts(new_post: Post):
    print(new_post)
    print('hi', new_post.model_dump())
    return {"data": "new post"}
# title str, content str