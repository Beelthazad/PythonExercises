#Defina una función que reciba dos enteros con los goles del equipo local y visitante y devuelva el signo de la quiniela.

def signo(local, visitante):
    if local > visitante:
        print("1\n")
    elif local == visitante:
        print("X\n")
    else:
        print("2\n")

x = input("Introduce los goles del equipo local\n")
y = input("Introduce los goles del equipo visitante\n")
signo(x,y)