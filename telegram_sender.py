from telegram import Bot
from config import BOT_TOKEN, CHAT_ID

bot = Bot(token=BOT_TOKEN)

def send_message(msg):
    try:
        bot.send_message(
            chat_id=CHAT_ID,
            text=msg,
            parse_mode="Markdown",
            disable_web_page_preview=False
        )
    except Exception as e:
        print("Error enviando mensaje a Telegram:", e)
