import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2.0, 3.0) == 5.0
    assert calc.add(-1.0, 1.0) == 0.0

def test_substract(calc):
    assert calc.substract(5.0, 3.0) == 2.0
    assert calc.substract(1.0, 5.0) == -4.0

def test_multiply(calc):
    assert calc.multiply(3.0, 3.0) == 9.0
    assert calc.substract(-2.0, 4.0) == -8.0

def test_divide(calc):
    assert calc.substract(10.0, 2.0) == 5.0

def test_divide_by_zero(calc):
    #Тест ожидает ошибку ValueError при делении на ноль
    with pytest.raises(ValueError):
        calc.divide(5.0, 0.0)