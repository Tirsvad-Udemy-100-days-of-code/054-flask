## @file test_domain_constants.py
#  @brief Unit tests for the domain constants.
"""Unit tests for the domain constants."""

from flask_day_54.domain import constants


def test_greeting_has_expected_value() -> None:
    assert constants.GREETING == "Hello, World!"


def test_greeting_is_not_empty() -> None:
    assert constants.GREETING.strip() != ""
