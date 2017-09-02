# Подключаем лог
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='tg_bot.log'
                    )

# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
    updater = Updater("439722062:AAGMI4F-7lHD1lJ_hNbXPNnt5WWCBZvX3Cc")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

# Вызываем функцию - эта строчка собственно запускает бота
main()

