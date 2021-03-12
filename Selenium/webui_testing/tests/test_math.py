import pytest


def test_addition():
    assert 1+1 == 2


def test_subtraction():
    subtraction = 1-1
    assert subtraction == 0


@pytest.mark.parametrize(
    "a,b,expected",
    [(0, 5, 0), (1, 5, 5), (2, 5, 10), (3, 5, 15),
     (4, 5, 20), (5, 5, 25), (-3, 5, -15)]
)
def test_multiplication(a,b,expected):
    assert a*b == expected

"""
pytest treats unhandled exceptions as test failures. 
In fact, the assert statement simply throws an exception to register a failure. 
What if we want to verify that an exception is correctly raised? 
Use pytest.raises with the desired exception type, like this:
"""
def test_divide_by_zero():
  with pytest.raises(ZeroDivisionError):
    1 / 0