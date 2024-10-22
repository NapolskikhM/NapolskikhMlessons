from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def welcome_():
    return {'message': "Главная страница"}


@app.get('/user/admin')
async def welcome_admin():
    return {'message': "Вы вошли как администратор"}


@app.get('/user/{user_id}')
async def welcome_user_id(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    return {'message': f"Вы вошли как пользователь № {user_id}"}


@app.get('/user/{username}/{age}')
async def welcome_username(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                         example='UrbanUser')],
                           age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]):
    return {'message': f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
