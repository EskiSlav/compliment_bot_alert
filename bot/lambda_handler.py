from __future__ import annotations

import json
import logging
from logging.config import dictConfig

from config.config import logging_config
from func import func

dictConfig(logging_config)
logger = logging.getLogger(__name__)


def main(event, context):
    logger.debug(event)

    logger.info('WTF1')
    func.send_compliments()
    logger.info('WTF2')

    body = json.dumps({
        'status': 200,
    })
    ret = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'body': body,
    }
    return ret


def lambda_handler(event, context):
    return main(event, context)


# import json
# import openai
# import boto3
# import logging
# from logging.config import dictConfig
# from config.config import logging_config
# from func.func import send_compliments
# from aws.ssm import get_ssm_parameter_value
# from tg.bot import Bot

# dictConfig(logging_config)
# logger = logging.getLogger(__name__)

# openai_api = get_ssm_parameter_value('/config/bot/openai_api_token')
# openai.api_key = openai_api


# def lambda_handler(event, context):
#     send_compliments()
#     return {
#         'statusCode': 200,
#         'body': 'Compliment'
#     }
