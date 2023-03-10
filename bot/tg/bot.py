from __future__ import annotations

import logging

import requests

logger = logging.getLogger(__name__)


class Bot:
    def __init__(self, token) -> None:
        self.token = token
        self.session = requests.Session()
        self.request_string = f'https://api.telegram.org/bot{self.token}/'
        logger.info('Bot is initialized')

    def send_message(self, chat_id: int, text: str, parse_mode: str = 'MarkdownV2'):
        url = self.request_string + 'sendMessage'
        json_data = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': parse_mode,
        }

        logger.debug(f'Sending message: {json_data=}')
        response = self.session.post(url=url, json=json_data)
        logger.info(f'Sent message to {chat_id}')
        logger.debug(f'{response.status_code=}')
        logger.debug(f'{response.text=}')

        return response.status_code
