def sumar(
a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def main():
    print("================================")
    print("   PROYECTO DOCKER - PYTHON")
    print("================================")
    print("Suma: 10 + 5 =", sumar(10, 5))
    print("Resta: 10 - 5 =", restar(10, 5))
    print("Multiplicación: 10 * 5 =", multiplicar(10, 5))
    print("División: 10 / 5 =", dividir(10, 5))
    print("================================")
    print("Programa ejecutado correctamente")


if __name__ == "__main__":
    main()
