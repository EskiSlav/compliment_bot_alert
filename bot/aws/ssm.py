from __future__ import annotations

import logging

import boto3

logger = logging.getLogger(__name__)


def get_ssm_parameter_value(parameter_string, ssm_client=None):
    if ssm_client is None:
        ssm_client = boto3.client('ssm')

    parameter = ssm_client.get_parameter(
        Name=parameter_string, WithDecryption=True,
    )

    logger.info(f'Retreived SSM parameter {parameter_string}')

    return parameter['Parameter']['Value']
