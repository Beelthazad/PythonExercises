## -*- coding: utf-8 -*-
# Implemente una función tal que dada una lista de cadenas de caracteres y un carácter x devuelva las posiciones que ocupan en la lista las palabras
# que terminan en x.

def pos_lista_caracter(lista, caracter):
    for x,y in enumerate(lista):
        if lista[x].endswith(caracter):
            print x, y
    return 0

a = ['vuelox', 'amigo', 'programacionx', 'laberasiop', 'asdasdx']
b = 'x'
pos_lista_caracter(a,b)
