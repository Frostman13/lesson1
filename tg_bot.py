import tg_bot_settings

# Подключаем лог
import logging
logging.basicConfig(format='%(name)s - %(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='tg_bot.log'
                    )

# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Приветствие
def start_bot(bot, update):
    start_text = """Привет, {}!

Я простой бот и понимаю только команды: {}
    """.format(update.message.chat.first_name,'/start')
    logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
    update.message.reply_text(start_text)

# Чат-бот
def chat_bot(bot, update):
    text=update.message.text
    logging.info(text)
    update.message.reply_text(text)

def main():
    updater = Updater(tg_bot_settings.TELEGRAM_API_KEY)
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_bot))
    dp.add_handler(MessageHandler(Filters.text, chat_bot))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    logging.info('Bot started')
    main()
