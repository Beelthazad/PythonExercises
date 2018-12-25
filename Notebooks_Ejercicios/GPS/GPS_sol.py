# -*- coding: utf-8 -*-
import csv
from datetime import datetime
from math import sin, cos, sqrt, atan2, radians
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

'''
print("\x1b[6;30;42m" ,".", "\x1b[0m" , "\n")
    ** 10/16 **
'''

def lee_puntos(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de puntos

    ENTRADA:
       - fichero: nombre del fichero de datos -> str
    SALIDA:
       - lista de puntos del trayecto -> [(datetime, float, float, float)]

    Cada línea del fichero se corresponde con un punto del recorrido, y se representa
    con una tupla con los siguientes valores:
        - tiempo: momento en el que se realizó el registro
        - latitud: número real con la latitud del punto en grados
        - longitud: número real con la longitud del punto en grados
        - altitud: número real con la altitud del punto en metros

    Para convertir una cadena con el formato HH:MM:SS en un objeto 'time' usaremos
    la siguiente expresión:

        datetime.strptime(tiempo,'%H:%M:%S')
    '''
    parametros = list()
    with open(fichero, encoding='utf-8') as f:
        for linea in f:
            tiempo, latitud, longitud, altitud = linea.split(',')
            datetime.strptime(tiempo, '%H:%M:%S')
            latitud = float(latitud)
            longitud = float(longitud)
            altitud = float(altitud)
            res = tiempo, latitud, longitud, altitud
            parametros.append(res)

    return parametros
    pass

# Test de la función lee_puntos
puntos = lee_puntos('./data/ruta.csv')
print('Longitud de la lista puntos[][]: ',len(puntos))
print("\x1b[6;30;42m" ,"Test función lee_puntos", "\x1b[0m" ,puntos[:5])
print(puntos[1][1])
print('Probando el type() del elemento "tiempo": ',type(puntos[1][0]), '\n')

#--------------------------------------------------------------------
# Funciones de acceso a Puntos
#--------------------------------------------------------------------
def coordenadas_punto(punto):
    ''' Obtiene las coordenadas geográficas de un punto del trayecto

    ENTRADA:
       - punto: punto del trayecto -> (datetime, float, float, float)
    SALIDA:
       - latitud, longitud y altitud del punto -> (float, float, float)
    '''
    return (punto[1],punto[2],punto[3])


def tiempo_punto(punto):
    ''' Obtiene el instante de tiempo correspondiente a un punto del trayecto

    ENTRADA:
       - punto: punto del trayecto -> (datetime, float, float, float)
    SALIDA:
       - instante de tiempo asociado al punto -> datetime
    '''
    return punto[0]

#--------------------------------------------------------------------
# Funciones de acceso a Intervalos
#--------------------------------------------------------------------
def desnivel_intervalo(puntos, i):
    ''' Obtiene el desnivel correspondiente a un intervalo de un trayecto

    ENTRADA:
       - puntos: lista de puntos del trayecto -> [(datetime, float, float, float)]
       - i: número de orden del intervalo -> int
    SALIDA:
       - incremento de altitud en el intervalo -> float
    '''
    return puntos[i+1][3]-puntos[i][3]


def distancia_intervalo(puntos, i):
    ''' Obtiene la distancia recorrida en un intervalo de un trayecto

    ENTRADA:
       - puntos: lista de puntos del trayecto -> [(datetime, float, float, float)]
       - i: número de orden del intervalo -> int
    SALIDA:
       - distancia recorrida en el intervalo -> float
    '''
    return distancia_haversine_3d(coordenadas_punto(puntos[i]),coordenadas_punto(puntos[i+1]))


def tiempo_intervalo(puntos, i):
    ''' Obtiene el tiempo en segundos invertido en un intervalo de un trayecto

    ENTRADA:
       - puntos: lista de puntos del trayecto -> [(datetime, float, float, float)]
       - i: número de orden del intervalo -> int
    SALIDA:
       - tiempo en segundos invertido en el intervalo -> float
    '''
    return (puntos[i+1][0]-puntos[i][0]).seconds/3600


def velocidad_intervalo(puntos, i):
    ''' Obtiene la velocidad correspondiente a un intervalo de un trayecto

    ENTRADA:
       - puntos: lista de puntos del trayecto -> [(datetime, float, float, float)]
       - i: número de orden del intervalo -> int
    SALIDA:
       - velocidad en el intervalo -> float
    '''
    return distancia_intervalo(puntos,i)/tiempo_intervalo(puntos,i)

def filtra_por_tiempo(puntos, inicio, fin):
    ''' Selecciona los puntos que se encuentren entre dos instantes de tiempo

    ENTRADA:
       - puntos: lista de puntos del trayecto -> [(datetime, float, float, float)]
       - inicio: hora de inicio del filtro -> str
       - fin: hora de fin del filtro -> str
    SALIDA:
       - lista de puntos del trayecto -> [(datetime, float, float, float)]

    Toma como entrada una lista de puntos y dos instantes de tiempo en formato
    'HH:MM:SS'. Produce como salida otra lista de puntos en la que solo se incluyen
    aquellos que se han registrado entre ambos instantes de tiempo.
    SOL:
    Vamos a iterar a través de los puntos y comparamos la primera posición de cada
    elemento en nuestra lista con el intervalo de tiempo inicio/fin
    '''
    datetime.strptime(inicio, '%H:%M:%S')
    datetime.strptime(fin, '%H:%M:%S')
    intervalo = list()
    for i in range(len(puntos)):
        if (puntos[i][0] >= inicio) and (puntos[i][0] <= fin):
            intervalo.append(puntos[i])

    return intervalo
    pass

# Test de la función filtra_por_tiempo
print("\x1b[6;30;42m" ,"Test función filtra_por_tiempo.", "\x1b[0m")
primera_parte = filtra_por_tiempo(puntos, '00:00:00', '11:48:00')
print(len(primera_parte))
print(primera_parte[:5], '\n')

print("\x1b[6;30;42m" ,"Test función filtra_por_tiempo, prueba 2.", "\x1b[0m")
segunda_parte = filtra_por_tiempo(puntos, '11:48:01', '23:36:00')
print(len(segunda_parte))
print(segunda_parte[:5], '\n')



def distancia_haversine(coord_a, coord_b):
    ''' Cálculo de la distancia entre dos coordenadas geográficas

    ENTRADA:
       - coord_a: coordenadas del primer punto -> (float, float)
       - coord_b: coordenadas del segundo punto -> (float, float)
    SALIDA:
       - distancia entre ambos puntos -> float

    Recibe como entrada dos coordenadas, cada una de ellas representada mediante una tupla
    (latitud,longitud) y calcula la distancia en kilómetros mediante la fórmula
    del haversine.
    '''
    radio_tierra = 6373.0
    latitud_a, longitud_a = radians(coord_a[0]), radians(coord_a[1])
    latitud_b, longitud_b = radians(coord_b[0]), radians(coord_b[1])
    inc_lat  = latitud_b - latitud_a
    inc_long = longitud_b - longitud_a

    a = sin(inc_lat / 2)**2 + cos(latitud_a) * cos(latitud_b) * sin(inc_long / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return radio_tierra * c

# Test de la función distancia_haversine
print("\x1b[6;30;42m" ,"Test función haversine: ", "\x1b[0m")
sevilla = (37.3828300, -5.9731700)
cadiz = (36.5008762, -6.2684345)
print(distancia_haversine(sevilla, cadiz))



def distancia_haversine_3d(coord_a, coord_b):
    ''' Cálculo de la distancia entre dos coordenadas geográficas considerando altitud

    ENTRADA:
       - coord_a: coordenadas del primer punto -> (float, float, float)
       - coord_b: coordenadas del segundo punto -> (float, float, float)
    SALIDA:
       - distancia entre ambos puntos -> float

    Recibe como entrada dos coordenadas, cada una de ellas representada mediante una tupla
    (latitud,longitud,altitud) y calcula la distancia en kilómetros de la siguiente forma:
       - Calcular la diferencia de altitud de los dos puntos (en kilómetros)
       - Calcular la distancia_haversine de los dos puntos
       - Usar ambos valores y el teorema de Pitágoras para calcular la distancia haversine_3d
    '''
    dif_altitud = coord_a[2] - coord_b[2]
    dist_2d = distancia_haversine(coord_a[:2], coord_b[:2])
    dist_3d = sqrt(dist_2d**2 + (dif_altitud)**2)
    return dist_3d
    pass

# latitud, longitud, altitud
print("\x1b[6;30;42m" ,"Test función haversine_3d: ", "\x1b[0m")
# Test de la función distancia_haversine_3d
coord_1 = (36.74991256557405,-5.147951105609536,712.2000122070312)
coord_2 = (36.75008556805551,-5.148005923256278,712.7999877929688)
print(distancia_haversine(coord_1, coord_2))      # Funciona bien con tuplas de 3 valores gracias al tipado dinámico de Python
print(distancia_haversine_3d(coord_1, coord_2))

def distancia_trayecto(puntos):
    ''' Cálculo de la distancia de un trayecto

    ENTRADA:
       - puntos: lista de puntos del trayecto -> [(datetime, float, float, float)]
    SALIDA:
       - distancia total del trayecto -> float

    Recibe como entrada un trayecto representado mediante una lista de tuplas
    (tiempo,latitud,longitud,altitud) y calcula la distancia total en kilómetros.
    Se seguirán los siguientes pasos:
       - Calcular a partir de la lista puntos una lista de coordenadas
         (latitud,longitud,altitud)
       - Calcular una lista de intervalos cada uno de ellos representado mediante
         una tupla de dos coordenadas (inicio_intervalo, fin_intervalo)
       - Usar la función distancia_haversine_3d para calcular la distancia total
         del trayecto
    '''
    coordenadas = list()
    intervalos = list()
    for i in range(len(puntos)):
        coordenadas.append(coordenadas_punto(puntos[i]))

    for z in range(len(coordenadas)):
        aux = (coordenadas[z][0:], coordenadas[z+1][0:])
        intervalos.append(aux)

    for _ in range(len(aux)):
        sum = sum + distancia_haversine_3d(aux[_])

    return sum
    pass



# Test de la función distancia_trayecto
print("\x1b[6;30;42m" ,"Test función distancia_trayecto: ", "\x1b[0m")
print(distancia_trayecto(puntos))
print(distancia_trayecto(primera_parte))
print(distancia_trayecto(segunda_parte))



def velocidad_trayecto(puntos):
    ''' Cálculo de la velocidad en un trayecto

    ENTRADA:
       - puntos: lista de puntos del trayecto -> [(datetime, float, float, float)]
    SALIDA:
       - velocidad media durante el trayecto -> float

    Recibe como entrada un trayecto representado mediante una lista de tuplas
    (tiempo,latitud,longitud,altitud) y calcula la velocidad media en km/h
    en dicho trayecto. Para calcular la duración, en horas, de un periodo de
    tiempo comprendido entre los momentos inicio y fin se puede usar la
    siguiente expresión:
          duracion = (fin - inicio).seconds/3600
    '''
    pass

# Test de la función velocidad_trayecto
print("\x1b[6;30;42m" ,"Test función velocidad_trayecto: ", "\x1b[0m")
print(velocidad_trayecto(puntos))
print(velocidad_trayecto(primera_parte))
print(velocidad_trayecto(segunda_parte))



def desnivel_acumulado(puntos):
    ''' Cálculo del desnivel acumulado (de subida y bajada) de un trayecto

    ENTRADA:
       - puntos: lista de puntos del trayecto -> [(datetime, float, float, float)]
    SALIDA:
       - desniveles acumulados de subida y bajada -> (float, float)

    Recibe como entrada un trayecto representado mediante una lista de tuplas
    (tiempo,latitud,longitud,altitud) y calcula una tupla con los desniveles
    acumulados de subida y bajada. Se pueden seguir los siguientes pasos:
       - Calcular a partir de la lista puntos una lista de altitudes
       - Calcular una lista de desniveles a partir de la lista de altitudes
       - Calcular una lista de desniveles de subida a partir de la lista de desniveles
       - Calcular una lista de desniveles de bajada a partir de la lista de desniveles
    '''
    pass

# Test de la función desnivel_acumulado
print("\x1b[6;30;42m" ,"Test función desnivel_acumulado: ", "\x1b[0m")
print(desnivel_acumulado(puntos))
print(desnivel_acumulado(primera_parte))
print(desnivel_acumulado(segunda_parte))

def mostrar_perfil(puntos):
    ''' Traza el perfil de un trayecto

    ENTRADA:
       - puntos: lista de puntos del trayecto -> [(datetime, float, float, float)]
    SALIDA EN PANTALLA:
       - gráfica con el perfil del trayecto

    Toma como entrada un trayecto definido por una lista de puntos y produce como salida
    el perfil del trayecto. En el eje X se muestran los kilómetros y en el eje Y las alturas
    de los distintos puntos (en metros). Para generar la gráfica se usarán las siguientes
    instrucciones:
        kilometros = [distancia_total*i/len(altitudes) for i in range(len(altitudes))]
        plt.plot(kilometros,altitudes)
        plt.show()

    Donde las variables distancia y altitudes significan, respectivamente:
        - distancia_total: distancia total del trayecto
        - altitudes: lista con las altitudes de cada punto del trayecto
    '''
    pass

# Test de la función mostrar_perfil
print("\x1b[6;30;42m" ,"Test función mostrar_perfil: ", "\x1b[0m")
mostrar_perfil(puntos)

def mostrar_velocidad_por_intervalo(puntos):
    ''' Traza la evolución de la velocidad a lo largo del tiempo

    ENTRADA:
       - puntos: lista de puntos del trayecto -> [(datetime, float, float, float)]
    SALIDA EN PANTALLA:
       - gráfica con las velocidades por intervalo

    Toma como entrada un trayecto definido por una lista de puntos y produce como salida
    una gráfica con la velocidad en cada punto del trayecto. En el eje X se muestran los
    kilómetros recorridos y en el eje Y las velocidades (en km/h). Para generar la gráfica
    se usarán las siguientes instrucciones:
        kilometros = [distancia_total*i/len(velocidades) for i in range(len(velocidades))]
        plt.plot(kilometros, velocidades)
        plt.show()

    Las variables que hay que calcular previamente son:
        - distancia_total: distancia total del trayecto
        - distancias: lista con las distancias parciales recorridas en cada intervalo del trayecto.
          La distacia parcial se calcula mediante la distancia entre los puntos de inicio y fin
          de cada intervalo.
        - tiempos: lista con el tiempo invertido en cada intervalo del trayecto
        - velocidades: lista con las velocidades en cada intervalo del trayecto. No se calcularán
          velocidades para trayectos con tiempo==0 (puede que haya alguno por errores de medida)
    '''
    pass

# Test de la función mostrar_velocidad_por_intervalo
print("\x1b[6;30;42m" ,"Test función mostrar_velocidad_por_intervalo: ", "\x1b[0m")
mostrar_velocidad_por_intervalo(puntos)

def mostrar_ruta_en_mapa(puntos, mapa, lado=9, lat_base=-36.665, long_base=5.282, escala=0.23):
    ''' Traza un trayecto sobre un mapa

    ENTRADA:
       - puntos: lista de puntos del trayecto -> [(datetime, float, float, float)]
       - mapa: nombre del archivo que contiene la imagen del mapa -> str
       - lado: tamaño del cuadrado en el que se encaja la gráfica -> float
       - lat_base: latitud correspondiente a la esquina inferior izquierda de la gráfica -> float
       - long_base: latitud correspondiente a la esquina inferior izquierda de la gráfica -> float
       - escala: escalado de la ruta para acomodarse al tamaño del mapa -> float
    SALIDA EN PANTALLA:
       - gráfica con el trayecto trazado sobre el mapa

    Toma como entrada un trayecto definido por una lista de puntos y el nombre de un archivo
    PNG que contenga un mapa. El resto de parámetros sirven para configurar el tamaño de la imagen,
    y el desplazamiento y escalado de la ruta. Los valores por defecto de estos parámetros están
    ajustados para el mapa del ejemplo.

    Para generar la gráfica se usarán las siguientes instrucciones:
        img = mpimg.imread(mapa)
        plt.figure(figsize=(lado, lado))
        plt.imshow(img, zorder=0, extent=[0, lado, 0, lado])
        xs = [(x + lat_base) * lado  / 0.23 for x, _ in lats_longs]
        ys = [(y + long_base) * lado / 0.23 for _, y in lats_longs]
        plt.scatter(ys, xs, zorder=1, s=10, color='blue')
        plt.axis('off')
        plt.show()

    Solo es necesario calcular la siguiente variable:
        - lats_longs: lista de tuplas (latitud, longitud) correspondientes a todos los puntos
          del trayecto.
    '''
    pass

# Test de la función mostrar_ruta_en_mapa
print("\x1b[6;30;42m" ,"Test función mostrar_ruta_en_mapa: ", "\x1b[0m")
mostrar_ruta_en_mapa(puntos, './img/mapa_ronda.png')
