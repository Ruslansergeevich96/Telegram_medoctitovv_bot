from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
from telegram import Update

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Задаем токен бота
TOKEN = "YOUR_BOT_TOKEN"

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f"Hello {user.first_name}, I am your bot!")

def main() -> None:
    updater = Updater(token=TOKEN, use_context=True)  # Создаем экземпляр класса Updater

    dp = updater.dispatcher  # Получаем диспетчер для регистрации обработчиков

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Начинаем поиск обновлений
    updater.start_polling()

    # Держим бота активным до принудительной остановки
    updater.idle()

if __name__ == '__main__':
    main()