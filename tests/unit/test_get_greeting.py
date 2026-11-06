from flask_day_54.application.get_greeting import get_greeting


def test_get_greeting_returns_hello_world() -> None:
    assert get_greeting() == "Hello, World!"
