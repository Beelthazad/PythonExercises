# Función para comprobar si un número es primo.
# Un número es primo si solo tiene, exactamente, dos divisores positivos - 1 y el mismo entero. Si un número entero no es primo, lo llamaremos compuesto.

def esPrimo(entero):
    divisores = 0

    if entero == 1:
        print("1 no es un número primo!!!!")
        return 0

    for i in range(1,entero+1):
        if entero%i == 0:
            divisores = divisores+1

    if divisores == 2:
        print(entero, "es un número PRIMO.\n")
    else:
        print(entero, "es un nº COMPUESTO.")

x = int(input("Introduce un número entero...\n"))
esPrimo(x)
