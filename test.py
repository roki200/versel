import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Установка логирования
logging.basicConfig(level=logging.INFO)

# Токен вашего бота
API_TOKEN = '6581576935:AAER5ITDyFcGgOQ-pnCZ7zabkTtj3yMbUe4'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Отправка приветственного сообщения
    await message.reply("Привет! Я бот-приветствие.")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
