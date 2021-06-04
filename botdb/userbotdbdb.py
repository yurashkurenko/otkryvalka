from aiogram import Bot, Dispatcher, executor, types
import requests
import aiogram
import logging
import fnmatch
import db
import alldatadb
bot = Bot(token="1753263636:AAGqiaD18nFdcdulijFUGJyaWEAsql6eKsk")
alldatadb.menulevel(10)
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
dp = Dispatcher(bot)

@dp.message_handler()
async def cmd_start(message: types.Message):
    state=alldatadb.menulevel()
    buttons=alldatadb.buttonlist(state)
    keyboard = types.ReplyKeyboardRemove()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    print(buttons)
    messagedb=alldatadb.message(state)
    print(messagedb)
    command=alldatadb.command(state)
    print(command)
    alldatadb.menulevel(state)
    print(alldatadb.menulevel())
    print(state)
    print(message.chat)
    command=' пользователи'
       
#    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())
    if (message.text.lower() == '/start') or (message.text.lower() == '/help'):
        checkmessage='Добро пожаловать!'
        helpmessage='Задача управления пользователями сводится к заполнению таблицы пользователей, \
        таблицы боксов и таблицы соответствия пользователей и боксов. Один пользователь может \
        управлять несколькими боксами. Для управления боксами нужно выбрать существующего \
        пользователя или добавить и выбрать нового пользователя. затем выбранyому пользователю \
        добавить или удалить боксы для управления'
        alldatadb.menulevel(10)
        await message.answer(checkmessage, reply_markup=types.ReplyKeyboardRemove())
        await message.answer(helpmessage, reply_markup=types.ReplyKeyboardRemove())
#        S.find(str, [start],[end])	Поиск подстроки в строке. Возвращает номер первого вхождения или -1
    elif message.text.lower().find(' пользователи'):
        alldatadb.menulevel(1)
        print(command)
        print(state)
        checkmessage='Работа с ' + alldatadb.message(state)
        checkmessage1 = alldatadb.message(state)
        await message.answer(checkmessage, reply_markup=types.ReplyKeyboardRemove())
        await message.answer(checkmessage1, reply_markup=keyboard)
    elif message.text.lower().find(' назад'):
        alldatadb.menulevel(10)
        print(command)
        print(state)
        checkmessage='Работа с ' + alldatadb.message(state)
        checkmessage1 = alldatadb.message(state)
        await message.answer(checkmessage, reply_markup=types.ReplyKeyboardRemove())
        await message.answer(checkmessage1, reply_markup=keyboard)
        
        
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
