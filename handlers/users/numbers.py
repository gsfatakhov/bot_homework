from aiogram import types
from loader import dp, current_commands
from functools import reduce


@dp.message_handler()
async def command_start(message: types.Message):
    error_text = "Некоректный формат ввода, введите числа с точкой отделяющей дробную часть\nЕсли хотите отменить выполнение команды воспользуйтесь командой /exit"
    if message.from_user.id in current_commands.keys():
        if current_commands[message.from_user.id] == "sum":
            try:
                await message.answer(str(sum(map(float, message.text.split()))))
                current_commands.pop(message.from_user.id)
            except Exception as e:
                await message.answer(error_text)
        elif current_commands[message.from_user.id] == "mul":
            try:
                await message.answer(str(reduce((lambda x, y: x * y), (map(float, message.text.split())))))
                current_commands.pop(message.from_user.id)
            except Exception as e:
                await message.answer(error_text)
    else:
        await message.answer("Не выбрано никакой командыф")
