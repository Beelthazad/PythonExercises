# Defina una función que dada una lista devuelva la suma de sus elementos.
def sumaLista(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    return suma




print("Introduce los números de la lista separados con un espacio.")
a = [int(x) for x in input().split()]
print(a)
print("La suma de los elementos de la lista es...", sumaLista(a))
#En Python tenemos la función sum...
print(sum(a))