from typing import TypedDict

class Entrada(TypedDict):
    operacion: str
    resultado: float

historial: list[Entrada] = []

def registrar(operacion: str, resultado: float) -> None:
    historial.append({"operacion": operacion, "resultado": resultado})

def obtener_historial() -> list[Entrada]:
    return historial

def limpiar_historial() -> None:
    historial.clear()
