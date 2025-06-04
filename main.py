import zipfile
import os

# فك ضغط ملف Leecher.zip
if os.path.exists("Leecher.zip"):
    zipfile.ZipFile("Leecher.zip").extractall()

# استيراد البوت بعد فك الضغط
from pyrogram import Client, filters

bot = Client(
    "leech-bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

@bot.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("أهلًا بك في بوت التحميل!")

bot.run()
