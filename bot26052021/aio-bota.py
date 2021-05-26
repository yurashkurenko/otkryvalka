from aiogram import Bot, Dispatcher, executor, types
import requests
import aiogram
import logging
import fnmatch
import rooms
global select_room
import userrooms
#select_room=''
#select_room=rooms.all[0]
#print(rooms.server)
#print(rooms.room9003key)
logging.basicConfig(level=logging.INFO)
## 1676613896:AAE1ujeUGNZDDrbib45kgIz9Xq49x0hqYmw
bot = Bot(token="1676613896:AAE1ujeUGNZDDrbib45kgIz9Xq49x0hqYmw")
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ['Выбрать','Состояние','Разблокировать', 'Заблокировать']
keyboard.add(*buttons)
checkmessage='Здравствуйте'
#keyboard.add('Состояние','Открыть', 'Закрыть', 'Выбрать' )    
dp = Dispatcher(bot)
@dp.message_handler()
#def checkdoor():
#    messagetext='123'
#    checkdoor=messagetext
#http://blynk-cloud.com/auth_token/update/pin?value=value
#        await message.answer('Комната № '+select_room+ ' Дверь закрыта', reply_markup=keyboard)
#        print('Комната №  Дверь закрыта')
#        checkdoor(server,select_room)
#        checkdoor()
#        print(checkdoor)

async def cmd_start(message: types.Message):
    select_room=''
    select_room1=''
    message_chat_username='@'+message.chat.username
    checkrooms=userrooms.roomlist(message_chat_username)
    print(message.chat)
    if not checkrooms:
        await message.answer('У Вас нет доступа к управлению. По вопросам работы бота просьба обращаться @yurasoft1972', reply_markup=keyboard)
    if checkrooms:
        select_room=checkrooms[0]
#        select_room=select_room1
#    print(message)
#    print(message.chat.username)
#    global select_room,checkmessage
    # if not checkrooms:
        # await message.answer('У Вас нет доступа к управлению')
    if message.text.lower() == '/start':
        checkmessage='Добро пожаловать!'
        await message.answer(checkmessage+'По вопросам работы бота просьба обращаться @yurasoft1972', reply_markup=keyboard)
        #print(checkmessage)
    if message.text.lower() == 'заблокировать':
        checkmessage=rooms.door_block(select_room)
        await message.answer(checkmessage, reply_markup=keyboard)
        print(checkmessage)
    elif message.text.lower() == 'состояние':
        print(select_room)
        checkmessage=rooms.door_check(select_room)
        await message.answer(checkmessage, reply_markup=keyboard)
        print(checkmessage)
    elif message.text.lower() == 'разблокировать':
        checkmessage=rooms.door_unblock(select_room)
        await message.answer(checkmessage, reply_markup=keyboard)
        print(checkmessage) 
    elif message.text.lower() == 'выбрать':
        await message.answer('Показываю боксы, хозяин', reply_markup=keyboard)
        for room in checkrooms:
            checkmessage=rooms.door_check(room)
            await message.answer('/'+room+" "+checkmessage, reply_markup=keyboard)      
    elif fnmatch.fnmatch(message.text, "/*00*"):
        print(message.text)
        select_room1=message.text[1:]
        select_room=select_room1
        print(select_room1)
        print(select_room)
        checkmessage=rooms.door_check(select_room)
        await message.answer('Выбран бокс №' + rooms.zeropoint(select_room), reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
