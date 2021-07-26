import telebot
from telebot import types

bot = telebot.TeleBot("", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)

@bot.message_handler()

def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать ")
    bot.send_message(message.chat.id, "Ваше имя пользователя - "+ message.from_user.username)
    bot.send_message(message.chat.id, "Ваш телеграм id - "+ str(message.from_user.id))
    bot.send_message(message.chat.id, "Ваша регистрация в системе - "+ " нет регистрации")
    bot.send_message(message.chat.id, "Для регистрации необходимо согласиться с условиями регистрации")
    file='registration.pdf'
    with open("C:/install/botdb/registration.pdf","rb") as misc:
        f=misc.read()
        bot.send_document(message.chat.id,f)

def keyphone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    request_yes = False
    request_not = False
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_yes = types.KeyboardButton(text="Согласиться с условиями")
    button_not = types.KeyboardButton(text="Не согласиться с условиями")
    keyboard.add(button_yes, button_not)
    bot.send_message(message.chat.id, "Соглашайся с условиями и продолжим дальше...", reply_markup=keyboard)

    
if __name__ == '__main__':
     bot.infinity_polling()
