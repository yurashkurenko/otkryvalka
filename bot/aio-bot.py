from aiogram import Bot, Dispatcher, executor, types
import requests
import aiogram
import logging
import fnmatch
import rooms
global select_room
select_room=rooms.all[0]
print(rooms.server)
print(rooms.room9003key)
logging.basicConfig(level=logging.INFO)
## 1676613896:AAE1ujeUGNZDDrbib45kgIz9Xq49x0hqYmw
bot = Bot(token="1676613896:AAE1ujeUGNZDDrbib45kgIz9Xq49x0hqYmw")
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ['Выбрать','Состояние','Открыть', 'Закрыть']
keyboard.add(*buttons)
#keyboard.add('/start','Состояние','Открыть', 'Закрыть', 'Выбрать' )    
dp = Dispatcher(bot)
@dp.message_handler()
#def checkdoor():
#    messagetext='123'
#    checkdoor=messagetext
#http://blynk-cloud.com/auth_token/update/pin?value=value



async def cmd_start(message: types.Message):
#    print(message)
#    print(message.chat.username)
    global select_room
#    if message.chat.username == 'yurasoft1972':
#        await message.answer('У Вас нет доступа к управлению')
    if message.text.lower() == 'закрыть':
        rooms.door_check()
        await message.answer('Комната № '+select_room+ ' Дверь закрыта', reply_markup=keyboard)
#        print('Комната №  Дверь закрыта')
    elif message.text.lower() == 'состояние':
#        checkdoor(server,select_room)
#        checkdoor()
#        print(checkdoor)
        await message.answer('Выбрана Комната №  '+select_room+ '  Дверь закрыта', reply_markup=keyboard)
    elif message.text.lower() == 'открыть':
        await message.answer('Комната №  '+select_room+ '  Дверь открыта', reply_markup=keyboard)
        print('Комната №  Дверь открыта') 
    elif message.text.lower() == 'выбрать':
        await message.answer('Показываю комнаты, хозяин', reply_markup=keyboard)
        for room in rooms.all:
            await message.answer('/'+room+'   Дверь закрыта.', reply_markup=keyboard)      
    elif fnmatch.fnmatch(message.text, "/?00?"):
        print(message.text)
        select_room=message.text[1:]
        print(select_room)
        await message.answer('Выбрана комната №' + select_room, reply_markup=keyboard)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)