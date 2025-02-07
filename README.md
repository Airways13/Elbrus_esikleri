import logging
import random
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()  # .env faylidan TOKEN ni yuklash
TOKEN = os.getenv("7716542752:AAGAUkRP7OYT1YSPe4wLU5OacW1u5fzfMJk")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Logger sozlash
logging.basicConfig(level=logging.INFO)

# Savollar va variantlar
questions = [
    {"savol": "Qaysi hisob  aktiv hisoblanadi?", "variantlar": ["Kassa", "Ta'minotchilar", "Kredit", "Daromad"], "togri": "Kassa"},
    {"savol": "Qaysi hisob passiv hisoblanadi?", "variantlar": ["Kassa", "Ustav kapitali", "Debitor qarzdorlik", "Xarajatlar"], "togri": "Ustav kapitali"},
    {"savol": "Qaysi operatsiya aktivni oshiradi?", "variantlar": ["Xarajatni kamaytirish", "Kredit olish", "Tulov qilish", "Daromad olish"], "togri": "Daromad olish"},
]

# Start komanda
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Salom! Buxgalteriya test botiga xush kelibsiz! \n /quiz buyrug‘ini bering.")

# Test boshlash
@dp.message_handler(commands=['quiz'])
async def send_question(message: types.Message):
    savol = random.choice(questions)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [types.KeyboardButton(text=var) for var in savol["variantlar"]]
    markup.add(*buttons)
    
    await message.answer(savol["savol"], reply_markup=markup)
    bot_data[message.from_user.id] = savol["togri"]

# Javobni tekshirish
@dp.message_handler()
async def check_answer(message: types.Message):
    togri_javob = bot_data.get(message.from_user.id)
    if togri_javob:
        if message.text == togri_javob:
            await message.answer("✅ To‘g‘ri! Yana savol olish uchun /quiz ni bosing.")
        else:
            await message.answer(f"❌ Noto‘g‘ri. To‘g‘ri javob: {togri_javob}. Yana urinib ko‘ring: /quiz")
    else:
        await message.answer("Iltimos, avval /quiz ni bosing.")

# Botni ishga tushirish
if __name__ == "__main__":
    bot_data = {}  # Foydalanuvchilarning javoblarini saqlash
    executor.start_polling(dp, skip_updates=True)
