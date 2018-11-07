# Definir función factorial.
import math

def factorial(n):
    resultado = 1
    for i in range(n, 1, -1):
        resultado = resultado * i
    return resultado

x = int(input("Introduce un entero...\n"))
print(factorial(x))
print("Existe la función factorial en la libreria math...")
print(math.factorial(x))

