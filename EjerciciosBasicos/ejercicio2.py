# Devuelven suma y producto de dos args.
x = int(input("Introduce el primer número...\n"))
y = int(input("Introduce el segundo número...\n"))

def suma(num1, num2):
    return num1 + num2

def producto(num1, num2):
    return num1 * num2

print("Resultado de las funciones\n--")
print(suma(x,y))
print(producto(x,y))

