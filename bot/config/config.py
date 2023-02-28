from __future__ import annotations

import logging

FORMAT = '[%(levelname)s] %(asctime)s %(name)s %(funcName)s: %(message)s'
LOGGING_LEVEL = logging.DEBUG

logging_config = {
    'version': 1,
    'formatters': {
        'default': {
            'format': FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': LOGGING_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {
            'level': LOGGING_LEVEL,
            'handlers': ['console'],
        },
    },
    'disable_existing_loggers': True,
}


logger = logging.getLogger(__name__)
