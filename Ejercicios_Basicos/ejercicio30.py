# # -*- coding: utf-8 -*-
# DEfina una función usando el enumerate de Python tal que dada una lista devuelv ael valor mínimo y la posición en la que se encuentra
# (en caso de empate la primera vez que aparezca). HAga una segunda versión usando funciones predefinidas de listself.

def min_enumerate(lista):
    for i, x in enumerate(lista):
        if x == min(lista, key=len):
            print i,x
    return 0

def min_enum_listop(lista):
    min_aux = min(lista,key=len)
    print lista.index(min_aux), min_aux
    return 0

a = ['aaaaaaaaaaa','wacho', 'juano', 'libertarios', 'secadmin']
print "Con enumerate...\n"
min_enumerate(a)
print "Con funciones de lista...\n"
min_enum_listop(a)
