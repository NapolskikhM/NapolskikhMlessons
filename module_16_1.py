from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome_():
    return {'message': "Главная страница"}


@app.get('/user/admin')
async def welcome_admin():
    return {'message': "Вы вошли как администратор"}


@app.get('/user/{user_id}')
async def welcome_user_id(user_id: int):
    return {'message': f"Вы вошли как пользователь № {user_id}"}


@app.get('/user')
async def welcome_username(username: str = 'Tom', age: int = 56):
    return {'message': f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

