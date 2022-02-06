"""
Unit Test for math_function
"""
import math_function


def test_add():
    assert math_function.add(7, 3) == 10
    assert math_function.add(1) == 3
    assert math_function.add(0) == 2


def test_product():
    assert math_function.product(1) == 2
    assert math_function.product(5, 5) == 25
    assert math_function.product(0) == 0

def test_add_strings():
    result = math_function.add('Hello', 'World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'heldlo' not in result

def test_product_strings():
    assert math_function.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_function.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
