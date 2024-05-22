import logging
import colorlog

def setup_logger(name):
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    ))
    logger = colorlog.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
