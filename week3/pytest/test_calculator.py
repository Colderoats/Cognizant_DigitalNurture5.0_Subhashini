import pytest

def test_add(calc):
    assert calc.add(5, 3) == 8

def test_add_negative(calc):
    assert calc.add(-5, -5) == -10

def test_subtract(calc):
    assert calc.subtract(10, 4) == 6

def test_subtract_negative(calc):
    assert calc.subtract(-5, -3) == -2

def test_multiply(calc):
    assert calc.multiply(4, 5) == 20

def test_multiply_zero(calc):
    assert calc.multiply(5, 0) == 0

def test_divide(calc):
    assert calc.divide(20, 4) == 5

def test_divide_decimal(calc):
    assert calc.divide(5, 2) == 2.5

def test_modulus(calc):
    assert calc.modulus(10, 3) == 1

def test_power(calc):
    assert calc.power(2, 4) == 16

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)