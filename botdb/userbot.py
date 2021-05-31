from aiogram import Bot, Dispatcher, executor, types
import requests
import aiogram
import logging
import fnmatch
import pdata
import db
# global select_room
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
global menulevel 
menulevel='top'

# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
    # checkmessage='Добро пожаловать!'
    # helpmessage='Задача управления пользователями сводится к заполнению таблицы пользователей.'
    # # +' таблицы боксов и таблицы соответствия пользователей и боксов..\n Один пользователь может'
    # # +'управлять несколькими боксами. Для управления бок.\n сами нужно выбрать существующего пользователя'
    # # +'или добавить и выбрать нового пользователя. затем выбраному пользователю добавить или удалить боксы для управления'
    # await message.answer(checkmessage)
    # await message.answer(helpmessage)
    # await message.answer("/пользователи")
    # await message.answer("/боксы")
    # await cmd_start(message)

# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
    # helpmessage='Задача управления пользователями сводится к заполнению таблицы пользователей, \
    # таблицы боксов и таблицы соответствия пользователей и боксов. Один пользователь может \
    # управлять несколькими боксами. Для управления боксами нужно выбрать существующего \
    # пользователя или добавить и выбрать нового пользователя. затем выбраному пользователю \
    # добавить или удалить боксы для управления'
    # await message.answer(helpmessage)
    # await cmd_start(message)

async def userlistmessage():
    checkmessage='Список пользователей'
    await message.answer(checkmessage, reply_markup=keyboard1)
    table='users'
    rowsfetch=['user']
    users=[]
    users=db.fetchall(table,rowsfetch)
    for num in range(len(users)):
        checkmessage=alldata.users(num)
        if checkmessage:
            await message.answer(checkmessage, reply_markup=keyboard1)

@dp.message_handler()
async def cmd_start(message: types.Message):


    menulevel=alldata.menulevel()
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
        alldata.menulevel('пользователи')
        print( alldata.menulevel())
        alldata.usersupdate(alldata.users)
        checkmessage=alldata.menulevel()
        checkmessage='Работа с '+checkmessage
        await message.answer(checkmessage, reply_markup=keyboard1)
        checkmessage='Список пользователей'
        await message.answer(checkmessage, reply_markup=keyboard1)
        userlistmessage()
        await message.answer(checkmessage, reply_markup=keyboard1)
        checkmessage=alldata.userlist()
        print(alldata.userlist())
        await message.answer(checkmessage, reply_markup=keyboard1)
     
        
        alldata.usersupdate(alldata.users)
        userlistmessage()
        # for num in range(len(alldata.users)):
            # checkmessage=alldata.users[num]
            # if checkmessage:
                # await message.answer(checkmessage, reply_markup=keyboard1)

        checkmessage='Для добавления или удаления пользователя отправьте имя пользователя со знаком минус или плюс (например -user)  и нажмите нужную кнопку'
        await message.answer(checkmessage, reply_markup=keyboard1)        
        #print(checkmessage)
    elif message.text.lower() == 'боксы':
        alldata.menulevel('боксы')
        checkmessage=alldata.boxlist()
        await message.answer(checkmessage, reply_markup=keyboard1)
        print(checkmessage) 
    elif message.text.lower() == 'состояние':
        alldata.menulevel('состояние')
        checkmessage=alldata.userboxes
        await message.answer(checkmessage, reply_markup=keyboard1)
        print(checkmessage) 
    elif message.text.lower() == 'список':
        menulevel=alldata.menulevel()
        checkmessage='Список'+menulevel
        if menulevel=='боксы':
                checkmessage=alldata.boxlist()
                await message.answer(checkmessage, reply_markup=keyboard1)
        if menulevel=='пользователи':
                checkmessage=alldata.userlist()
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
        checkmessage='Добавление...'
        await message.answer(checkmessage, reply_markup=keyboard1)
        alldata.userappend(alldata.inputtextstr)
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
    alldata.inputtextstr=message.text
    valuetocmd=''
    if message.text[0]=='-': 
        valuetocmd=message.text[1:]
    if message.text[0]=='+': 
        valuetocmd=message.text[1:]
    alldata.inputtextstr=valuetocmd
    print(alldata.inputtextstr)
    print(message.text[0])
    print(message.text[1:])
    print(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
