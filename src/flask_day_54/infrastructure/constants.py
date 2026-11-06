## @file constants.py
#  @brief Constants of the infrastructure layer (server settings).
"""Server settings used by the entry point."""

from typing import Final

## @brief Interface the development server binds to.
HOST: Final[str] = "127.0.0.1"

## @brief TCP port of the development server.
PORT: Final[int] = 5000

## @brief Whether the development server runs in debug mode.
DEBUG: Final[bool] = True

## @brief Dotted module path of the Flask application.
APP_MODULE: Final[str] = "flask_day_54.presentation.hello"

## @brief Name of the environment variable Flask reads to find the application.
FLASK_APP_ENV_VAR: Final[str] = "FLASK_APP"
