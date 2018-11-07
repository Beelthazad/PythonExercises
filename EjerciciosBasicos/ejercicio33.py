# -*- coding: utf-8 -*-
# Implemente una función tal que dada una lista de palabras devuelva un conjunto con todos los caracteres de esas palabras.
# Puedes hacer varias versiones, mediante un recorrido de las palabras de la lista y dentro recorrer los caracteres...
# O por comprensión con un doble for o bien usando la funcion aplana que se ha viesto en un ejercicio anterior

def lista_conjunto(lista):
    conjunto = set()
    for i in range(len(lista)):
        for x in range(len(lista[i])):
            print len(lista[i])
            conjunto.add(lista[i][x])

    return conjunto

a = ['amigo', 'juanjo', 'josefino', 'lopetegui']
print lista_conjunto(a)
