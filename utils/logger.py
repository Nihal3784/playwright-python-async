import logging


def get_logger():
    logger = logging.getLogger("AutomationLogger")
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler("automation.log")
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
