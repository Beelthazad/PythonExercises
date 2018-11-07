# Defina una función tal que dado un número entero n devuelva una lista con los números del 1 al n. Idem pero sólo los pares.
def listaNum(entero):
    lista = list()
    listaPares = list()
    for i in range(1, entero+1):
        lista.append(i)
        if i%2 == 0:
            listaPares.append(i)

    print(lista)
    print(listaPares)


x = int(input("Introduce un entero...\n"))
listaNum(x)
