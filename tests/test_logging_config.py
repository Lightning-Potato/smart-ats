import logging

from smart_ats.logging_config import configure_logging


def test_configure_logging_sets_default_level(
    monkeypatch,
):
    monkeypatch.delenv(
        "LOG_LEVEL",
        raising=False,
    )

    configure_logging()

    root_logger = logging.getLogger()

    assert root_logger.level == logging.INFO


def test_configure_logging_uses_environment_level(
    monkeypatch,
):
    monkeypatch.setenv(
        "LOG_LEVEL",
        "DEBUG",
    )

    configure_logging()

    root_logger = logging.getLogger()

    assert root_logger.level == logging.DEBUG


def test_invalid_log_level_falls_back_to_info(
    monkeypatch,
):
    monkeypatch.setenv(
        "LOG_LEVEL",
        "NOT_A_LEVEL",
    )

    configure_logging()

    root_logger = logging.getLogger()

    assert root_logger.level == logging.INFO
