from aiogram import types
from loader import dp, current_commands


@dp.message_handler(text="/exit")
async def command_start(message: types.Message):
    if message.from_user.id in current_commands:
        current_commands.pop(message.from_user.id)
        await message.answer("Выполнение команды отменено")
    else:
        await message.answer("Никакая команда не выбрана")
