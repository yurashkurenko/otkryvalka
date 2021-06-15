from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
import asyncio
import logging
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
import requests
import aiogram
import logging
import fnmatch
import db
import alldatadb
token="1753263636:AAFrhVi5Qe8MY_qCvuxAa5MjXOAAcJR0zNs"
bot = Bot(token=token)
alldatadb.menulevel(10)
dp = Dispatcher(bot)

@dp.message_handler()
async def cmd_start(message: types.Message):
    messagestring=message.text
    if  messagestring not in ['добавить','удалить','список','назад','пользователи','боксы','управление','бокс']:
        alldatadb.messagestringbuffer(messagestring)
    print(messagestring)
    print(alldatadb.messagestringbuffer())
    state=alldatadb.menulevel()
    print(state)
    buttons=alldatadb.buttonlist(state)
#    keyboard = types.ReplyKeyboardRemove()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    print(buttons)
    messagedb=alldatadb.message(state)
    print(messagedb)
    command=alldatadb.command(state)
    print(command)
    alldatadb.menulevel(state)
    if (message.text.lower() == '/start') or (message.text.lower() == '/help'):
        # msg = text(bold('Я могу ответить на следующие команды:'),
        # '/voice', '/photo', '/group', '/note', '/file, /testpre', sep='\n')
        # await message.answer(msg, parse_mode=ParseMode.MARKDOWN)
        # msg = "Привет!\nНапиши мне что-нибудь!"
        # await message.answer(msg, parse_mode=ParseMode.MARKDOWN)
        startmessage='Добро пожаловать!'
        helpmessage=' Задача управления пользователями сводится к заполнению таблицы пользователей, \
        таблицы боксов и таблицы соответствия боксов и пользователей. \
        Одним боксом может управлять несколько пользователей \
        Для управления боксами нужно выбрать  или добавить и выбрать бокс \
        и добавить к нему существующих или вновь созданных пользователей /12..3 '
        alldatadb.menulevel(10)
        await message.answer(startmessage, parse_mode=ParseMode.MARKDOWN, reply_markup="")
        await message.answer(helpmessage, parse_mode=ParseMode.HTML, reply_markup=keyboard)
#    levelstate=[1,2,3,4,5,6,7,8,9,10]
    else:
        messagestring=message.text
        if messagestring =='назад':
            print(alldatadb.menulevel())
            state=alldatadb.commandlv4(state)
            print(state)
            alldatadb.menulevel(state)
            print(alldatadb.menulevel())
            state=alldatadb.menulevel()
            print(message.text)
            buttons=alldatadb.buttonlist(state)
            keyboard = ''
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*buttons)
            checkmessage='Работа с ' + alldatadb.message(state)
            checkmessage1 = alldatadb.message(state)
#            await message.answer(checkmessage, reply_markup='')
            await message.answer(checkmessage1, reply_markup=keyboard) 
        if messagestring=='список':
            checkmessage=''
            if state=='1':
                checkmessage=state+'\n Список пользователей \n '+alldatadb.userlist()
            if state=='4':
                checkmessage='Уровень '+state+'\n Список боксов  \n'+alldatadb.boxlist()
            if state=='7':
                selectedbox=''
                selectedbox=alldatadb.selectbox()
                checkmessage='Уровень '+state+'\n Список боксов и управляющих ими пользователей \n'
                checkmessage=checkmessage+'\n выбран бокс\n '+selectedbox
                checkmessage=checkmessage+'\n управляющие пользователи \n'+alldatadb.listboxusers(selectedbox)
            await message.answer(checkmessage, reply_markup=keyboard)
        if messagestring=='добавить':
            #checkmessage='Для добавления пользователя отправьте имя пользователя и нажмите кнопку добавление'
            msb2=alldatadb.messagestringbuffer()
            if state=='1':
                checkmessage=state+' Для добавления пользователя отправьте имя пользователя и нажмите кнопку добавление'
                alldatadb.insertuser(msb2)
                msb2=''
            if state=='4':
                checkmessage=state+' Для добавления бокса отправьте номер бокса и нажмите кнопку добавление'
                alldatadb.insertbox(msb2)
                msb2=''
            if state=='7':
                boxuser=''
                selectedbox=''
                selecteduser=''
                boxuser=msb2
                selectedbox=alldatadb.selectbox()
                alldatadb.selectuser(boxuser)
                selecteduser=alldatadb.selectuser()
                alldatadb.insertboxuser(boxuser,selectedbox)
                msb2=''
                checkmessage='Уровень '+state+'\n Выбран бокс '+selectedbox+'\n'
                checkmessage=checkmessage+'На данном этапе нужно выбрать пользователей для бокса '+selectedbox+'\n'
                checkmessage=checkmessage+'Сейчас боксом могут управлять следующие пользователи \n'+alldatadb.listboxusers(selectedbox)
                alldatadb.insertboxuser(selectedbox,selecteduser)
            await message.answer(checkmessage, reply_markup=keyboard)
        if messagestring=='удалить':
            #checkmessage='Для удаления пользователя выберите имя пользователя и нажмите кнопку удаление'
            msb2=alldatadb.messagestringbuffer()
            if state=='1':
                checkmessage=state+' Для удаления пользователя отправьте имя пользователя и нажмите кнопку удаление'
                alldatadb.deleteuser(msb2)
            if state=='4':
                checkmessage=state+' Для удаления бокса отправьте номер бокса и нажмите кнопку удаление'
                alldatadb.deletebox(msb2)   
            if state=='7':
                boxuser=''
                selectedbox=''
                selecteduser=''
                boxuser=msb2
                selectedbox=alldatadb.selectbox()
                alldatadb.selectuser(boxuser)
                selecteduser=alldatadb.selectuser()
                alldatadb.deleteboxuser(selectedbox,boxuser)
                msb2=''
                checkmessage=state+' Для удаления пользователя из управления боксом  отправьте имя пользователя и нажмите кнопку удаление'
            await message.answer(checkmessage, reply_markup=keyboard)
        if messagestring=='бокс':
            msb2=alldatadb.messagestringbuffer()
            if state=='7':
                checkmessage='Уровень '+state+' \nСписок боксов \n \n'+alldatadb.boxlist()
                checkmessage=checkmessage+'\n \nВыберите бокс для управления \nи отправьте название бокса.\n Для выбора бокса нажмите кнопку бокс.\n'
                selectbox=msb2
                alldatadb.selectbox(selectbox)
                checkmessage=checkmessage+'\n Выбран бокс '+alldatadb.selectbox()+'\n'
                await message.answer(checkmessage, reply_markup=keyboard)
        if messagestring=='пользователи':
            msb2=alldatadb.messagestringbuffer()
            if state=='7':
                selectuser=''
                selectuser=msb2
                checkmessage='Уровень '+state+'\n Выбран бокс '+msb2+'\n'
                checkmessage=checkmessage+'На данном этапе нужно выбрать пользователей для бокса '+msb2+'\n'
                checkmessage=checkmessage+'Сейчас боксом могут управлять следующие пользователи \n'+alldatadb.listboxusers(msb2)
                await message.answer(checkmessage, reply_markup=keyboard)
        str1=alldatadb.commandlv3(state)
        print(str1)
        levelstate=str1.split(' ')
        print(levelstate)
        for i in range(len(levelstate)):
            messagetocompare=alldatadb.commandlv1(levelstate[i])
            messagestring=message.text[0:5]
            if messagestring in messagetocompare:
                alldatadb.menulevel(levelstate[i])
                state=alldatadb.menulevel()
                print(message.text)
                print(messagetocompare)
                print(state)
                buttons=alldatadb.buttonlist(state)
                keyboard = ''
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(*buttons)
                checkmessage='Работа с ' + alldatadb.message(state)
                checkmessage1 = alldatadb.message(state)
                await message.answer(checkmessage, reply_markup='')
                await message.answer(checkmessage1, reply_markup=keyboard) 
                
#    if messagestring=='список' and state in [1,2,3]:
    # if messagestring=='список':
        # if state=='7':
            # checkmessage='\nСписок боксов и управляющих ими пользователей\n'
            # alldatadb.userlist()
            # await message.answer(checkmessage, reply_markup=keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
