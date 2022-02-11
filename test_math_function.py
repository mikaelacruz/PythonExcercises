"""
Unit Test for math_function
"""
import math_function
import pytest


@pytest.mark.parametrize('first, second, result',
                         [
                             (7, 3, 10),
                             ('Hello', ' World', 'Hello World'),
                             (10.5, 25.5, 36)
                         ]
                         )
def test_add(first, second, result):
    assert math_function.add(first, second) == result


"""
def test_product():
    assert math_function.product(1) == 2
    assert math_function.product(5, 5) == 25
    assert math_function.product(0) == 0

def test_add_strings():
    result = math_function.add('Hello', 'World')
    assert type(result) is str
    assert 'heldlo' not in result

def test_product_strings():
    assert math_function.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_function.product('Hello ')
    assert type(result) is str
    assert 'Hello' in result
"""
