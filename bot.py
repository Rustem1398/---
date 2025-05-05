import openai
from aiogram import Bot, Dispatcher, types, executor
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

SYSTEM_PROMPT = (
    "Ти — сертифікований фармацевт, який консультує клієнтів на основі інструкцій до ліків. "
    "Твоя задача — стисло, точно та простою мовою відповідати на запити про дозування, показання, "
    "протипоказання, побічні дії, а також взаємодію ліків. Не ставиш діагнозів. "
    "Якщо є сумніви — рекомендуєш звернутися до лікаря або фармацевта."
)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.text}
            ],
            temperature=0.5,
            max_tokens=500
        )
        answer = response['choices'][0]['message']['content']
        await message.answer(answer)
    except Exception as e:
        await message.answer("Сталася помилка. Спробуйте пізніше.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
