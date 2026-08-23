import logging


def get_logger(name="drift_monitor"):
    """
    Create and return a configured logger.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # Console handler
    handler = logging.StreamHandler()

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger