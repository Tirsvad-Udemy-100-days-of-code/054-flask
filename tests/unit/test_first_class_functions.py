from flask_day_54.domain import first_class_functions
from flask_day_54.domain.first_class_functions import (
    add,
    calculate,
    outer_function,
    returns_nested_function,
    subtract,
)


def test_add_returns_sum_of_two_numbers() -> None:
    assert add(2, 3) == 5


def test_subtract_returns_difference_of_two_numbers() -> None:
    assert subtract(5, 3) == 2


def test_calculate_applies_add_when_add_is_passed() -> None:
    assert calculate(2, 3, add) == 5


def test_calculate_applies_subtract_when_subtract_is_passed() -> None:
    assert calculate(5, 3, subtract) == 2


def test_calculate_applies_lambda_when_lambda_is_passed() -> None:
    assert calculate(4, 3, lambda n1, n2: n1 * n2) == 12


def test_outer_function_returns_nested_function_result() -> None:
    assert outer_function() == "Hello from the nested function"


def test_returned_nested_function_is_callable_independently() -> None:
    stored = returns_nested_function()

    assert stored() == "Hello from the nested function"


def test_nested_function_is_not_a_module_attribute() -> None:
    assert not hasattr(first_class_functions, "nested_function")
