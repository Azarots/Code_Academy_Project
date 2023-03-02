import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("Game_Logger.log")
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
