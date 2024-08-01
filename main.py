from fastapi import FastAPI, status
from router import blog_router, user_router

app = FastAPI()

app.include_router(blog_router.blogrouter)
app.include_router(user_router.userrouter)