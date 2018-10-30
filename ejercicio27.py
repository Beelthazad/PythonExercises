# Defina una función que reciba una lista de cadenas de caracteres y un carater x y devuelva el n. de palabras de la lista
# que empiezan por x. ----------- MÉTODO STARTSWITH
# Y si quisieramos contar las que terminan en un determinado carácter? ----- METODO ENDSWITH
# O las de longitud mayor que un valor?

def palabrasLista(caracter, lista):
    contador_empiezan = 0
    contador_terminan = 0
    for i in range(len(lista)):
        if lista[i].startswith(caracter):
            contador_empiezan += 1
        if lista[i].endswith(caracter):
            contador_terminan += 1

    print("Empiezan con ", caracter, " = ", contador_empiezan, " palabras.\n")
    print("Terminan con", caracter, " = ", contador_terminan, " palabras.\n")
    return contador_terminan, contador_empiezan

def longitud_check(longitud, lista):
    contador_longitud = 0
    for i in range(len(lista)):
        if len(lista[i]) > longitud:
            contador_longitud += 1

    print("Son de más longitud que ", longitud, " = ", contador_longitud, " palabras.\n")
    return 0

lista_palabras = ["juan","paranoya", "pentesting", "almadraba", "casa", "almendra"]
a = input("Introduce un caracter")
b = int(input("Introduce una longitud a comprobar..."))
palabrasLista(a,lista_palabras)
longitud_check(b, lista_palabras)