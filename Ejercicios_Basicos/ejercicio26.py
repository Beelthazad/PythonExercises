# Defina una función que reciba una lista y una función con una condición sobre los elementos de la lista y devuelva
# el número de elementos de la lista que cumplen la condición.
# Para que el usuario introduzca una función lambda:
# f0 = "x**2"
# f = eval("lambda x:" + f0)

def listaCondicion(lista, condicion):
    pos_actual = 0
    for i in range(len(lista)):
        pos_actual = lista[i]
        if eval("pos_actual" + condicion):
            print(lista[i])
    return 0

lista = [1,2,4,5,6,10,3,5,2,6,8,3,2,6,10,22,90]
user_condicion = input("Introduce la condición. Puede ser del tipo 'menor que x', 'mayor que x', 'igual a'. // pos_actual_lista + argumentos.")
listaCondicion(lista, user_condicion)