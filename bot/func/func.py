from __future__ import annotations

import logging

import openai
from aws.dynamodb import DynamoDB
from aws.models import NewCompliment
from aws.ssm import get_ssm_parameter_value
from tg.bot import Bot
from tg.models import User
logger = logging.getLogger(__name__)

openai.api_key = get_ssm_parameter_value('/config/bot/openai_api_token')
bot = Bot()
db = DynamoDB()


def generate_compliment():
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt='Give me a compliment in original manner',
        temperature=0.9,
        max_tokens=2048,
    )
    logger.debug(f'OpenAI {response=}')
    return response['choices'][0]['text']


def send_compliments():
    logger.debug('Starting sending compliments')

    users = db.get_all_users()

    for user in users:
        u = User(**user)
        compliment = NewCompliment(generate_compliment())
        db.put_compliment(compliment)
        bot.send_message(u.id, compliment.compliment_ua)
