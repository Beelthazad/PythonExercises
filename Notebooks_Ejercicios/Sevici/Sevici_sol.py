# -*- coding: utf-8 -*-
import csv
from math import sqrt
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
'''
En este ejercicio vamos a trabajar con la red de estaciones del servicio de alquiler de bicicletas de Sevilla, Sevici. Para ello disponemos de los datos de las estaciones, obtenidos de https://citybik.es/.

En primer lugar leeremos los datos de las estaciones desde un fichero CSV. Realizaremos algunas operaciones con los datos, como obtener las estaciones con bicicletas libres o las estaciones más próximas a nuestra ubicación. Finalmente, dibujaremos sobre el mapa las estaciones, distinguiendo entre las que tienen bicicletas disponibles y las que no las tienen.

Las funciones que vamos a desarrollar son las siguientes:

    lee_estaciones: lee los datos de las estaciones desde un fichero csv
    estaciones_bicis_libres: crea una lista con las estaciones que tienen bicicletas libres, ordenada por el número de bicis libres
    calcula_distancia: calcular la distancia a una estación desde un punto dado
    estaciones_cercanas: crea una lista con las estaciones con bicis libres más cercanas a un punto dado, ordenadas de la más cercana a la más lejana
    ubicacion_estaciones: crear una lista con las coordenadas de todas las estaciones
    ubicacion_estaciones_libres: crear una lista con las coordenadas de todas las estaciones que tienen bicicletas lib

DATOS DISPONIBLES
-----------------
Nombre de la estación
Número total de bornetas de la estación
Número de bornetas vacías
Número de bicicletas disponibles
Latitud
Longitud -->
    name,slots,empty_slots,free_bikes,latitude,longitude
    149_CALLE ARROYO,20,11,9,37.397829929383,-5.97567172039552
    257_TORRES ALBARRACIN,20,16,4,37.38376948792722,-5.908921914235877
    243_GLORIETA DEL PRIMERO DE MAYO,15,6,9,37.380439481169994,-5.953481197462845
    109_AVENIDA SAN FRANCISCO JAVIER,15,1,14,37.37988413609134,-5.974382770011586
    073_PLAZA SAN AGUSTIN,15,10,4,37.38951386231434,-5.984362789545622

    ** 0/6 **

'''
def lee_estaciones(fichero):
    ''' Lee el fichero de datos y devuelve una lista de estaciones

    ENTRADA:
       - fichero: nombre del fichero CSV -> str
    SALIDA:
       - lista de estaciones -> [(str, int, int, int, float, float)]

    Cada estación se representa con una tupla con los siguientes valores:
    - Nombre de la estación
    - Número total de bornetas
    - Número de bornetas vacías
    - Número de bicicletas disponibles
    - Latitud
    - Longitud
    Usaremos el módulo csv de la librería estándar de Python para leer el
    fichero de entrada.
    Hay que saltar la línea de encabezado del fichero y comenzar a leer los datos
    a partir de la segunda línea.
    Hay que realizar un pequeño procesamiento con los datos numéricos. Hay que
    pasar del formato cadena (que es lo que se interpreta al leer el csv) a un
    valor numérico (para poder aplicar operaciones matemáticas si fuese necesario).
    '''
    pass

# Test de la función lee_estaciones
estaciones_sevici = lee_estaciones('./data/estaciones.csv')
print(estaciones_sevici[:5])

:

def estaciones_bicis_libres(estaciones, k=5):
    ''' Estaciones que tienen bicicletas libres

    ENTRADA:
       - estaciones: lista de estaciones disponibles -> [(str, int, int, int, float, float)]
       - k: número mínimo requerido de bicicletas -> int
    SALIDA:
       - lista de estaciones seleccionadas -> [(int, str)]

    Toma como entrada una lista de estaciones y un número k.
    Crea una lista formada por tuplas (número de bicicletas libres, nombre)
    de las estaciones que tienen al menos k bicicletas libres. La lista
    estará ordenada por el número de bicicletas libres.
    '''
    pass

# Test de la función estaciones_bicis_libres
libres1 = estaciones_bicis_libres(estaciones_sevici)
print("Hay", len(libres1), "estaciones con 5 o más bicis libres:", libres1[:5])
libres2 = estaciones_bicis_libres(estaciones_sevici, 10)
print("Hay", len(libres2), "estaciones con 10 o más bicis libres:", libres2[:5])
libres3 = estaciones_bicis_libres(estaciones_sevici, 1)
print("Hay", len(libres3), "estaciones con al menos una bici libre:", libres3[:5])

def calcula_distancia(x1, y1, x2, y2, fb):
    ''' Distancia entre un punto y una estación

    ENTRADA:
       - x1: latitud del primer punto -> float
       - y1: longitud del primer punto -> float
       - x2: latitud del segundo punto -> float
       - y2: longitud del segundo punto -> float
       - fb: número de bicicletas libres -> int
    SALIDA:
       - distancia entre un punto y una estación -> float

    Toma como entrada la latitud y longitud de un punto, la longitud y
    latitud de una estación y el número de bicicletas libres de la estación.
    Calcula la distancia entre el punto y la estación aplicando la fórmula

        distancia = sqrt((x2-x1)**2 + (y2-y1)**2) * (1 - fb/100)
    '''
    pass



def estaciones_cercanas(estaciones, latitud, longitud, k=5):
    ''' Estaciones cercanas a un punto dado

    ENTRADA:
       - estaciones: lista de estaciones disponibles -> [(str, int, int, int, float, float)]
       - latitud: latitud del punto -> float
       - longitud: longitud del punto -> float
       - k: número de estaciones cercanas a calcular -> int
    SALIDA:
       - distancia, nombre y bicicletas libres de las estaciones seleccionadas -> [(float, str, int)]

    Toma como entrada una lista de estaciones, la latitud y longitud de un punto y
    un valor k.
    Crea una lista formada por tuplas (distancia, nombre de estación, bicicletas libres)
    con las k estaciones con bicicletas libres más cercanas al punto dado, ordenada por
    su distancia al punto.
    '''
    pass

# Test de la función
cerca_de_mi = estaciones_cercanas(estaciones_sevici, 37.357659, -5.9863)
print(cerca_de_mi)

def dibuja_mapa():
    ancho = 9
    aspect_ratio = 1.09
    img = mpimg.imread('./img/mapa.png')
    plt.figure(figsize=(ancho, ancho * aspect_ratio))
    plt.imshow(img, zorder=0, extent=[0, ancho, 0, ancho * aspect_ratio])
    plt.axis('off')

def dibuja_estaciones(coordenadas, color="red"):
    ancho = 9
    aspect_ratio = 1.09
    xs = [(x - 37.31) * ancho * aspect_ratio / 0.13 for x, _ in coordenadas]
    ys = [(y + 6.04) * ancho / 0.15 for _, y in coordenadas]
    plt.scatter(ys, xs, zorder=1, s=10, color=color)

def ubicacion_estaciones(estaciones):
    ''' Coordenadas de todas las estaciones

    ENTRADA:
       - estaciones: lista de estaciones disponibles -> [(str, int, int, int, float, float)]
    SALIDA:
       - latitudes y longitudes de las estaciones -> [(float, float)]

    Recibe un lista de estaciones.
    Crea una lista formada por tuplas (latitud, longitud) con todas las estaciones.
    '''
    pass

# Test de la función ubicacion_estaciones
coordenadas = ubicacion_estaciones(estaciones_sevici)
dibuja_mapa()
dibuja_estaciones(coordenadas)
plt.show()

def ubicacion_estaciones_libres(estaciones, k=5):
    ''' Coordenadas de las estaciones con bicicletas libres

    ENTRADA:
       - estaciones: lista de estaciones disponibles -> [(str, int, int, int, float, float)]
       - k: número mínimo requerido de bicicletas libres -> int
    SALIDA:
       - latitudes y longitudes de las estaciones seleccionadas -> [(float, float)]

    Recibe una lista de estaciones y un valor k.
    Crea una lista formada por tuplas (latitud, longitud) con todas las estaciones
    que tienen más de k estaciones libres.
    '''
    pass

# Test de la función ubicacion_estaciones_libres
coordenadas_todas = ubicacion_estaciones(estaciones_sevici)
coordenadas_libres = ubicacion_estaciones_libres(estaciones_sevici)
dibuja_mapa()
dibuja_estaciones(coordenadas_todas)
dibuja_estaciones(coordenadas_libres, color="green")
plt.show()
