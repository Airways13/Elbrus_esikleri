import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

# .env faylidan tokenni yuklash
load_dotenv()
TOKEN = os.getenv("7716542752:AAGAUkRP7OYT1YSPe4wLU5OacW1u5fzfMJk")

# Bot va dispatcher yaratish
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Logger sozlash
logging.basicConfig(level=logging.INFO)

# Start komandasi
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Bu buxgalteriya bot. Savol olish uchun /quiz ni bosing.")

# Botni ishga tushirish
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
