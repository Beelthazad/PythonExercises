# -*- coding: utf-8 -*-
# Implemente una funcion tal que dada una lista de cadenas de caracteres devuelva un conjunto con los caracteres iniciales de las palabras de lista.
# Compare la salida con una lista.

def cadena_conjunto(lista):
    conjunto = set()
    for i in range(len(lista)):
        conjunto.add(lista[i][0])

    return conjunto

a = ['amigo', 'juanjo', 'josefino', 'lopetegui']
print cadena_conjunto(a)
