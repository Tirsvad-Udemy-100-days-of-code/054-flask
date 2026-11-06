## @file get_greeting.py
#  @brief Use case that provides the greeting.
"""Use case that provides the greeting."""

from flask_day_54.domain.constants import GREETING


## @brief Return the greeting to show the user.
#  @return The greeting text.
def get_greeting() -> str:
    """Return the greeting to show the user."""
    return GREETING
