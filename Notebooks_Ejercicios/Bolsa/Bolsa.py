#!/usr/bin/env python
# coding: utf-8

# # Ejercicio: Análisis de datos bursátiles
# **Autor**: José A. Troyano.      **Revisores**: Fermín Cruz, Carlos G. Vallejo.     **Última modificación:** 29/10/2018

# El análisis bursátil tiene como objetivo el estudio del comportamiento de los mercados, con idea de obtener información que ayude a la toma de decisiones de inversión. Cuando se usan técnicas estadísticas y herramientas informáticas para realizar este análisis se suele hablar de _quantitative analysis_. Y a los profesionales que se especializan en este tipo de técnicas y herramientas se les llama <a href="https://en.wikipedia.org/wiki/Quantitative_analyst">Quants</a>. En este ejercicio haremos una pequeña incursión en este apasionante mundo, mediante un análisis simple sobre datos de cotizaciones de empresas españolas. 
# 
# Para implementar algunas de las funciones que nos hacen falta, haremos uso de utilidades disponibles en la librería estándar de Python y en el paquete <code>matplotlib</code>. Para ello, antes de empezar, deberemos importar los siguientes elementos:

# In[ ]:


from math import sqrt
from matplotlib import pyplot as plt
import statistics


# ## 1. Carga de datos

# En este ejercicio usaremos datos obtenidos de <a href="https://es.finance.yahoo.com/">Yahoo! Finance</a>. En concreto, dispondremos de las cotizaciones durante las sesiones del año 2016 de una serie de empresas del <a href="https://es.wikipedia.org/wiki/IBEX_35">IBEX 35</a>. Para identificar a las empresas usaremos las mismas abreviaturas empleadas en el índice IBEX 35. Estos son los nombres de las empresas para las que tenemos datos:
# 
# <pre>
#         bancos = ['BBVA', 'CABK', 'BKT', 'SAB', 'SAN', 'POP']
#         constructoras = ['ACS', 'FER', 'FCC']
#         energia = ['ELE', 'REE', 'ENG', 'GAS', 'IBE']
# </pre>
# 
# De toda la información proporcionada por la API de _Yahoo Finance!_ solo se ha seleccionado el precio de cierre diario de cada empresa. Los datos se encuentran en la carpeta <code>datos</code>, dentro de la cual hay un fichero de texto para cada empresa. En esos ficheros, cada línea se corresponde con el valor de cierre de un día. Los datos están ordenados cronológicamente, pero no se almacena ninguna información sobre la fecha. Los nombres de estos ficheros se componen con la abreviatura de la empresa, seguida del sufijo <code>'MC.txt'</code>. Estas serían, por ejemplo, las primeras líneas del fichero <code>BBVA.MC.txt</code> correspondiente a la empresa BBVA:
# 
# <pre>
#         5.96213
#         5.83916
#         5.878080000000001
#         5.75245
#         5.6790199999999995
#         5.55074
#         5.61257
#         5.63436
#         5.63526
#         5.57354
# </pre>
# 
# La siguiente función será la encargada de leer el fichero de una empresa, y construir a partir de él una estructura de datos en memoria. Usaremos una lista para almacenar todas las cotizaciones diarias de una empresa.

# In[ ]:


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
    pass


# In[ ]:


# Test de la función lee_precios_empresa
bbva_precios = lee_precios_empresa('BBVA')

print(bbva_precios[:20])


# Apoyándonos en la función anterior, implementaremos la función <code>lee_precios_empresas</code> que cargará en memoria los datos correspondientes a varias empresas. Crearemos un diccionario de listas para almacenar las cotizaciones de varias empresas.

# In[ ]:


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


# In[ ]:


# Test de la función lee_precios_empresas
empresas = ['BBVA', 'SAN', 'ACS', 'GAS']

precios = lee_precios_empresas(empresas)
for e in precios:
    print('{}'.format(e), precios[e][:5]) 


# ## 2. Generación de gráficas

# Una de las mayores ventajas del lenguaje Python es que, con muy pocas líneas de código, se pueden escribir programas que directamente nos proporcionan resultados de utilidad. Esto se debe fundamentalmente a dos razones:
# - El lenguaje en sí es muy expresivo y solo te obliga a escribir _lo justo_
# - Hay muchas librerías desarrolladas por terceros que resuelven infinidad de problemas interesantes
# 
# En esta sección veremos la segunda de estas razones _en acción_ a través de la librería <a href="https://matplotlib.org/">matplotlib</a>, que es el estándar _de facto_ para generar gráficas en Python. <code>matplotlib</code> es una librería muy extensa, completa y compleja (por la cantidad de alternativas que ofrece). Pero, a pesar de esa complejidad, es muy fácil obtener gráficos simples e informativos como muestra la siguiente función: 

# In[ ]:


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


# In[ ]:


# Test de la función traza_curva
bbva_precios = lee_precios_empresa('BBVA')

traza_curva(bbva_precios, label='BBVA')
traza_curva(bbva_precios, color='black')


# Con lo poco que conocemos de <code>matplotlib</code> podemos generar fácilmente una gráfica que nos permita comparar visualmente los precios de varias empresas. Lo haremos con la función <code>traza_curvas</code> que tomará como entrada un diccionario de series y una lista con el color de trazo que utilizaremos para cada serie:

# In[ ]:


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


# In[ ]:


# Test de la función traza_curvas
empresas = ['BBVA', 'SAN', 'ACS', 'GAS']
precios = lee_precios_empresas(empresas)
colores = ['blue', 'red', 'orange', 'grey']

traza_curvas(precios, colores)


# ## 3. Dos indicadores simples

# Los indicadores son herramientas matemáticas que dan una visión objetiva de las cotizaciones, con idea de ayudar a comprender el estado de las mismas y apoyarse en ellos a la hora de tomar decisiones de mercado. Lo ideal sería disponer de _indicadores adelantados_, que _den señales_ del mercado que nos permitan anticiparnos a su movimiento. En la práctica esta _utopía_ está muy lejos de ser alcanzada en el ámbito bursátil.
# 
# Los indicadores se pueden ver como funciones que toman series de valores, y producen como salida una información más resumida que es más fácil de interpretar por las personas. En esta sección implementaremos dos funciones que implican trasformaciones simples de las series de datos de entrada.

# ### 3.1. Cálculo de incrementos diarios

# Estrictamente hablando no vamos a calcular un indicador, sino que más bien se trata de una normalización de datos. La idea es disponer de una representación de las series que no dependa del rango en el que se muevan los precios de cada empresa. Si nos fijamos, por ejemplo, en la gráfica que muestra los precios de <code>['BBVA', 'SAN', 'ACS', 'GAS']</code> observamos que <code>'BBVA'</code> se mueve en el entorno de 5 euros, mientras que <code>'ACS'</code> lo hace en el de 25 euros. Con la trasformación que vamos a implementar, los cambios diarios serán expresados en tantos por uno, lo que permitirá comparar la evolución de valores que oscilan en rangos distintos: 

# In[ ]:


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


# In[ ]:


# Test de la función calcula incrementos
empresas = ['BBVA', 'SAN', 'ACS', 'GAS']
precios = lee_precios_empresas(empresas)
colores = ['blue', 'red', 'orange', 'grey']

incrementos = {e: calcula_incrementos(precios[e]) for e in empresas}
traza_curvas(incrementos, colores)


# Visualmente, esta última gráfica es bastante confusa. De hecho, salvo el pico de bajada del 20% de 'SAN', es bastante difícil interpretarla. Pero, como veremos más adelante, esta trasformación destila una información útil. Nos permitirá, por ejemplo, determinar el grado de parecido entre la evolución de dos empresas.

# ### 3.2. Cálculo de la media móvil

# La media móvil es un indicador muy simple y, a pesar de ello, muy utilizado en el análisis bursátil. Sirve para _eliminar ruido_, filtrando los movimientos puntuales y analizando los datos con una perspectiva temporal más amplia.
# 
# La media móvil simple, en un determinado momento, se calcula mediante la media aritmética de los $n$ datos anteriores de la serie. Si $n$ es muy grande, la influencia de los datos antiguos será mayor. Por su parte, valores bajos de $n$ hacen que el peso del indicador recaiga solo la historia reciente.
# 
# A pesar de ser un indicador muy simple, hay estrategias relativamente efectivas que se apoyan en la detección de señales de compra y venta en función de los puntos de corte de medias con distintos valores de $n$.

# In[ ]:


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


# In[ ]:


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


# En la primera de las gráficas, observamos la utilidad de la media móvil a la hora de _limpiar de ruidos_ una serie de precios. La curva de la media es mucho más suave, lo que permite destacar de forma más nítida la tendencia de precios de BBVA.
# 
# En la segunda gráfica también queda patente el beneficio de la media móvil. Si la comparamos con la gráfica en la que se solapaban directamente los incrementos de las cuatro empresas, en esta nueva visualización van apareciendo con más claridad puntos potencialmente significativos.

# ## 4. Análisis comparativo

# En este punto, vamos a aprovechar parte de lo que llevamos implementado hasta ahora para responder a una pregunta que nos puede dar una información de utilidad a la hora de operar en bolsa:
# 
# <center>_¿Cuál es el grado de parecido entre dos empresas?_</center>
# 
# Podemos utilizar este dato, por ejemplo, para diversificar carteras. Si tenemos valores de empresas muy parecidas corremos el riesgo de que todas caigan al mismo tiempo si hay un desplome en el sector en el que operan. En cambio, si tenemos una cartera diversificada puede que ganemos menos en tiempos de subida, pero es más probable que se puedan compensar pérdidas de algunas empresas (en tiempos de bajadas) si otras aguantan la cotización porque tienen un comportamiento potencialmente distinto.
# 
# En esta sección utilizaremos la _similitud del coseno_ sobre los incrementos de precios para medir de forma objetiva el grado de parecido entre dos series en el _pasado_. En bolsa es importante resaltar lo de _el pasado_ porque, como reza una famosa frase en el mundo bursátil: "beneficios pasados no aseguran beneficios futuros". 

# ### 4.1. Similitud del coseno

# La <a href="https://es.wikipedia.org/wiki/Similitud_coseno">similitud del coseno</a> es una medida de la similitud entre dos vectores que se calcula a partir del coseno del ángulo comprendido entre ellos. Esta función vale $1$ si ambos vectores tienen la misma dirección, $0$ si son ortogonales y $-1$ si son opuestos.
# 
# Si usamos esta medida sobre series de valores, el mayor parecido entre dos series vendría dado por una similitud de $1$, mientras que un valor de $-1$ se correspondería con el grado de similitud de dos series completamente antagónicas.
# 
# El cálculo de la similitud del coseno es bastante simple, y se basa en el producto escalar entre los vectores:
# 
# $$
# similitud(A,B) = \frac{\sum a_ib_i}{\sqrt{\sum a_i^2}\sqrt{\sum b_i^2}}
# $$

# In[ ]:


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


# In[ ]:


# Test de la función similitud_coseno
print(similitud_coseno([1, 2, 3], [2, 4, 6]))       # Dos vectores paralelos
print(similitud_coseno([1, 2, 3], [-2, -4, -6]))    # Dos vectores opuestos
print(similitud_coseno([1, 0, 1], [0, 1, 0]))       # Dos vectores ortogonales
print(similitud_coseno([1, 2, 3], [1.7, 4.3, 5.8])) # Dos vectores parecidos


# ### 4.2. Cálculo de la empresa más parecida

# Ya tenemos todos los elementos para calcular el grado de similitud del comportamiento en bolsa de dos empresas. Lo haremos a través de la función <code>busca_empresa_mas_parecida</code> que toma como entrada el nombre de una empresa y un diccionario de cotizaciones, y produce como salida el nombre de la empresa más parecida y un diccionario con las similitudes con cada empresa:

# In[ ]:


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


# In[ ]:


# Test de la función empresa_mas_parecida
bancos_menos_bbva = ['CABK', 'BKT', 'SAB', 'SAN', 'POP']
constructoras = ['ACS', 'FER', 'FCC']
energia = ['ELE', 'REE', 'ENG', 'GAS', 'IBE']
empresas = bancos_menos_bbva + constructoras + energia

(empresa, similitudes) = busca_empresa_mas_parecida('BBVA', empresas)
print('La empresa más parecida a BBVA es ' + empresa)
for e in similitudes.keys():
    print("{:5}  {:5.3f}".format(e, similitudes[e]))

