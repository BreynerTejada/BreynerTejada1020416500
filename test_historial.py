import pytest
from historial import registrar, obtener_historial, limpiar_historial

def setup_function():
    limpiar_historial()

def test_registrar_operacion():
    registrar("5 + 3", 8)
    assert len(obtener_historial()) == 1
    assert obtener_historial()[0] == {"operacion": "5 + 3", "resultado": 8}

def test_multiples_registros():
    registrar("10 - 4", 6)
    registrar("6 * 7", 42)
    assert len(obtener_historial()) == 2

def test_limpiar_historial():
    registrar("15 / 3", 5.0)
    limpiar_historial()
    assert len(obtener_historial()) == 0
