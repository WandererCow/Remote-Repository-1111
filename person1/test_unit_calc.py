# tests/test_unit_calc.py
from calc import add


def test_add_positive():
    assert add(3, 3) == 6


def test_add_negative():
    assert add(-1, -1) == -2


def test_add_something():
    assert add(15, -7) == 8
