from fastapi import APIRouter, status

blogrouter = APIRouter(
    prefix='/blogs',
    tags=['blogs']
)

@blogrouter.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(blog):
    # Create blog here
    return {'message': 'New blog created'}

@blogrouter.get("/")
def list_blogs():
    return {'message': 'List of all blogs'}

@blogrouter.get("/{blog_id}")
def get_blog(blog_id: int):
    return {'message': f'Blog with id {blog_id}'}

@blogrouter.put("/{blog_id}")
def update_blog(blog_id: int, blog_update):
    # Update blog here
    return {'message': f'Blog with id {blog_id} is updated.'}

@blogrouter.delete("/{blog_id}")
def delete_blog(blog_id: int):
    return {"message": "Blog deleted successfully"}
