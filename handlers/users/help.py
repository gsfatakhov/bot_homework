from aiogram import types
from loader import dp


@dp.message_handler(text="/help")
async def command_start(message: types.Message):
    await message.answer(
        "/sum - находит сумму введенных чисел\n/mul - находит произведение введенных чисел\n/sub - находит разницу двух чисел\n/div - делит первое число на второе\n/evl - находит значение выражения\n/exit - отменяет выполнение команды")
