## @file first_class_functions.py
#  @brief Lecture 5 demo of functions as first-class objects.
"""Functions can be passed as arguments, nested and returned like any value."""

from collections.abc import Callable

from flask_day_54.domain.constants import (
    ADD_DEMO_LINE,
    NESTED_FUNCTION_MESSAGE,
    OUTER_DEMO_LINE,
    RETURNED_DEMO_LINE,
    SUBTRACT_DEMO_LINE,
)


## @brief Add two numbers.
def add(n1: float, n2: float) -> float:
    """Return the sum of the two numbers."""
    return n1 + n2


## @brief Subtract the second number from the first.
def subtract(n1: float, n2: float) -> float:
    """Return the first number minus the second."""
    return n1 - n2


## @brief Apply a function passed as argument to two numbers.
#  @param func The function to call with `n1` and `n2`.
def calculate(n1: float, n2: float, func: Callable[[float, float], float]) -> float:
    """Return `func(n1, n2)`."""
    return func(n1, n2)


## @brief Call a function that is defined inside this one.
def outer_function() -> str:
    """Return the result of the nested function, reachable only in here."""

    def nested_function() -> str:
        return NESTED_FUNCTION_MESSAGE

    return nested_function()


## @brief Hand the nested function to the caller.
def returns_nested_function() -> Callable[[], str]:
    """Return the nested function so it can be stored and called later."""

    def nested_function() -> str:
        return NESTED_FUNCTION_MESSAGE

    return nested_function


## @brief Print the lecture 5 demo.
def main() -> None:
    """Print the results of the first-class function examples."""
    print(ADD_DEMO_LINE.format(value=calculate(2, 3, add)))
    print(SUBTRACT_DEMO_LINE.format(value=calculate(5, 3, subtract)))
    print(OUTER_DEMO_LINE.format(value=outer_function()))
    stored = returns_nested_function()
    print(RETURNED_DEMO_LINE.format(value=stored()))


if __name__ == "__main__":
    main()
