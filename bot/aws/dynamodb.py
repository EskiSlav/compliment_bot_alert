from __future__ import annotations

import logging
from hashlib import sha1

import boto3
from tg.models import User

from .models import Compliment

logger = logging.getLogger(__name__)


class DynamoDB:
    USERS_TABLE = 'users'
    COMPLIMENTS_TABLE = 'compliments'

    def __init__(self) -> None:
        self.dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
        logger.info('DynamoDB is initialized')

    def get_all_users(self):
        table = self.dynamodb.Table(DynamoDB.USERS_TABLE)
        users = table.scan()['Items']
        logger.info(f'Retreived all entries from table {DynamoDB.USERS_TABLE}')
        return users

    def put_compliment(self, compliment: Compliment) -> bool:
        table = self.dynamodb.Table(DynamoDB.COMPLIMENTS_TABLE)
        response = table.put_item(
            Item={
                'id': sha1(compliment.compliment.encode()).hexdigest(),
                'compliment': compliment.compliment,
                'translated_compliment': compliment.compliment_ua,
            },
        )
        logger.debug(f'DynamoDB {response=}')
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        if status_code >= 200 and status_code < 300:
            logger.info('Compliment has been put into table')
        else:
            logger.error(
                'Something went wrong when putting compliment into table',
            )
        return bool(status_code)

    def put_user(self, user: User) -> bool:
        table = self.dynamodb.Table(DynamoDB.USERS_TABLE)
        response = table.put_item(
            Item={
                'id': user.id,
                'is_bot': user.is_bot,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'language_code': user.language_code,
            },
        )
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        return bool(status_code)
