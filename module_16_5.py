from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):

    id: int
    username: str
    age: int


@app.get('/')
async def get_main_page(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, "users": users})


@app.get(path='/user/{user_id}')
async def get_users(request: Request, user_id: int):
    return templates.TemplateResponse('users.html', {'request': request, "user": users[user_id-1]})


@app.post('/')
async def new_user(new_user: User):

    new_user.id = len(users) + 1
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def user_update(user_id: int, username: str, age: int):
    try:
        edited_user = users[user_id]
        edited_user.username = username
        edited_user.age = age
    except KeyError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    try:
        users.pop(user_id)
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")