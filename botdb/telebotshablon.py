#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import dialog
import logging
import telegram
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    
def dial(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    #answer=dialog.dialog(update.message.text)
    answer=dialog.dialog(update.message.text)
    print(answer)
#    keyboard = telegram.replykeyboardmarkup(resize_keyboard = True)
#    buttons = ['Выбрать','Состояние','Разблокировать', 'Заблокировать']
#    keyboard.add(*buttons)
#    reply_keyboard =eval("[['Boy', 'Girl', 'Other', 'Girl', 'Other', 'Girl', 'Other', #'Girl', 'Other'],['Boy', 'Girl', 'Other']]")
    reply_keyboard =eval(answer[1])
    #reply_keyboard = ['это просто чудо']
#    update.message.reply_text(answer, reply_markup=ReplyKeyboardMarkup(reply_keyboard, #one_time_keyboard=True, input_field_placeholder='Boy or Girl?'))
    update.message.reply_text(answer[0], reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard = True))
    exec(answer[2])
    

def main() -> None:
    #TOKEN = "1911835109:AAFn5iq-Y9ufv-kqXMjH13OgwJ9hT1j2fBU"
    #Here is the token for bot голос @Cheluskinbot:
    TOKEN = "720456901:AAHKxg2WHPqaaIemulTkO3x7IXGD-IZSd-w"
    #"""Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)
    #keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, dial))
    dispatcher.add_handler(MessageHandler(Filters.all, dial))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()