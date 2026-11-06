from collections.abc import Callable

from flask_day_54.domain.decorators import (
    make_bold,
    make_emphasis,
    make_underlined,
    plain_hello,
    say_hello,
)


def test_make_bold_wraps_text_in_b_tags() -> None:
    assert make_bold(plain_hello)() == "<b>Hello, World!</b>"


def test_make_emphasis_wraps_text_in_em_tags() -> None:
    assert make_emphasis(plain_hello)() == "<em>Hello, World!</em>"


def test_make_underlined_wraps_text_in_u_tags() -> None:
    assert make_underlined(plain_hello)() == "<u>Hello, World!</u>"


def test_say_hello_applies_stacked_decorators_nearest_first() -> None:
    assert say_hello() == "<b><em><u>Hello, World!</u></em></b>"


def test_plain_hello_is_not_decorated() -> None:
    assert plain_hello() == "Hello, World!"


def test_decorator_keeps_name_and_docstring_of_wrapped_function() -> None:
    assert say_hello.__name__ == "say_hello"
    assert say_hello.__doc__ == "Return the greeting."


def test_decorator_wraps_function_returning_another_string() -> None:
    def goodbye() -> str:
        return "Bye"

    decorated: Callable[[], str] = make_bold(goodbye)

    assert decorated() == "<b>Bye</b>"
