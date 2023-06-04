import calculator as calc


def test_add():
    assert calc.add(2, 3) == 5


def test_subtract():
    calc.subtract(4, 3) == 1