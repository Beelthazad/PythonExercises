# Defina una función que dado un número entero n devuelva la suma de los n primeros números naturales
def sumaEnteros ():
    suma = 0
    entero = int(input("Introduce un entero..."))
    for i in range(0, entero+1):
        suma = suma + i
        i = i+1
    return suma

print(sumaEnteros())

