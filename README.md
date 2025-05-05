# 💊 Telegram Бот: Онлайн-Фармацевт

Цей бот використовує OpenAI (GPT-4), щоб надавати стислі, точні та прості відповіді на запити щодо ліків: дозування, показання, протипоказання, побічні дії, взаємодія.

> ⚠️ Бот не ставить діагнозів. За потреби рекомендує звернутися до лікаря чи фармацевта.

---

## 🚀 Як розгорнути на Render

1. Форкни цей репозиторій на GitHub.
2. Зайди на [https://render.com](https://render.com) → New Web Service.
3. Обери свій репозиторій → Render зчитає `render.yaml`.
4. Додай змінні середовища:

- `TELEGRAM_TOKEN` – токен твого бота
- `OPENAI_API_KEY` – твій ключ OpenAI

5. Натисни “Deploy”.

---

## 🔧 Налаштування локально (для тесту)

```bash
pip install -r requirements.txt
export TELEGRAM_TOKEN=...
export OPENAI_API_KEY=...
python bot.py
