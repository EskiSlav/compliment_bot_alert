from __future__ import annotations

import logging

import requests
from aws.ssm import get_ssm_parameter_value

logger = logging.getLogger(__name__)


class Bot:
    def __init__(self, token=None) -> None:
        if token is None:
            token = get_ssm_parameter_value('/config/bot/api_token')

        self.token = token
        self.session = requests.Session()
        self.request_string = f'https://api.telegram.org/bot{self.token}/'

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
