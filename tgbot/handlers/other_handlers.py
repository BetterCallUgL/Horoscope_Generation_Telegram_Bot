from aiogram import Dispatcher
from aiogram import types

from keyboards.keyboards import help_generate_kb


# Хэндлер для текстовых сообщений, которые не попали в другие хэндлеры
async def send_answer(message: types.Message):
    await message.answer(
        'Вы неверно указали указали команду или данного знака зодиака не существует. Доступные команды предоставлены на клавиатуре',
        reply_markup=help_generate_kb)


# Функция для регистрации хэндлера.
def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(send_answer)
