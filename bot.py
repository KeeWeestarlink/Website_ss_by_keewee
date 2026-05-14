  GNU nano 9.0                     bot.py
import telebot
import requests

BOT_TOKEN = "8784990071:AAGCCkg74boLQjYLCGdPXIQEEoLBFwiL-Yc"

bot = telebot.TeleBot(BOT_TOKEN)

def get_video(url):
    try:
        api = f"https://tikwm.com/api/?url={url}"
        r = requests.get(api).json()
        return r['data']['play']
    except:
        return None

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "TikTok link ပို့ပါ 🎬")

@bot.message_handler(func=lambda m: m.text and "tiktok.com" in m.text)
def download(msg):
    bot.reply_to(msg, "Downloading...⏳")

    video = get_video(msg.text)

    if video:
        try:
            bot.send_video(msg.chat.id, video)
        except:
            bot.reply_to(msg, "Send မရဘူး ❌")
    else:
        bot.reply_to(msg, "Link မှားနေတယ် ❌")

@bot.message_handler(func=lambda m: True)
def other(msg):
    bot.reply_to(msg, "TikTok link ပဲပို့ပါ")

print("Bot running...")
bot.infinity_polling()



