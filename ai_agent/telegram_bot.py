from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
chat_id = os.getenv('TELEGRAM_CHAT_ID')

def send_alert(ticker, summary, link, impact_score):
    sirens = '🚨' * impact_score
    message = f"{sirens} *{ticker} Alert!* {sirens}\n\n{summary}\n\n[Read more]({link})"
    bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown', disable_web_page_preview=True)
