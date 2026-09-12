import os
from dataclasses import dataclass

from dotenv import load_dotenv


DEFAULT_LLM_MODE = "mock"
DEFAULT_LOG_LEVEL = "INFO"

SUPPORTED_LLM_MODES = {
    "mock",
    "deepseek",
}

SUPPORTED_LOG_LEVELS = {
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL",
}


class ConfigurationError(ValueError):
    """
    Raised when application configuration is invalid.
    """


@dataclass(frozen=True)
class AppConfig:
    llm_mode: str
    deepseek_api_key: str | None
    log_level: str


def load_config(
    load_environment_file=True,
):
    """
    Loads and validates application configuration.
    """

    if load_environment_file:
        load_dotenv()

    llm_mode = os.getenv(
        "LLM_MODE",
        DEFAULT_LLM_MODE,
    ).lower()

    deepseek_api_key = os.getenv(
        "DEEPSEEK_API_KEY"
    )

    log_level = os.getenv(
        "LOG_LEVEL",
        DEFAULT_LOG_LEVEL,
    ).upper()

    config = AppConfig(
        llm_mode=llm_mode,
        deepseek_api_key=deepseek_api_key,
        log_level=log_level,
    )

    validate_config(config)

    return config


def validate_config(config):
    """
    Validates application configuration.
    """

    if config.llm_mode not in SUPPORTED_LLM_MODES:
        raise ConfigurationError(
            "Unsupported LLM_MODE. "
            "Expected 'mock' or 'deepseek'."
        )

    if (
        config.llm_mode == "deepseek"
        and not config.deepseek_api_key
    ):
        raise ConfigurationError(
            "DEEPSEEK_API_KEY is required "
            "when LLM_MODE=deepseek."
        )

    if config.log_level not in SUPPORTED_LOG_LEVELS:
        raise ConfigurationError(
            "Unsupported LOG_LEVEL."
        )