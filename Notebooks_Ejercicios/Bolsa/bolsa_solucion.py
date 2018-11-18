# -*- coding: utf-8 -*-
# COLORING: print("\x1b[6;30;42m" , "LOREM IPSUM", "\x1b[0m")
from math import sqrt
from matplotlib import pyplot as plt
import statistics
import csv

'''
    FUNCIONES COMPLETADAS: 0/8
'''

def lee_precios_empresa(empresa, ruta='./data/', extension='.MC.txt'):
    ''' Lee el fichero de una empresa y devuelve una lista de precios

    ENTRADA:
       - empresa: nombre de la empresa de la que se quieren leer los datos -> str
       - ruta: carpeta donde se encuentra el fichero -> str
       - extension: con la que se completa el nombre del fichero -> str
    SALIDA:
       - lista de precios -> [float]

    En el fichero de entrada se encuentran las cotizaciones de una
    empresa durante un año (un número por línea correspondiente al valor de
    cierre de un día).
    La función toma como entrada el nombre de la empresa, la ruta donde se
    encuentra el fichero y la extensión que hay que añadir al nombre de la
    empresa para componer el nombre del fichero.
    Produce como salida una lista de números reales. Es importante tener en
    cuenta que hay que transformar lo que se lee del fichero (cadenas
    de caracteres) en valores numéricos.
    '''
    lista_precios = list()
    with open(''.join([ruta, empresa, extension]), encoding='utf-8') as f:
        lector = csv.reader(f) # Así evitamos trabajar de +.
        lista_precios = [precio for precio in lector] # Esto convierte todos los campos sin '' a tipo float.
    return lista_precios
    pass

# Test de la función lee_precios_empresa
bbva_precios = lee_precios_empresa('BBVA')
print(bbva_precios[:20])
print(type(bbva_precios[1]))

def lee_precios_empresas(empresas, ruta='./data/', extension='.MC.txt'):
    ''' Carga los ficheros de precios de varias empresas en un diccionario

    ENTRADA:
       - empresas: nombres de la empresas de las que se quieren leer los datos -> [str]
       - ruta: carpeta donde se encuentran los ficheros -> str
       - extension: con la que se completan los nombres de los ficheros -> str
    SALIDA:
       - diccionario de precios -> {str: [float]}

    Recibe una lista de nombres de empresas, la ruta donde se encuentran
    los ficheros y la extensión que hay que añadir al nombre de las empresas
    para componer los nombres de los fichero.
    Se apoya en la función lee_precios para leer la información de una empresa
    y devuelve como salida un diccionario de series de precios en el que se
    usan como claves los nombres de las empresas
    '''
    pass

# Test de la función lee_precios_empresas
empresas = ['BBVA', 'SAN', 'ACS', 'GAS']

precios = lee_precios_empresas(empresas)
for e in precios:
    print('{}'.format(e), precios[e][:5])


def traza_curva(serie, label='Valor', color='blue'):
    ''' Traza una curva a partir de una serie de puntos

    ENTRADA:
       - serie: lista de valores numéricos -> [float]
       - label: eqtiqueta que se mostrará en la gráfica -> str
       - color: que se usará para trazar la curva -> str
    SALIDA EN PANTALLA:
       - gráfica con la evolución de la serie a lo largo del tiempo

    Utiliza el método plot del paquete matplotlib. Usaremos dos de los
    parámetros más importantes del método plot para controlar un poco el
    estilo de la gráfica:
        - label: etiqueta que se le asocia a la curva
        - color: color del trazo
    El método legend del objeto plt nos permite visualizar la leyenda con
    las etiquetas.
    '''
    plt.plot(serie, label=label, color=color)
    plt.legend()
    plt.show()

# Test de la función traza_curva
bbva_precios = lee_precios_empresa('BBVA')

traza_curva(bbva_precios, label='BBVA')
traza_curva(bbva_precios, color='black')

def traza_curvas(series, colores):
    ''' Traza varias curvas para varias series de puntos

    ENTRADA:
       - series: diccionario con las cotizaciones de varias empresas -> {str: [float]}
       - colores: lista de colores, uno por cada empresa -> [str]
    SALIDA EN PANTALLA:
       - gráfica con la evolución de todos los valores lo largo del tiempo

    Para resolver este ejercicio seguiremos los siguientes pasos:
    - Calcular una lista con los nombres de las series (las claves del diccionario)
    - Calcular una lista paralela a la anterior cuyos elementos serán las series (los
      valores del diccionario)
    - Recorrer en paralelo las dos listas anteriores, junto con la lista de colores,
      para generar los distintos trazos de la gráfica

    NOTA: Puede ser de utilidad la función 'built-in' zip
    '''
    pass

# Test de la función traza_curvas
empresas = ['BBVA', 'SAN', 'ACS', 'GAS']
precios = lee_precios_empresas(empresas)
colores = ['blue', 'red', 'orange', 'grey']

traza_curvas(precios, colores)

def calcula_incrementos(serie):
    ''' Calcula incrementos porcentuales (tantos por 1) a partir de una serie

    ENTRADA:
       - serie: lista de valores numéricos -> [float]
    SALIDA:
       - lista de incrementos -> [float]

    Se calcula el incremento de la posición "i" con respecto a la posición
    "i-1". La lista de salida tendrá, por tanto, una posición menos. Los
    valores resultantes se encuentran centrados en el 0 y estarán normalizados
    en cuanto a la magnitud. Por ejemplo un valor de 0.05 implica una subida
    diaria del 5%, y una bajada del 1% se corresponderá con -0.01.
    '''
    pass

# Test de la función calcula incrementos
empresas = ['BBVA', 'SAN', 'ACS', 'GAS']
precios = lee_precios_empresas(empresas)
colores = ['blue', 'red', 'orange', 'grey']

incrementos = {e: calcula_incrementos(precios[e]) for e in empresas}
traza_curvas(incrementos, colores)

def calcula_media_movil(serie, ventana=5):
    ''' Calcula la media móvil de una serie

    ENTRADA:
       - serie: lista de valores numéricos -> [float]
       - ventana: número de valores que se usarán para calcular la media móvil -> int
    SALIDA:
       - lista de medias móviles -> [float]

    La ventana indica el número de valores de la serie que se utilizan
    para calcular la media. Por defecto se usa una ventana de 5. El valor
    de la posición i es la media de los valores comprendidos en las posiciones
    [i-ventana, i] de la serie.
    El primer punto de la serie para el que se puede calcular la media móvil
    será "serie[ventana]". A los puntos anteriores se les asignará como valor
    de media móvil la correspondiente a este primer punto.
    '''
    pass


# Test de la función media_movil
bbva_precios = lee_precios_empresa('BBVA')
empresas = ['BBVA', 'SAN', 'ACS', 'GAS']
precios = lee_precios_empresas(empresas)
incrementos = {e: calcula_incrementos(precios[e]) for e in empresas}
colores = ['blue', 'red', 'orange', 'grey']

bbva_movil = calcula_media_movil(bbva_precios, ventana=10)
precios_media = {'Precios': bbva_precios, 'Media': bbva_movil}
traza_curvas(precios_media, ['blue', 'red'])
medias = {e: calcula_media_movil(incrementos[e], ventana=10) for e in empresas}
traza_curvas(medias, colores)


def similitud_coseno(serie_a, serie_b):
    ''' Similitud del coseno de dos series de valores

    ENTRADA:
       - serie_a: primera serie de valores numéricos -> [float]
       - serie_b: segunda serie de valores numéricos -> [float]
    SALIDA:
       - similitud del coseno entre ambas series -> float

    Dadas dos series de valores:
        [a1, a2, ..., an]
        [bi, b2, ..., bn]
    Para calcular la similitud del coseno es necesario, en primer lugar,
    calcular los siguientes sumandos:
        aa = a1 * a1 + a2 * a2 + ... + an * an
        bb = b1 * b1 + b2 * b2 + ... + bn * bn
        ab = a1 * b1 + a2 * b2 + ... + an * bn
    A partir de ellos, la similitud del coseno entre las dos series se
    calcula con la siguiente expresión:
        ab / (sqrt(aa) * sqrt(bb))
    '''
    pass

# Test de la función similitud_coseno
print(similitud_coseno([1, 2, 3], [2, 4, 6]))       # Dos vectores paralelos
print(similitud_coseno([1, 2, 3], [-2, -4, -6]))    # Dos vectores opuestos
print(similitud_coseno([1, 0, 1], [0, 1, 0]))       # Dos vectores ortogonales
print(similitud_coseno([1, 2, 3], [1.7, 4.3, 5.8])) # Dos vectores parecido

def busca_empresa_mas_parecida(empresa, empresas):
    ''' Empresa más parecida a otra de una lista de empresas

    ENTRADA:
       - empresa: nombre de la empresa de la que queremos buscar parecidas -> str
       - empresas: diccionario con las cotizaciones de varias empresas -> {str: [float]}
    SALIDA:
       - empresa más parecida y diccionario de similitudes -> (str, {str: float})

    Toma como entrada el nombre de una empresa y un diccionario de cotizaciones.
    Produce como salida una tupla con dos informaciones:
        - El nombre de la empresa más parecida
        - Un diccionario con las similitudes con cada empresa
    Se usa la similitud del coseno sobre los incrementos para determinar cuál
    es la empresa con cotizaciones más parecidas.

    Para resolver este ejercicio seguiremos los siguientes pasos:
    - Cargar las cotizaciones de la 'empresa' en la lista 'precios_empresa' y
      calcular los incrementos en la lista 'inc_empresa'
    - Cargar las cotizaciones de la lista 'empresas' en el diccionario
      'precios_empresas' y calcular los correspondientes incrementos en
      el diccionario 'inc_empresas'
    - Calcular las similitudes de 'empresa' con cada una de las 'empresas'
      y guardarlas en el diccionario 'similitudes'
    - Calcular el nombre de la empresa más parecida con la siguiente instrucción:

            mas_parecida = max(similitudes, key=similitudes.get)
    '''
    pass
'''
# Test de la función empresa_mas_parecida
bancos_menos_bbva = ['CABK', 'BKT', 'SAB', 'SAN', 'POP']
constructoras = ['ACS', 'FER', 'FCC']
energia = ['ELE', 'REE', 'ENG', 'GAS', 'IBE']
empresas = bancos_menos_bbva + constructoras + energia

(empresa, similitudes) = busca_empresa_mas_parecida('BBVA', empresas)
print('La empresa más parecida a BBVA es ' + empresa)
for e in similitudes.keys():
    print("{:5}  {:5.3f}".format(e, similitudes[e])
'''
