# Defina una f(x) que reciba tres valores y devuelva el menor de los tres. Compruebe si existe alguna función en Python que haga lo mismo.
# En Python 3 tenemos integrada la función min(), pero vamos a hacer el programa a lo bonzo.

def comparar(uno, dos, tres):
    if uno < dos and uno < tres:
        print(uno + " es el menor de nuestros números\n")
    elif dos < uno and dos < tres:
        print(dos + " es el menor de nuestros números\n")
    else:
        print(tres + " es el menor de nuestros números\n")

x = input("Introduce el primer numero")
y = input("Introduce el segundo")
z = input("Introduce  el tercero")

comparar(x,y,z)

print("Utilizamos ahora la función min()")
print(min(x,y,z))