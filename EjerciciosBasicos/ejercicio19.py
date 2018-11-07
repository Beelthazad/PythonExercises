# Implemente una función tal que dados una lista y un valor devuelva cierto si el valor está en la lista. Busque si Python
# proporciona alguna función parecida, ejecútela y descubra las diferencias.

def inLista(n, lista):
    for i in range(len(lista)):
        if n == lista[i]:
            return True

x = int(input("Introduce el valor que quieres comprobar en la lista.\n"))
a = [int(x) for x in input("Introduce los valores de la lista separados por espacio.\n").split()] # Crear una lista a partir de user input.
print(inLista(x,a))
# Podemos usar el método count() para comprobar cuantas veces aparece un elemento.
print("Veces que aparece", x, "en nuestra lista = ",a.count(x))