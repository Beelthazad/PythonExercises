# -*- coding: utf-8 -*-
from os import listdir
import csv
from collections import namedtuple
from datetime import datetime
'''
Se dispone de los resultados de primera y segunda división desde la temporada 00-01 hasta la temporada 15-16. Los datos están organizados en dos carpetas (Primera y Segunda),
y dentro de cada una de ellas hay un fichero CSV para cada temporada. Cada línea de estos ficheros se corresponde con un partido, y en ella se incluyen cinco datos:

    Fecha del partido
    Equipo que juega en casa
    Goles del equipo de casa
    Equipo visitante
    Goles del equipo visitante

Estan serían, por ejemplo, las primeras líneas del fichero de la temporada 15-16 en primera división:

        21/08/2015,Málaga CF,0,Sevilla FC,0
        21/08/2015,Atlético de Madrid,1,UD Las Palmas,0
        21/08/2015,RC Deportivo,0,Real Sociedad,0
        21/08/2015,RCD Espanyol,1,Getafe CF,0
        21/08/2015,Rayo Vallecano,0,Valencia CF,0
        21/08/2015,Athletic Club,0,FC Barcelona,1
        21/08/2015,Real Betis,1,Villarreal CF,1

Los principales aspectos que tendremos que resolver a la hora de procesar estos datos de entrada serán: separar adecuandamente los campos mediante las comas, interpretar el formato
de las fechas para extraer el día, el mes y el año, y leer todos los ficheros de una carpeta para obtener una lista con todos los partidos de una competición.
'''


Partido = namedtuple('Partido', 'fecha local goles_local visitante goles_visitante')

def lee_temporada(fichero):
    ''' Lee el fichero de una temporada y devuelve una lista de partidos

    ENTRADA:
       - fichero: nombre del fichero del que se quieren leer los datos -> str
    SALIDA:
       - lista de partidos -> [Partido(datetime.date, str, int, str, int)]

    Cada partido se representa con una tupla con los siguientes valores:
    - fecha
    - equipo local
    - goles equipo local
    - equipo visitante
    - goles equipo visitante
    Usaremos el módulo csv de la librería estándar de Python para leer los
    ficheros de entrada.
    En el caso de las fechas, nos hará falta convertir una cadena de caracteres
    en una fecha (objeto date del módulo datetime). Para ello utilizaremoos el
    método strptime del módulo datetime de la librería estándar de Python.
    En concreto, para crear un objeto date a partir de una cadena_fecha con el
    formato que tenemos en nuestros ficheros de datos, podemos usar la siguiente
    instrucción:

        datetime.strptime(fecha, "%d/%m/%Y").date()

    También hay que realizar un pequeño procesamiento con los goles. Hay que
    pasar del formato cadena (que es lo que se interpreta al leer el csv) a un
    valor numérico (para poder aplicar operaciones matemáticas si fuese
    necesario).
    '''
    pass

# Test de la función lee_temporada
primera_15_16 = lee_temporada('./data/Primera/15-16.csv')
print(primera_15_16[:5])



def lee_competicion(carpeta):
    ''' Lee todas las temporadas y devuelve una lista de partidos

    ENTRADA:
       - carpeta: ruta de la carpeta en la que se encuentran los ficheros -> str
    SALIDA:
       - lista de partidos -> [Partido(datetime.date, str, int, str, int)]

    Toma como entrada la ruta de una carpeta en la que hay varios
    ficheros correspondientes a distintas temporadas de una misma
    competición.
    Devuelve como salida la lista de partidos resultante tras unir
    las listas que construye la función lee_temporada() a partir
    de cada fichero de la carpeta.
    '''
    pass



# Test de la función lee_competición
primera = lee_competicion('./data/Primera/')
segunda = lee_competicion('./data/Segunda/')
partidos = primera + segunda
print(len(partidos))
print(len(primera), primera[:5])
print(len(segunda), segunda[:5])


def equipos_participantes(partidos):
    ''' Equipos participantes en una lista de partidos

    ENTRADA:
       - partidos: lista de partidos -> [Partido(datetime.date, str, int, str, int)]
    SALIDA:
       - conjunto de equipos -> {str}

    Calcula una lista con los nombres de los equipos que han aparecido
    al menos una vez en la lista de partidos que recibe como entrada.
    '''
    pass

# Test de la función equipos_participantes
equipos_primera = equipos_participantes(primera)
print(len(equipos_primera), equipos_primera)
equipos_segunda = equipos_participantes(segunda)
print(len(equipos_segunda), equipos_segunda)

def partidos_por_fecha(partidos, inicio=None, fin=None):
    ''' Filtra los partidos jugados en un rango de fechas

    ENTRADA:
       - partidos: lista de partidos -> [Partido(datetime.date, str, int, str, int)]
       - inicio: fecha inicial del rango -> datetime.date
       - fin: fecha final del rango -> datetime.date
    SALIDA:
       - lista de partidos seleccionados -> [Partido(datetime.date, str, int, str, int)]

    Se devuelven aquellos partidos que se han jugado entre las fechas inicio
    y fin. Ambos parámetros serán objetos dete del módulo datetime.
    Si inicio es None, se incluirán los partidos desde el principio de
    la serie, y si fin es None se inlcuirán los partidos hasta el último de
    la serie.
    '''
    pass

# Test de la función partidos_por_fecha
inicio = datetime(2007, 9, 15).date()
fin = datetime(2008, 7, 1).date()
print(len(partidos_por_fecha(partidos, inicio, fin)))
print(len(partidos_por_fecha(partidos, inicio, None)))
print(len(partidos_por_fecha(partidos, None, fin)))
print(len(partidos_por_fecha(partidos, None, None)))

def partidos_por_equipos(partidos, equipos):
    ''' Filtra los partidos jugados por un conjunto de equipos

    ENTRADA:
       - partidos: lista de partidos -> [Partido(datetime.date, str, int, str, int)]
       - equipos: de los que se requieren los partidos -> [str]
    SALIDA:
       - lista de partidos seleccionados -> [Partido(datetime.date, str, int, str, int)]

    Se devuelven aquellos partidos que se han jugado por alguno de los
    equipos incluidos en la lista que se recibe como segundo parámetro.
    '''
    pass

# Test de la función partidos_por_equipos
de_madrid = ['Real Madrid', 'Rayo Vallecano', 'Atlético de Madrid', 'Getafe CF', 'CD Leganés']
partidos_de_madrid = partidos_por_equipos(partidos, de_madrid)
print(len(partidos_de_madrid), partidos_de_madrid[:5])

def calcula_elo(elo_a, elo_b, goles_a, goles_b, k=20):
    ''' Cálculo de los nuevos valores elo tras un partido

    ENTRADA:
       - elo_a: puntos Elo del equipo A antes del partido -> float
       - elo_b: puntos Elo del equipo B antes del partido -> float
       - goles_a: goles del equipo A en el partido -> int
       - goles_b: goles del equipo B en el partido -> int
       - k: parámetro para regular la velocidad de cambio en el ranking -> float
    SALIDA:
       - nueva puntuación Elo del equipo A -> float
       - nueva puntuación Elo del equipo B -> float

    Dados dos participantes A y B, con puntuación ELOA y ELOB, respectivamente,
    las probabilidades de que cada uno de ellos gane el enfrentamiento se
    calculan así:
        EA = 1/(1+pow(10,(ELOB-ELOA)/400))
        EB = 1/(1+pow(10,(ELOA-ELOB)/400))
    A partir de EA y EB, se calculan los nuevos valores de ELOA y ELOB de la
    siguiente forma:
        ELOA' = ELOA + (RA - EA) * k
        ELOB' = ELOB + (RB - EB) * k
    Donde k es un parámetro que regula la estabilidad del ranking y su
    velocidad de convergencia (usaremos k=20 por defecto) y RA y RB es el
    resultado de cada jugador (1=victoria, 0.5=empate, 0=derrota).
    '''
    pass



# Test de la función calcula_elo
print(calcula_elo(1000, 1000, 3, 3)) # Equipos parejos, empatan
print(calcula_elo(1000, 1000, 3, 0)) # Equipos parejos, gana uno
print(calcula_elo(2000, 1000, 3, 0)) # Equipos no parejos, gana el mejor
print(calcula_elo(2000, 1000, 3, 3)) # Equipos no parejos, empatan
print(calcula_elo(2000, 1000, 0, 3)) # Equipos no parejos, gana el peor

def muestra_ranking(ranking, limite=None):
    ''' Muestra un ranking ordenado de mayor a menor

    ENTRADA:
       - ranking: puntuación Elo para cada equipo -> {str: float}
       - limite: número máximo de equipos a mostrar
    SALIDA EN PANTALLA:
       - listado ordenado de los equipos y su puntuación Elo

    Toma como entrada un ranking (diccionario {equipo,puntos}) y calcula
    a partir de él una lista de tuplas (puntos, equipo) ordenada de mayor
    a menor por puntuación.
    El parámetro limite establece el numero de elementos del ranking ordenado
    que se mostrará como salida. Si el limite es None, se mostrará el ranking
    completo.
    El listado de salida debe incluir para cada equipo su posición en el
    ranking, su nombre y su puntuación Elo. Se puede usar el método format
    de las cadenas de caracteres de Python para dar un buen formato a este
    listado. Hay una buena explicación sobre la notación usada por el
    método format en:
        https://pyformat.info/
    '''
    pass

# Test de la función muestra_ranking
ranking =  {'CD San Roque': 1489, 'Real Balompédica Linense': 1912,
            'UD Los Barrios': 1636, 'Algeciras CF': 1750}
muestra_ranking(ranking)

def calcula_ranking_elo(partidos, ranking_previo=dict()):
    ''' Ranking Elo de todos los equipos tras una secuencia de partidos

    ENTRADA:
       - partidos: lista de partidos -> [Partido(datetime.date, str, int, str, int)]
       - ranking_previo: puntuación Elo inicial para los equipos -> {str: float}
    SALIDA:
       - ranking actualizado tras los partidos -> {str: float}

    El resultado del ranking será un diccionario en el que las claves serán
    los equipos y los valores serán las puntuciaciones de los equipos.

    De inicio se asigna a todos los equipos la misma puntuación Elo. Este
    valor inicial puede ser cualquiera. En ajedrez, por ejemplo, se suele
    utilizar el valor 1500 para aquellos jugadores de los que no se tiene
    aún ninguna información. Nostros usaremos el valor 1000. Además, cabe
    la posibilidad de recibir como parámetro un ranking previo. En ese caso
    las entradas de ese diccionario prevalecerán sobre el valor inicial
    por defecto.

    Los partidos deben procesarse en orden cronológico. Para ello, antes
    de empezar, deberá ordenarse la lista de partidos por este criterio.
    '''
    pass

# Test de la función calcula_ranking_elo
elo = calcula_ranking_elo(primera)
muestra_ranking(elo, limite=10)
print()
elo = calcula_ranking_elo(primera, ranking_previo={'Cádiz CF':2000})
muestra_ranking(elo, limite=10)

def calcula_rendimiento(equipo, partidos, ranking_elo):
    ''' Cálculo del rendimiento de un equipo en un conjunto de partidos

    ENTRADA:
       - equipo: del que se quiere calcular el rendimiento -> str
       - partidos: lista de partidos de la competición -> [Partido(datetime.date, str, int, str, int)]
       - ranking_elo: puntuación Elo inicial para los equipos -> {str: float}
    SALIDA:
       - ranking actualizado tras los partidos -> {str: float}

    Toma como entrada un equipo, una lista de partidos y un ranking Elo.
    Calcula como salida el rendimiento del equipo en función de los partidos
    de la lista en los que ha participado. Se usa para ello la siguiente
    fórmula:

               suma Elo de competidores + victorias*400 - derrotas*400
       rend = ---------------------------------------------------------
                             número de partidos

    Una buena forma de enfocar la implementación es calcular, a partir de la
    lista de partidos, una lista tuplas (contrincante, diferencia de goles).
    Solo con el signo de la diferencia se puede determinar si para ese
    contrincante hay que añadir 400, -400 ó 0 al acumular su puntuación Elo.
    Según el enfoque, puede venir bien usar una función que calcule el signo
    de un número entero. Pero en Python no está disponible, ¿cuál es el 'idiom'
    Python para calcular el signo de un número?
    '''
    pass



# Test de la función calcula_rendimiento
inicio_14 = datetime(2014, 8, 15).date()
fin_16 = datetime(2016, 7, 1).date()
partidos_hasta_14 = partidos_por_fecha(partidos, inicio=None, fin=inicio_14)
ranking_hasta_14 = calcula_ranking_elo(partidos_hasta_14)
primera_14_16 = partidos_por_fecha(partidos, inicio=inicio_14, fin=None)
print(calcula_rendimiento('Real Madrid', primera_14_16, ranking_hasta_14))

def calcula_ranking_rendimiento(equipos, partidos, ranking_elo):
    ''' Cálculo del ranking de rendimiento de un conjunto de equipos

    ENTRADA:
       - equipos: de los que se quiere calcular el rendimiento -> [str]
       - partidos: lista de partidos de la competición -> [Partido(datetime.date, str, int, str, int)]
       - ranking_elo: puntuación Elo inicial para los equipos -> {str: float}
    SALIDA:
       - ranking actualizado tras los partidos -> {str: float}

    Toma como entrada una lista de equipos, una lista de partidos en
    los que pueden haber participado esos equipos y un ranking_elo.
    Produce como salida un ranking en el que a cada equipo de la
    lista equipos se le asocia su rendimiento en función de los
    partidos en los que ha participado.
    '''
    pass

# Test de la función calcula_ranking_rendimiento
andaluces = ['Málaga CF', 'Real Betis', 'Sevilla FC', 'RC Recreativo',
            'Cádiz CF', 'Xerez CD', 'Granada CF', 'Córdoba CF']
rendimiento = calcula_ranking_rendimiento(andaluces, primera_14_16, ranking_hasta_14)
muestra_ranking(rendimiento)
