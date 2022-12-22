from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token="5808059076:AAGTYhIYT2sbkw06wQcnuVpupVmrmWxEhgA")

dp = Dispatcher(bot)


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = "Hello world"
    await bot.send_message(chat_id=chat_id, text=text)


executor.start_polling(dp)
