# Función que reciba un entero e imprima en la consola los números del 1 a n y del 0 a n - 1
# Haremos funciones con for y con while

def imprimirUno(num):
    for i in range(1, num+1):
        print(i)
    for z in range(0, num):
        print(z)

def imprimirDos(num):
    a = 0
    b = 1
    while b <= num:
        print(b)
        b+=1
    while a <= num - 1:
        print(a)
        a+=1

x = int(input("Introduce num\n"))
print("Mediante for\n")
imprimirUno(x)
print("Mediante while")
imprimirDos(x)