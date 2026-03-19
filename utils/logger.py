import logging

def get_logger():
    logger = logging.getLogger("automation")

    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger