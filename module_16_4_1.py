import json
from typing import Annotated, List
from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):

    id: int
    username: str
    age: int


@app.get('/')
async def welcome_():
    return {'message': "Главная страница"}


@app.get('/users')
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def new_user(username: str, age: int):

    new_user = User(id=0, username='', age=0)

    a = []
    for i in users:
        a.append(i.id)
    new_user.id = max(a, default=0) + 1
    new_user.username = username
    new_user.age = age
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def user_update(user_id: int, username: str, age: int):
    try:
        edited_user = None
        for i in users:
            if i.id == user_id:
                edited_user = i
        edited_user.username = username
        edited_user.age = age
    except KeyError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    try:
        for i in users:
            if i.id == user_id:
                users.remove(i)
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
