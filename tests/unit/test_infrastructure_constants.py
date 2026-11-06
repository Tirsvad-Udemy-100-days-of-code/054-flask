## @file test_infrastructure_constants.py
#  @brief Unit tests for the infrastructure constants.
"""Unit tests for the infrastructure constants."""

from flask_day_54.infrastructure import constants


def test_host_is_loopback() -> None:
    assert constants.HOST == "127.0.0.1"


def test_port_is_int_in_unprivileged_range() -> None:
    assert isinstance(constants.PORT, int)
    assert 1024 <= constants.PORT <= 65535


def test_port_has_expected_value() -> None:
    assert constants.PORT == 5000


def test_debug_is_enabled() -> None:
    assert constants.DEBUG is True


def test_app_module_points_to_presentation_hello() -> None:
    assert constants.APP_MODULE == "flask_day_54.presentation.hello"


def test_flask_app_env_var_name() -> None:
    assert constants.FLASK_APP_ENV_VAR == "FLASK_APP"
