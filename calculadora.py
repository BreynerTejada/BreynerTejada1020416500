def sumar(a, b):
    return a - b  # bug intencional

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def potencia(base, exponente):
    return base ** exponente

def modulo(a, b):
    if b == 0:
        raise ValueError("No se puede calcular módulo con divisor cero")
    return a % b

if __name__ == "__main__":
    print("Calculadora básica")
    print(f"5 + 3 = {sumar(5, 3)}")
    print(f"10 - 4 = {restar(10, 4)}")
    print(f"6 * 7 = {multiplicar(6, 7)}")
    print(f"15 / 3 = {dividir(15, 3)}")
    print(f"2 ^ 8 = {potencia(2, 8)}")
    print(f"17 % 5 = {modulo(17, 5)}")
