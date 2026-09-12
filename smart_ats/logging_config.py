import logging


def configure_logging(log_level):
    """
    Configures application-wide logging.
    """

    numeric_level = getattr(
        logging,
        log_level,
        logging.INFO,
    )

    logging.basicConfig(
        level=numeric_level,
        format=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),
        force=True,
    )