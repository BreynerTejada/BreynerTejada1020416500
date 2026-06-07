import pytest
from calculadora import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(10, 4) == 6
    assert restar(0, 5) == -5

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10

def test_dividir():
    assert dividir(10, 2) == 5.0
    assert dividir(7, 2) == 3.5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)

def test_potencia():
    from calculadora import potencia
    assert potencia(2, 8) == 256
    assert potencia(3, 3) == 27

def test_modulo():
    from calculadora import modulo
    assert modulo(17, 5) == 2
    assert modulo(10, 3) == 1

def test_modulo_por_cero():
    from calculadora import modulo
    with pytest.raises(ValueError):
        modulo(5, 0)
