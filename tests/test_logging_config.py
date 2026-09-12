import logging

from smart_ats.logging_config import (
    configure_logging,
)


def test_configure_logging_sets_info_level():
    configure_logging("INFO")

    root_logger = logging.getLogger()

    assert root_logger.level == logging.INFO


def test_configure_logging_sets_debug_level():
    configure_logging("DEBUG")

    root_logger = logging.getLogger()

    assert root_logger.level == logging.DEBUG
