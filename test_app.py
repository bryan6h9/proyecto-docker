import pytest
from app import sumar, restar, multiplicar, dividir


def test_sumar():
    assert sumar(5, 5) == 10


def test_restar():
    assert restar(10, 5) == 5


def test_multiplicar():
    assert multiplicar(4, 5) == 20


def test_dividir():
    assert dividir(10, 2) == 5


def test_division_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

