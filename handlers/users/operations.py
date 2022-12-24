from aiogram import types
from loader import dp, current_commands


@dp.message_handler(text="/sum")
async def command_start(message: types.Message):
    current_commands[message.from_user.id] = "sum"
    await message.answer("Ввeдите числа для суммирования")


@dp.message_handler(text="/sub")
async def command_start(message: types.Message):
    current_commands[message.from_user.id] = "sub"
    await message.answer("Ввeдите два числа для вычитания второго из первого")


@dp.message_handler(text="/mul")
async def command_start(message: types.Message):
    current_commands[message.from_user.id] = "mul"
    await message.answer("Ввeдите числа для умножения")


@dp.message_handler(text="/div")
async def command_start(message: types.Message):
    current_commands[message.from_user.id] = "div"
    await message.answer("Ввeдите два для деления первого вторым")


@dp.message_handler(text="/evl")
async def command_start(message: types.Message):
    current_commands[message.from_user.id] = "evl"
    await message.answer("Ввeдите выражение для подсчета")
