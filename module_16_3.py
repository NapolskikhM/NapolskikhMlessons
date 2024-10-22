from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/')
async def welcome_():
    return {'message': "Главная страница"}


@app.get('/users')
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def new_message(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                         example='UrbanUser')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    new_user = str(int(max(users, key=int)) + 1)
    users[new_user] = f'Имя: {username}, возраст: {age}'
    return {'message': f"User {new_user} is registered"}


@app.put('/user/{user_id}/{username}/{age}')
async def welcome_user_id(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
                          username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                        example='UrbanUser')],
                          age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return {'message': f"User {user_id} is registered"}


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    users.pop(str(user_id))
    return {'message': f"User {user_id} is deleted"}