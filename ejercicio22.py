# Implemente una función que devuelva el mayor de los elementos de una lista. Idem con el menor. Busque si Python proporciona funciones similares.

def menorLista(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor



def mayorLista(lista):
    mayor = lista[0]
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor


a = [int(x) for x in input("Introduce los valores de la lista separados por espacio.\n").split()] # Crear una lista a partir de user input.
print(menorLista(a))
print(mayorLista(a))

# En Python tenemos las funciones max() y min()