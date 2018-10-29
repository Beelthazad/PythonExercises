# Defina una función que recibe n y m enteros y muestre en consola los valores entre n y m-1.
# Con los mismos argumentos calcule la suma entre n y m-1. ¿Y entre n y m?

def entreEnteros(n,m):
    for i in range(n, m):
        print(i)
        i = i+1

    return 0

x = int(input("Introduce n...\n"))
y = int(input("Introduce m...\n"))
print("Las sumas pedidas serán... ")
print(x+(y-1))
print(x+y)
print("Los números entre", x, "y", y, "serán...")
entreEnteros(x,y)
