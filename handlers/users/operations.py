from aiogram import types
from loader import dp, current_commands


@dp.message_handler(text="/sum")
async def command_start(message: types.Message):
    current_commands[message.from_user.id] = "sum"
    await message.answer("Ввидите числа для суммирования")

@dp.message_handler(text="/sub")
async def command_start(message: types.Message):
    current_commands[message.from_user.id] = "sum"
    await message.answer("Ввидите числа для суммирования")


@dp.message_handler(text="/mul")
async def command_start(message: types.Message):
    current_commands[message.from_user.id] = "mul"
    await message.answer("Ввидите числа для умножения")


@dp.message_handler(text="/div")
async def command_start(message: types.Message):
    current_commands[message.from_user.id] = "mul"
    await message.answer("Ввидите числа для умножения")
