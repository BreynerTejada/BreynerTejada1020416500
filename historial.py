historial = []

def registrar(operacion, resultado):
    historial.append({"operacion": operacion, "resultado": resultado})

def obtener_historial():
    return historial

def limpiar_historial():
    historial.clear()
