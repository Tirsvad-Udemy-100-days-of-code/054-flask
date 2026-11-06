## @file hello.py
#  @brief The minimal Flask application of lectures 1 to 4.
"""The minimal Flask application of lectures 1 to 4."""

from flask import Flask

from flask_day_54.application.get_greeting import get_greeting
from flask_day_54.infrastructure.constants import DEBUG, HOST, PORT

## @brief The Flask application object.
app = Flask(__name__)


## @brief Handle GET / and answer with the greeting.
#  @return The greeting as the response body.
@app.route("/")
def hello_world() -> str:
    """Answer the root route with the greeting."""
    return get_greeting()


## @brief Start the Flask development server with the configured settings.
def main() -> None:
    """Run the development server using the infrastructure settings."""
    app.run(host=HOST, port=PORT, debug=DEBUG)


if __name__ == "__main__":
    main()
