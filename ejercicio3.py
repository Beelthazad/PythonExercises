import math

def areaCirculo(radio):
    area = radio**2 * math.pi
    longitud = 2 * math.pi * radio
    return area, longitud

r = int(input("Introduce radio...\n"))
print(areaCirculo(r))
