"""Main logger config.
"""

import logging

logging.basicConfig(level=logging.DEBUG)

LOGGER_MAIN_NAME = "LOG"

logger = logging.getLogger(f'{LOGGER_MAIN_NAME}')
