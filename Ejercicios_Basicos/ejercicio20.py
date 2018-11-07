# Implemente una función tal que dados una lista y un valor x devuelve cierto si todos los elementos de la lista
# son mayores que x

def mayor_q_Lista(numero, lista):
    contador = 0
    for i in range(len(lista)):
        if numero > lista[i]:
            contador += 1

    if contador == len(lista):
        return True
    else:
        return False

x = int(input("Introduce el valor a comprobar...\n"))
a = [int(x) for x in input("Introduce elementos lista separados x espacio.\n").split()]
print(mayor_q_Lista(x,a))