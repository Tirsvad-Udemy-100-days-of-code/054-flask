## @file decorators.py
#  @brief Lecture 6 demo of decorators and the `@` syntax.
"""A decorator wraps a function to add behaviour without editing it."""

from collections.abc import Callable
from functools import wraps

from flask_day_54.domain.constants import (
    AT_SYNTAX_DEMO_LINE,
    BOLD_TAG,
    BY_HAND_DEMO_LINE,
    EMPHASIS_TAG,
    GREETING,
    HTML_TAG_TEMPLATE,
    NAME_DEMO_LINE,
    PLAIN_DEMO_LINE,
    UNDERLINE_TAG,
)


def _tag_decorator(tag: str) -> Callable[[Callable[[], str]], Callable[[], str]]:
    """Build a decorator that wraps the returned text in the given HTML tag."""

    def decorator(func: Callable[[], str]) -> Callable[[], str]:
        @wraps(func)
        def wrapper() -> str:
            return HTML_TAG_TEMPLATE.format(tag=tag, text=func())

        return wrapper

    return decorator


## @brief Wrap the text of a function in `<b>` tags.
make_bold = _tag_decorator(BOLD_TAG)

## @brief Wrap the text of a function in `<em>` tags.
make_emphasis = _tag_decorator(EMPHASIS_TAG)

## @brief Wrap the text of a function in `<u>` tags.
make_underlined = _tag_decorator(UNDERLINE_TAG)


## @brief Greeting with the three decorators stacked; the nearest applies first.
@make_bold
@make_emphasis
@make_underlined
def say_hello() -> str:
    """Return the greeting."""
    return GREETING


## @brief The same greeting without any decorator.
def plain_hello() -> str:
    """Return the greeting."""
    return GREETING


## @brief Print the lecture 6 demo.
def main() -> None:
    """Print the plain, hand-decorated and `@` decorated greeting."""
    print(PLAIN_DEMO_LINE.format(value=plain_hello()))
    print(BY_HAND_DEMO_LINE.format(value=make_bold(plain_hello)()))
    print(AT_SYNTAX_DEMO_LINE.format(value=say_hello()))
    print(NAME_DEMO_LINE.format(value=say_hello.__name__))


if __name__ == "__main__":
    main()
