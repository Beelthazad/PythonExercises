#Defina una funcion tal que dada una lista de enteros devuelva la suma de los pares
def sumaPares(lista):
    suma = 0
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            suma = suma + lista[i]
    return suma

print("Introduce los números de la lista separados con un espacio.")
a = [int(x) for x in input().split()]
print(sumaPares(a))