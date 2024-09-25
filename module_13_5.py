# С загрузкой aiogram 2.25.1 на python 3.12 ничего не вышло,
# лезть в глубины, к сожалению, нет времени.
# Поставил на python 3.10.

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Информация')
button_2 = KeyboardButton(text='Рассчитать')
kb.add(button_1)
kb.add(button_2)

@dp.message_handler(text=['/start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


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

    @dp.message_handler()
    async def all_message():
        print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)