## @file hello.py
#  @brief The minimal Flask application of lectures 1 and 2.
"""The minimal Flask application of lectures 1 and 2."""

from flask import Flask

from flask_day_54.application.get_greeting import get_greeting

## @brief The Flask application object.
app = Flask(__name__)


## @brief Handle GET / and answer with the greeting.
#  @return The greeting as the response body.
@app.route("/")
def hello_world() -> str:
    """Answer the root route with the greeting."""
    return get_greeting()
