def esPar(numero):
    if numero%2 != 0:
        return bool(0)
    else:
        return bool(1)


num = int(input("Introduce un numero a comprobar... el resultado es un booleano :p\n"))
print(esPar(num))