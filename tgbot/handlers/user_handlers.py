from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from keyboards.keyboards import zodiac_kb, help_generate_kb
from services.client import zodiac_generate


# Хэндлер, обрабатывающий команду '/start'
async def start_command(message: types.Message) -> None:
    await message.answer(text='Добро пожаловать в бот,генерирующий гороскопы',
                         reply_markup=help_generate_kb)
    await message.delete()


# Хэндлер, обрабатывающий команду '/help'
async def help_command(message: types.Message) -> None:
    await message.answer(
        """Данный бот способен генерировать гороскопы для выбранного знака зодиака на день.
Для этого, нажмите кнопку /generation и выберите желанный знак зодиака.""",
        reply_markup=help_generate_kb)


# Хэндлер, обрабатывающий команду '/generation'
async def generate_command(message: types.Message) -> None:
    await message.answer('Выберите знак Зодиака', reply_markup=zodiac_kb)


# Хэндлер, обрабатывающий название знака зодиака и генерирующий для него гороскоп
async def generate_button(message: types.Message) -> None:
    await message.answer('Дождитесь пока сгенерируется ваш Гороскоп')
    horoscope = await zodiac_generate(message.text)
    await message.answer(horoscope)


# Функция для регистрации хэндлеров. Импортируется и вызывается в файле bot.py
def register_user_handlers(dp) -> None:
    dp.register_message_handler(start_command, commands='start')
    dp.register_message_handler(help_command, commands='help')
    dp.register_message_handler(generate_command, commands='generation')
    dp.register_message_handler(generate_button,
                                Text(equals=['Рыбы', 'Водолей', 'Козерог', 'Стрелец', 'Скорпион', 'Весы', \
                                             'Дева', 'Лев', 'Рак', 'Близнецы', 'Телец',
                                             'Овен']))
