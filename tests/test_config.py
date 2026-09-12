import pytest

from smart_ats.config import (
    AppConfig,
    ConfigurationError,
    load_config,
    validate_config,
)


def test_load_config_uses_defaults(
    monkeypatch,
):
    monkeypatch.delenv(
        "LLM_MODE",
        raising=False,
    )
    monkeypatch.delenv(
        "DEEPSEEK_API_KEY",
        raising=False,
    )
    monkeypatch.delenv(
        "LOG_LEVEL",
        raising=False,
    )

    config = load_config(load_environment_file=False)

    assert config.llm_mode == "mock"
    assert config.deepseek_api_key is None
    assert config.log_level == "INFO"


def test_load_config_normalizes_values(
    monkeypatch,
):
    monkeypatch.setenv(
        "LLM_MODE",
        "MOCK",
    )
    monkeypatch.setenv(
        "LOG_LEVEL",
        "debug",
    )
    monkeypatch.delenv(
        "DEEPSEEK_API_KEY",
        raising=False,
    )

    config = load_config(load_environment_file=False)

    assert config.llm_mode == "mock"
    assert config.log_level == "DEBUG"


def test_deepseek_mode_requires_api_key():
    config = AppConfig(
        llm_mode="deepseek",
        deepseek_api_key=None,
        log_level="INFO",
    )

    with pytest.raises(ConfigurationError):
        validate_config(config)


def test_deepseek_mode_accepts_api_key():
    config = AppConfig(
        llm_mode="deepseek",
        deepseek_api_key="test-key",
        log_level="INFO",
    )

    validate_config(config)


def test_invalid_llm_mode_is_rejected():
    config = AppConfig(
        llm_mode="unknown",
        deepseek_api_key=None,
        log_level="INFO",
    )

    with pytest.raises(ConfigurationError):
        validate_config(config)


def test_invalid_log_level_is_rejected():
    config = AppConfig(
        llm_mode="mock",
        deepseek_api_key=None,
        log_level="LOUD",
    )

    with pytest.raises(ConfigurationError):
        validate_config(config)
