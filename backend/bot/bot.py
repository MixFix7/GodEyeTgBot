from telebot.async_telebot import AsyncTeleBot
from django.conf import settings
from . import messages


bot = AsyncTeleBot(settings.BOT_TOKEN, parse_mode='HTML')

state = {}
server_url = 'http://localhost:8000'


async def main():
    webhook_url = f"{server_url}/tg-bot/telegram-bot-webhook/"
    await bot.remove_webhook()
    await bot.set_webhook(url=webhook_url)


"""COMMAND HANDLERS"""


@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, messages.start_message)

