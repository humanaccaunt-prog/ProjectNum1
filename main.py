import telebot
from dotenv import load_dotenv
import os
import time

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Будь лакса, спробуйте цi команди!!!!:\n/start\n/help\n/potushno\n/python"
    )


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        "Доступнi потужно-команди:\n/start\n/help\n/potushno\n/python"
    )


@bot.message_handler(commands=['potushno'])
def potushno_handler(message):
    bot.reply_to(
        message,
        "Т-Т-ТИ С-С-С-КАЗАВ ПОТУЖНО???????"
    )

    time.sleep(3)

    for i in range(40):
        bot.reply_to(
            message,
            "ПОТУЖНОOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
        )
    with open("video.mp4", "rb") as video:
        bot.send_video(message.chat.id, video)

@bot.message_handler(commands=['python'])
def python_handler(message):
    bot.reply_to(
        message,
        "Т-Т-ТИ С-С-С-КАЗАВ PYTHON???????"
    )

    time.sleep(3)

    for i in range(40):
        bot.reply_to(
            message,
            "PYTHOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON"
        )
    with open("video.mp4", "rb") as video:
        bot.send_video(message.chat.id, video)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    bot.reply_to(
        message,
        f"Ти написав потужний текст: {message.text}"
    )

print("Бот запущен...")
bot.infinity_polling()