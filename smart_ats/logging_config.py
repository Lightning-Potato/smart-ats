import logging
import os

DEFAULT_LOG_LEVEL = "INFO"


def configure_logging():
    """
    Configures application-wide logging.

    The log level can be controlled through the LOG_LEVEL
    environment variable.
    """

    log_level_name = os.getenv(
        "LOG_LEVEL",
        DEFAULT_LOG_LEVEL,
    ).upper()

    log_level = getattr(
        logging,
        log_level_name,
        logging.INFO,
    )

    logging.basicConfig(
        level=log_level,
        format=("%(asctime)s | %(levelname)s | %(name)s | %(message)s"),
        force=True,
    )
