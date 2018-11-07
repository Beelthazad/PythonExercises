# coding=utf-8
# Dada una lista "lis" de cadenas de caracteres construya una lista con todas las tuplas formadas por la longitud las palabras de lis. HAga un sort de esa listaself.
# Usando la lista de tuplas anterior construya una función que devuelva las cadenas de mínima y máxima longitud de "lis" en una tuplaself.
# PARA CREAR UNA TUPLA DE 1 SOLO VALOR ------> (50,) CON UNA COMA!!

def tuplas_len_lista(lista):
    lista_aux = list()
    tupla_aux = 0
    for i in range(len(lista)):
            tupla_aux = (lista[i],len(lista[i]))
            print(tupla_aux)
            lista_aux.append(tupla_aux)
    return lista_aux

def tupla_min_max(lista):
    a = (min(lista, key=len),max(lista,key=len))
    return a

a = ['amigo', 'juanymedio', 'cabesa', 'pisha', 'gaditangeeks', 'oo']
res = tuplas_len_lista(a)
print("La lista resultado, ordenada, sera...\n", res.sort())
print(tupla_min_max(a))
