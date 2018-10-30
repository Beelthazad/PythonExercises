# Investigue como convertir una cadena de caracteres en una lista de caracteres.
# Usando esa conversión implemente una función que reciba una lista de cadenas de caracteres y devuelva una lista formada por listas de caracteres.
# ['una','dos','tres] ---- ['u','n','a'], ...

def listaCadenas(lista):
    lista_caracteres = list()
    for i in range(len(lista)):
        a = [x for x in lista[i]]   # Para cada caracter de la posición iterada de lista[]
        lista_caracteres.append(a)  # Introducirlo en el output
    return lista_caracteres


lista_cadenas = ['una', 'dos', 'tres']
print(listaCadenas(lista_cadenas))