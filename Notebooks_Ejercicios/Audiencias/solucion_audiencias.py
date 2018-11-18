# # -*- coding: utf-8 -*-
import csv
import statistics
from matplotlib import pyplot as plt

'''
Lee el fichero de entrada y devuelve una lista de audiencias.

Cada linea del fichero se corresponde con la audiencia de un programa,
se representa con una tupla que tiene ( edición, audiencia )

Hay que transformar la entrada (cadenas de caracteres) en valores
numéricos para que puedan ser procesados posteriormente.
'''

def lee_audiencias(fichero):
    audiencias = []
    with open(fichero, encoding='utf-8') as f:
        for linea in f:
            edicion, share = linea.split(',')
            edicion = int(edicion)
            share = float(share)
            tupla = (edicion, share)
            audiencias.append(tupla)
    return audiencias

AUDIENCIAS_GH = lee_audiencias('./data/GH.csv')
print("\x1b[6;30;42m" ,"Las audiencias con la funcion lee_audiencias original es...", "\x1b[0m" ,AUDIENCIAS_GH[:20], "\n")

'''
    Podemos encontrar una implementación mucho más simple.
'''

def lee_audiencias_opt(fichero):
    with open(fichero, encoding='utf-8') as f:
        # Se crea un objeto lector (un iterator) que separará los valores por comas
        lector = csv.reader(f)
        # Lista por comprensión sobre el objeto lector
        audiencias = [(int(edicion), float(share)) for edicion, share in lector]
    return audiencias

AUDIENCIAS_GH_OPT = lee_audiencias_opt('./data/GH.csv')
print("\x1b[6;30;42m" ,"Las audiencias con la función l_a_opt será...", "\x1b[0m" , AUDIENCIAS_GH_OPT[:20], "\n")

'''
    Una vez que hemos cargado los datos en una estructura en memoria ya podemos empezar a trabajar con ellos. Lo haremos con funciones que denominaremos de transformación y filtrado.
    Con estas funciones podremos obtener información derivada de los datos originales en crudo, extraer un subconjunto de los datos en base a una consulta, y también podremos transformar
    los datos originales para obtener nuevas estructuras de datos que nos sirvan para resolver los problemas que nos plantee cada proyecto.

    En este ejercicio implementaremos tres funciones de este tipo que nos permitirán:

    Calcular una lista con las distintas ediciones del programa presentes en los datos de entrada
    Seleccionar los datos de audiencia de unas ediciones determinadas
    Calcular las medias de share por cada edición

    La primera de las funciones se llama calcula_ediciones y obtendrá, a partir de los datos de entrada, una lista ordenada de las diferentes ediciones para las que hay algún registro en ellos.
    Las siguientes celdas contienen la implementación y el test, respectivamente, de esta función:
'''

def calcula_ediciones(audiencias):

    '''
    Calcula el conjunto de ediciones presentes en una lista de audiencias

    ENTRADA:
       - audiencias: lista de audiencias -> [(int, float)]
    SALIDA:
       - lista de ediciones -> [int]

       Toma como entrada una lista de tuplas (edición, share) y produce como
       salida una lista ordenada con aquellas ediciones para las que haya al menos
       una tupla. La lista de salida no contendrá elementos repetidos.
       '''

    ediciones = {e for e, _ in audiencias}
    ediciones = list(ediciones)
    ediciones.sort()
    return ediciones

ediciones = calcula_ediciones(AUDIENCIAS_GH_OPT)
print("\x1b[6;30;42m" , "Función calcula ediciones...", "\x1b[0m" ,ediciones, "\n")


def filtra_por_ediciones(audiencias, ediciones):

    '''
    Selecciona las tuplas correspondientes a unas determinadas ediciones

    ENTRADA:
       - audiencias: lista de audiencias -> [(int, float)]
       - ediciones: lista de ediciones a seleccionar -> [int]
    SALIDA:
       - lista de audiencias seleccionadas -> [(int, float)]

    Toma como entrada una lista de tuplas (edición, share) y un conjunto de
    ediciones. Produce como salida otra lista de tuplas en la que solo se
    incluyen aquellas cuya edición sea una de las que se recibe como parámetro.
    '''

    filtradas = [(e, s) for e, s in audiencias if e in ediciones]
    return filtradas

audiencias_123 = filtra_por_ediciones(AUDIENCIAS_GH_OPT, [1,2,3])
print("\x1b[6;30;42m" , "Función FILTRA ediciones...", "\x1b[0m" ,audiencias_123, "\n")

def medias_por_ediciones(audiencias):
    '''
    Calcula la media de audiencia para cada edición

    ENTRADA:
       - audiencias: lista de audiencias -> [(int, float)]
    SALIDA:
       - medias de audiencia por cada edición -> {int : float}

    Toma como entrada una lista de tuplas (edición, share) y produce como
    salida un diccionario en el que las claves son las ediciones y los
    valores son las medias de audiencia de cada edición.
    '''
    medias = dict()
    ediciones = calcula_ediciones(audiencias)
    for edicion in ediciones:
        # Calculamos la lista de shares de cada edición
        shares = [s for e, s in audiencias if edicion == e]
        # Usamos la lista de shares para calcular la media
        medias[edicion] = sum(shares)/len(shares)
    return medias

medias = medias_por_ediciones(AUDIENCIAS_GH_OPT)
print("\x1b[6;30;42m" , "Función MEDIAS por ediciones...", "\x1b[0m", "\n")
print(medias)

def muestra_evolucion_audiencias(audiencias):
    ''' Genera una curva con la evolución de las audiencias

    ENTRADA:
       - audiencias: lista de audiencias -> [(int, float)]
    SALIDA EN PANTALLA:
       - gráfica con la evolución de los shares a lo largo del tiempo

    Toma como entrada una lista de tuplas (edición, share) y muestra una
    curva con la evolución de los shares a lo largo del tiempo.

    Para generar la gráfica usaremos elementos del paquete matplotlib. Estas
    son las instrucciones que permiten trazar una curva a partir de la lista de
    shares:
        plt.plot(shares, label='audiencia')
        plt.legend()
        plt.show()
    '''
    # Calculamos la lista de shares
    shares = [s for _, s in audiencias]
    # Componemos y visualizamos la gráfica
    plt.plot(shares, label='audiencia')
    plt.legend()
    plt.show()

muestra_evolucion_audiencias(AUDIENCIAS_GH_OPT) # Test de la función muestra_evolucion_audiencias

def muestra_medias_por_ediciones(audiencias):
    ''' Genera un diagrama de barras con la media de audiencia de cada edición

    ENTRADA:
       - audiencias: lista de audiencias -> [(int, float)]
    SALIDA EN PANTALLA:
       - gráfica con las medias por cada edición

    Toma como entrada una lista de tuplas (edición, share) y muestra un diagrama
    de barras. Habrá una barra por cada edición presente en la lista de audiencias.
    Se mostrará la media de shares de cada edición.

    Estas son las instrucciones 'matplotlib' para trazar el diagrama de barras
    a partir de una lista de ediciones y otra lista (con el mismo orden) de
    medias de shares:
        plt.bar(ediciones, lista_medias)
        plt.xticks(ediciones, ediciones, fontsize=8)
        plt.show()
    '''
    # Calculamos la lista de ediciones
    ediciones = calcula_ediciones(audiencias)
    # Calculamos las medias por cada edición
    dicc_medias = medias_por_ediciones(audiencias)
    # Generamos una lista de medias con el mismo orden que las ediciones
    lista_medias = [dicc_medias[e] for e in ediciones]
    # Componemos y visualizamos la gráfica
    plt.bar(ediciones, lista_medias)
    plt.xticks(ediciones, ediciones, fontsize=8)
    plt.show()

muestra_medias_por_ediciones(AUDIENCIAS_GH_OPT)
# ------------------------------------------------------------------------------------------------
# Ejercicios a completar...

def mediana_c(lista):
    ''' Calcula la mediana de una serie

    ENTRADA:
       - lista: serie de valores numéricos -> [float]
    SALIDA:
       - mediana de los valores de entrada -> float
    '''
    lista.sort()

    if len(lista) % 2 != 0: # Si es impar...
        return lista[len(lista)/2]
    else:                    # Si es par...
        x = lista[int(len(lista)/2)]
        y = lista[(int(len(lista)/2)-1)]
        return (x+y)/2
# La mediana del share, si el total de valores de la lista es impar, será el valor central.
# Si es par, será la media de las dos puntuaciones centrales. Los datos deben de estar ordenados de menor a mayor.
    pass


def calcula_estadisticos(audiencias):
    ''' Calcula la media, mediana, máximo y mínimo de una lista de audiencias

    ENTRADA:
       - audiencias: lista de audiencias -> [(int, float)]
    SALIDA:
       - media, mediana, máximo y mínimo -> (float, float, float, float)
    '''
    shares = [s for _, s in audiencias]
    # MEDIA
    media = sum(shares)/2
    # MEDIANA
    mediana = mediana_c(shares)
    # MAXIMO
    maximo = max(shares)
    # MINIMO
    minimo = min(shares)
    return media,mediana,maximo,minimo
    pass

media, mediana, maximo, minimo = calcula_estadisticos(AUDIENCIAS_GH_OPT)
print("\x1b[6;30;42m" , "Función calcula_estadisticos()...", "\x1b[0m" ,"\n")
print('Media: ', media)
print('Mediana:', mediana)
print('Máximo:', maximo)
print('Mínimo:', minimo)

def lista_medias_shares(audiencias):
    ''' Calcula una lista ordenada de ediciones según su media de shares

    ENTRADA:
       - audiencias: lista de audiencias -> [(int, float)]
    SALIDA:
       - pares (medias de audiencia, edición) ordenados de mayor a menor media -> [(float, int)]
    '''
    medias = medias_por_ediciones(audiencias)
    # Terminar
    shares_eds_i = list()
# Creamos una lista tuplas a partir del diccionario que genera la función medias_por_ediciones().
    for edicion, share_media in medias.items():
        shares_eds_i.append(tuple([float(share_media),int(edicion)]))
# Ordenamos la lista por el segundo elemento de la tupla. Podríamos hacerlo un 127% + rápido usando como key del ordenado itemgetter(1).
    shares_eds_i.sort(key=lambda x:x[1])
    return shares_eds_i
    pass


# Test de la función lista_medias_shares
shares_eds = lista_medias_shares(AUDIENCIAS_GH)
print("\x1b[6;30;42m" , "Función lista_medias_share...", "\x1b[0m" ,"\n")
for s, e in shares_eds:
    print("{:6.3f} -> {:3f}".format(e, s))
