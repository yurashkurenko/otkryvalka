from aiogram import Bot, Dispatcher, executor, types
import requests
import aiogram
import logging
import fnmatch
import rooms
global select_room
import userrooms
bot = Bot(token="1753263636:AAGqiaD18nFdcdulijFUGJyaWEAsql6eKsk")
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

buttons = ['Пользователи','Боксы','Состояние']
buttonsuser = ['Добавить','Удалить','Список']
buttonsboxes = ['Добавить','Удалить','Список']
#buttons = ['Пользователи','Боксы','+','-','V','Добавить','Удалить','Состояние']
keyboard.add(*buttons)
dp = Dispatcher(bot)
@dp.message_handler()

async def cmd_start(message: types.Message):
    print(message.chat)
    if message.text.lower() == '/start':
        checkmessage='Добро пожаловать!'
        helpmessage='Задача управления пользователями сводится к заполнению таблицы пользователей, таблицы боксов и таблицы соответствия пользователей и боксов. Один пользователь может управлять несколькими боксами. Для управления боксами нужно выбрать существующего пользователя или добавить и выбрать нового пользователя. затем выбраному пользователю добавить или удалить боксы для управления'
        await message.answer(checkmessage+'По вопросам работы бота просьба обращаться @yurasoft1972'+' '+helpmessage, reply_markup=keyboard)
        #print(checkmessage)
    elif message.text.lower() == 'пользователи':
        checkmessage=userrooms.userlist()
        await message.answer(checkmessage, reply_markup=keyboard)
        print(checkmessage)
    elif message.text.lower() == 'боксы':
        checkmessage=userrooms.boxlist()
        await message.answer(checkmessage, reply_markup=keyboard)
        print(checkmessage)    
    elif message.text.lower() == 'состояние':
        checkmessage='состояние'
        await message.answer(checkmessage, reply_markup=keyboard)
        print(checkmessage) 
 
 
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
