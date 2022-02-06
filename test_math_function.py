"""
Unit Test for math_function
"""
import math_function


def test_add_():
    assert math_function.add(7, 3) == 10
    assert math_function.add(1) == 3
    assert math_function.add(0) == 2


def test_product():
    assert math_function.product(1) == 2
    assert math_function.product(5, 5) == 25
    assert math_function.product(0) == 0
