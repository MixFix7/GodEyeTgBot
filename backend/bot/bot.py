from telebot.async_telebot import AsyncTeleBot
from django.conf import settings
from . import messages
import requests


bot = AsyncTeleBot(settings.BOT_TOKEN, parse_mode='HTML')

state = {}
server_url = 'http://localhost:8000'


async def main():
    webhook_url = f"{server_url}/tg-bot/telegram-bot-webhook/"
    await bot.remove_webhook()
    await bot.set_webhook(url=webhook_url)


""" COMMAND HANDLERS """


@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, messages.start_message)


@bot.message_handler(commands=['find_person'])
async def handler_find_person(message):
    await bot.send_message(message.chat.id, messages.find_person_message)
    state[message.from_user.id] = 'finding_person'


""" COMMANDS FUNCTIONS """


@bot.message_handler(func=lambda message: state.get(message.chat.id) is None)
async def unknown_command(message):
    await bot.send_message(message.chat.id, messages.unknown_command_message)


@bot.message_handler(func=lambda message: state.get(message.from_user.id) == 'finding_person')
async def find_person(message):
    text_lines = message.text.split('\n')
    data = {}
    for line in text_lines:
        key, value = line.split(' - ')
        data[key] = value

    response = requests.post(f"{server_url}/data/find-person/", data=data)
    persons_data = response.json()

    if persons_data:
        for person in persons_data:
            person_data = f"<b> --- DATA OF {person['name']} --- </b>"
            person_data += "\n"
            for field, value in person.items():
                if field != 'social_data':
                    person_data += f"\n{field}: {value}"
            else:
                person_data += "\n"
            if 'social_data' in person and person['social_data']:
                social_data = f"<b> --- SOCIAL --- </b>"
                person_data += "\n"
                for social_field, social_value in person['social_data'][0].items():
                    social_data += f"\n{social_field}: {social_value}"
                person_data += social_data
            await bot.send_message(message.chat.id, person_data)

    else:
        await bot.send_message(message.chat.id, messages.nothing_found_message)



