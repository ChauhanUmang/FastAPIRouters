from fastapi import FastAPI, status

app = FastAPI()

@app.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(blog):
    # Create blog here
    return {'message': 'New blog created'}

@app.get("/")
def list_blogs():
    return {'message': 'List of all blogs'}

@app.get("/{blog_id}")
def get_blog(blog_id: int):
    return {'message': f'Blog with id {blog_id}'}

@app.put("/{blog_id}")
def update_blog(blog_id: int, blog_update):
    # Update blog here
    return {'message': f'Blog with id {blog_id} is updated.'}

@app.delete("/{blog_id}")
def delete_blog(blog_id: int):
    return {"message": "Blog deleted successfully"}


@app.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user):
    # Create new user
    return {'message': 'new user created'}

@app.get("/")
def list_users():
    return {'message': 'List of all users'}

@app.get("/{user_id}")
def get_user(user_id: int):
    return {'message': f'User with id {user_id}'}

@app.put("/{user_id}",)
def update_user(user_id: int, user_update):
    # Update user here
    return {'message': f'User with id {user_id} is updated.'}

@app.delete("/{user_id}")
def delete_user(user_id: int):
    return {"message": "User deleted successfully"}
