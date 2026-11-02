# tests/test_integration.py
from person1.calc import add


def test_calc_chain():
    result = add(add(1, 2), add(3, 4))
    assert result == 10