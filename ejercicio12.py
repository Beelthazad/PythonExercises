# Function dados x, n calcule x^n.
def elevadoa(base,exponente):
    resultado = base
    for i in range(1,exponente):
        resultado = resultado * base
    return resultado

x = int(input("Introduce el entero base...\n"))
y = int(input("Introduce el entero exponente...\n"))
print(elevadoa(x,y))

print("En Python podemos usar el operador '**' para potencias...")
print(x, "**",y, " = ",x**y)