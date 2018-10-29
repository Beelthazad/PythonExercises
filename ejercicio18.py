# Implemente una función tal que dados dos números enteros n y m, devuelva una lista de n elementos aleatorios en el intervalo -m,m. Investigue una
# función que genere valores aleatorios enteros.

# VAMOS A USAR LA FUNCIÓN RANDINT DE LA LIBRERÍA RANDOM
import random

def listaAleatoria(n,m):
    lista = list()
    for i in range(1, n+1):
        lista.append(random.randint(-m,m))
    return lista

x = int(input("Introduce el número de elementos que tendrá la lista...\n"))
y = int(input("Introduce m - que nos dará el intervalo de números aleatorios que estarán en la lista...\n"))
print(listaAleatoria(x,y))