# Defina una función que dado un natural n devuelva una lista con las posiciones {i,j} de una matriz cuadrada de orden n empiezando por (0,0).
# Idem para los elementos de la diagonal. ídem para los elementos de la matriz triangular inferior.
# Que tendríamos que cambiar para que empezara por la (1,1)
# Podemos hacerlo con NUMPY, lo cual sería muy sencillo...

def matriz_orden(orden):
    matriz = [[0 for x in range(orden)] for y in range(orden)]
    return matriz

def posiciones(matriz, orden):
    for i in range(orden):
        for j in range(orden):
            print("matriz[", i,"][",j,"] = ", matriz[i][j])


def diagonal(matriz, orden):
    for i,j in zip(range(orden), range(orden)):
            print("matriz[", i, "][", j, "] = ", matriz[i][j])

def triangular_inferior(matriz,orden):
    for i in range(orden):
        for j in range(orden):
            if i >= j:
                print("matriz[", i, "][", j, "] = ", matriz[i][j])


n = int(input("Introduce el orden de la matriz a crear..."))
matriz_op =matriz_orden(n)
print(matriz_op)
print("Lista de posiciones...\n")
posiciones(matriz_op, n)
print("Diagonal\n")
diagonal(matriz_op,n)
print("Triangular inferior\n")
triangular_inferior(matriz_op,n)