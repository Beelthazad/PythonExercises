# Dada una lista devuelva el menor valor positivo de lis. Qué pasa si todos los números de la lista son negativos?
# Implemente una función que generalice cualquier mínimo con condicion.
# Esto es, reciba una lista y una condición sobre los elementos de la lista y devuelva el mínimo de entre los elementos que cumplen
# la condición. Invóquela para conseguir el mínimo de los números pares.

def minLista(lista):
    for i in range(lista):
        if [n for n in lista < 0]:
            print("Todos son negativos")
        else:
            return min([n for n in lista if n<0])

def minCondicion(lista, condicion):
    pos_actual = 0
    lista_aux = list()
    for i in range(len(lista)):
        pos_actual = lista[i]
        if eval("pos_actual" + condicion):
            lista_aux.append(lista[i])
    print(lista_aux)
    return min(lista_aux)

lista = [1,2,4,5,6,10,3,5,2,6,8,3,2,6,10,22,90]
user_condicion = input("Introduce la condición. Puede ser del tipo 'menor que x', 'mayor que x', 'igual a'. // pos_actual_lista + argumentos.")
print(minCondicion(lista, user_condicion))
# eval("pos_actual" + condicion):
