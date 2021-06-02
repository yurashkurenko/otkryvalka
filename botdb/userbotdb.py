from aiogram import Bot, Dispatcher, executor, types
import requests
import aiogram
import logging
import fnmatch
import pdata
import db
# global select_room
import alldatadb
import alldata
bot = Bot(token="1753263636:AAGqiaD18nFdcdulijFUGJyaWEAsql6eKsk")
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ['Пользователи','Боксы','Состояние']
buttonsuser = ['Добавить','Удалить','Список','Назад']
buttonsboxes = ['Добавить','Удалить','Список']
#buttons = ['Пользователи','Боксы','+','-','V','Добавить','Удалить','Состояние']
keyboard.add(*buttons)
keyboard1.add(*buttonsuser)

dp = Dispatcher(bot)
menulevel='top'
alldatadb.menulevel(menulevel)

@dp.message_handler()
async def cmd_start(message: types.Message):
    menulevel=alldatadb.menulevel()
    #inputtext=''
    #valuetocmd=''
    print(menulevel)
    print(message.chat)
    if (message.text.lower() == '/start') or (message.text.lower() == '/help'):
        checkmessage='Добро пожаловать!'
        helpmessage='Задача управления пользователями сводится к заполнению таблицы пользователей, \
        таблицы боксов и таблицы соответствия пользователей и боксов. Один пользователь может \
        управлять несколькими боксами. Для управления боксами нужно выбрать существующего \
        пользователя или добавить и выбрать нового пользователя. затем выбранyому пользователю \
        добавить или удалить боксы для управления'
        await message.answer(checkmessage, reply_markup=keyboard)
        await message.answer(helpmessage, reply_markup=keyboard)
    elif message.text.lower() == 'пользователи':
        alldatadb.menulevel("пользователи")
        print( alldatadb.menulevel())
        if alldatadb.menulevel()=='пользователи':
            checkmessage='пользователями.'
        checkmessage='Работа с '+checkmessage
        await message.answer(checkmessage, reply_markup=keyboard1)
        checkmessage='Список пользователей'
        await message.answer(checkmessage, reply_markup=keyboard1)
        checkmessage=alldatadb.userlist()
        await message.answer(checkmessage, reply_markup=keyboard1)
        # checkmessage='Для добавления или удаления пользователя отправьте имя пользователя со знаком минус или плюс (например -user)  и нажмите нужную кнопку'
        # await message.answer(checkmessage, reply_markup=keyboard1)        
        # #print(checkmessage)
    elif message.text.lower() == 'боксы':
        alldatadb.menulevel('боксы')
        checkmessage=alldata.boxlist()
        await message.answer(checkmessage, reply_markup=keyboard1)
        print(checkmessage) 
    elif message.text.lower() == 'состояние':
        alldata.menulevel('состояние')
        checkmessage=alldata.userboxes
        await message.answer(checkmessage, reply_markup=keyboard1)
        print(checkmessage) 
    elif message.text.lower() == 'список':
        menulevel=alldatadb.menulevel()
        checkmessage='Список'+menulevel
        if menulevel=='боксы':
                checkmessage=alldata.boxlist()
                await message.answer(checkmessage, reply_markup=keyboard1)
        if menulevel=='пользователи':
                checkmessage=alldatadb.userlist()
                await message.answer(checkmessage, reply_markup=keyboard1)
        print(checkmessage) 
    elif message.text.lower() == 'пользователи-боксы':
        checkmessage=alldata.userlist()
        await message.answer(checkmessage, reply_markup=keyboard1)
        print(checkmessage)         
        await message.answer(checkmessage, reply_markup=keyboard)
        print(checkmessage) 
    elif message.text.lower() == 'назад':
        checkmessage='назад'
        await message.answer(checkmessage, reply_markup=keyboard)
        print(checkmessage) 
    elif message.text.lower() == 'добавить':
        if alldatadb.menulevel()=='пользователь':
           checkmessage='Добавление пользователя'
           await message.answer(checkmessage, reply_markup=keyboard1)
           alldatadb.userappend(alldatadb.inputtextstr)
           checkmessage=alldata.menulevel
           await message.answer(checkmessage, reply_markup=keyboard1)#inputtext=message.text
           checkmessage=alldata.inputtextstr+' добавлен'
        await message.answer(checkmessage, reply_markup=keyboard1)#inputtext=message.text
        checkmessage=alldata.userlist()
        await message.answer(checkmessage, reply_markup=keyboard1)
    elif message.text.lower() == 'удалить':
        checkmessage='Удаление...'
        await message.answer(checkmessage, reply_markup=keyboard1)
        alldata.userremove(alldata.inputtextstr)
        checkmessage=alldata.inputtextstr+'удален'
        await message.answer(checkmessage, reply_markup=keyboard1)#inputtext=message.text
        checkmessage=alldata.userlist()
        await message.answer(checkmessage, reply_markup=keyboard1)
    alldatadb.inputtextstr=message.text
    valuetocmd=''
    if message.text[0]=='-': 
        valuetocmd=message.text[1:]
    if message.text[0]=='+': 
        valuetocmd=message.text[1:]
    alldatadb.inputtextstr=valuetocmd
    print(alldata.inputtextstr)
    print(message.text[0])
    print(message.text[1:])
    print(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
