# aiogram 2.25.1 python 3.10

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import crud_functions

products_ = crud_functions.get_all_products()

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):

    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):

    username = State()
    email = State()
    age = State()
    balance = State()


# главное меню
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Информация')
button_2 = KeyboardButton(text='Рассчитать')
button_5 = KeyboardButton(text='Купить')
button_10 = KeyboardButton(text='Регистрация')
kb.add(button_1)
kb.add(button_2)
kb.add(button_5)
kb.add(button_10)

# меню расчет нормы калорий
InlineKeyboardMarkup_ = InlineKeyboardMarkup()
button_3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
InlineKeyboardMarkup_.add(button_3)
InlineKeyboardMarkup_.add(button_4)

# меню перечень товаров
InlineKeyboardMarkup_1 = InlineKeyboardMarkup()
button_6 = InlineKeyboardButton(text=f'{products_[0][1]}', callback_data="product_buying")
button_7 = InlineKeyboardButton(text=f'{products_[1][1]}', callback_data="product_buying")
button_8 = InlineKeyboardButton(text=f'{products_[2][1]}', callback_data="product_buying")
button_9 = InlineKeyboardButton(text=f'{products_[3][1]}', callback_data="product_buying")
InlineKeyboardMarkup_1.add(button_6)
InlineKeyboardMarkup_1.add(button_7)
InlineKeyboardMarkup_1.add(button_8)
InlineKeyboardMarkup_1.add(button_9)


# добавил, поскольку нажатие на кнопку "Информация" предлагает ввести /start
@dp.message_handler(text='Информация')
async def main_menu(message):
    await message.answer(text='Нажмите на кнопку "Рассчитать", "Купить" или "Регистрация"')


# /start выводит основное меню
@dp.message_handler(text=['/start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


# выводит меню "рассчитать норму калорий" и "формулы расчета"
@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer(text='Выберите опцию:', reply_markup=InlineKeyboardMarkup_)


# выводит формулу Миффлина - Сан Жеора
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.answer(text='Формула Миффлина - Сан Жеора для мужчин при средней физической активности: '
                           'потребное число килокалорий в сутки '
                           '= 1,4625 * ( 10 х вес(кг) + 6,25 x рост(см) – 5 х возраст(г) + 5')
    await call.answer()


# запрос возраста
@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


# запрос роста
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


# запрос веса
@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


# расчет калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # исключаем нечисловые данные:
    try:
        # считаем калории для средней активности с округлением до целых
        calories_ = int(1.4625 * ((float(data['weight']) * 10) + (float(data['growth']) * 6.25)
                                  - (float(data['age']) * 5) + 5))
        # выводим
        await message.answer(f'Ваша норма калорий: {calories_}')
        # на самом деле не калорий, а килокалорий
        await state.finish()
    except ValueError:
        await message.answer('Некорректные данные!')
        await state.finish()


# картинки и описание продукта
# файлы картинок file1.jpg file2.jpg file3.jpg file4.jpg
@dp.message_handler(text='Купить')
async def get_buying_list(message):

    for i in range(1, 4):
        await message.answer(text=f'Название: {products_[i][1]} '
                                  f'| Описание: {products_[i][2]} | Цена: {products_[i][3]}')
        with open(f'file{i}.jpg', 'rb') as img:
            await message.answer_photo(img)
    # вывод меню товаров
    await message.answer(text='Выберите продукт для покупки:', reply_markup=InlineKeyboardMarkup_1)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.answer(text="Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if crud_functions.is_included(message.text):
        await message.answer('Пользователь существует, введите другое имя:')
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data_ = await state.get_data()
    crud_functions.add_user(f"{data_['username']}", f"{data_['email']}", f'{data_["age"]}')
    await message.answer('Регистрация прошла успешно.')
    await state.finish()
    await message.answer('Нажмите на кнопку "Рассчитать" или "Купить"', reply_markup=kb)


# ответ на любое сообщение
@dp.message_handler()
async def all_message(message):
    await message.answer('Введите "/start" чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
