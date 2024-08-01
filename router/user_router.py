from fastapi import APIRouter, status

userrouter = APIRouter(
    prefix='/users',
    tags=['users']
)

@userrouter.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user):
    # Create new user
    return {'message': 'new user created'}

@userrouter.get("/")
def list_users():
    return {'message': 'List of all users'}

@userrouter.get("/{user_id}")
def get_user(user_id: int):
    return {'message': f'User with id {user_id}'}

@userrouter.put("/{user_id}",)
def update_user(user_id: int, user_update):
    # Update user here
    return {'message': f'User with id {user_id} is updated.'}

@userrouter.delete("/{user_id}")
def delete_user(user_id: int):
    return {"message": "User deleted successfully"}
