from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot('1445822445:AAGPIA7reTrAxWncto3bXWEUKo9R7UgKo10')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    await message.reply('Тест')

executor.start_polling(dp)