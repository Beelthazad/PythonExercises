# Defina una función tal que dado un número n devuelva una lista con los cuadrados de los números pares menores de n.
def listaCuadrados(entero):
    listaResult = list()
    for i in range(1,entero):
        if esPar(i) == True:
            listaResult.append(i**2)
    return listaResult

def esPar(entero):
    if entero%2 == 0:
        return True
    else:
        return False

x = int(input("Introduce un entero...\n"))
print(listaCuadrados(x))
