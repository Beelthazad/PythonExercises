import csv
import statistics
import matplotlib.pyplot as plt

def lee_audiencias(fichero):
  try:
    with open(fichero, 'r') as f:
        # Exception handling...
        # Creamos un objecto lector (iterator) que separará los valores por comas
        lector = csv.reader(f)
        # Lista por compresión sobre el objeto lector
        audiencias = [(int(edicion), float(share)) for edicion, share in lector]
        print("Se ha creado la lista 'audiencias', que contiene edicion y share. No ha habido errores.")
        print("------------------------------------------------------------------------\n")
        return audiencias
  except IOError:
      print("Error de entrada de datos...")
      sys.exit()

AUDIENCIASGH = lee_audiencias('csv/gh.csv')
print("Las audiencias serían ", AUDIENCIASGH[:20],"\n")
print("--------------------------------------------------------------------\n")
# EJ 2.
# * Calcular lista con distintas ediciones del programa presentes en los datos de entrada
# * Seleccionar los datos de audiencia de unas ediciones determiandas
# * Calcular las medidas de share por edición.

def calcula_ediciones(audiencias):
    ediciones = [e for e, _ in audiencias]
    print("Lista de tuplas con edición y share, ", ediciones)
    print("--------------------------------------------------------------------\n")
    ediciones = set(ediciones)
    print("Se transforma en conjunto con set(), eliminando los repetidos ", ediciones)
    print("--------------------------------------------------------------------\n")
    ediciones = list(ediciones)
    print("Convertimos el conjunto en lista con list() para poder ordenarlo ", ediciones)
    print("--------------------------------------------------------------------\n")
    ediciones.sort()
    print("Una vez ordenado, tenemos... ", ediciones)
    print("--------------------------------------------------------------------\n")
    return ediciones

ediciones = calcula_ediciones(AUDIENCIASGH)
print("Las ediciones serian ", ediciones,"\n")
print("--------------------------------------------------------------------\n")

def filtra_por_ediciones(audiencias, ediciones):
    # Devuelve una tupla cualquiera  (e,s) tal que e,s de la lista de tuplas AUDIENCIAS si e se encuentra en EDICIONES
    filtradas = [(e, s) for e,s in audiencias if e in ediciones]
    return filtradas

audiencias_123 = filtra_por_ediciones(AUDIENCIASGH, [1,2,3])
print("Las audiencias de las ediciones del 1 al 3 serían ", audiencias_123,"\n")
print("--------------------------------------------------------------------\n")

def medias_por_ediciones(audiencias):
    medias = dict()
    ediciones = calcula_ediciones(audiencias)
    for edicion in ediciones:
        shares = [s for e, s in audiencias if edicion == e]
        medias[edicion] = sum(shares) / len(shares)
    return medias

medias = medias_por_ediciones(AUDIENCIASGH)
print("Las medias serían ",medias,"\n")
print("--------------------------------------------------------------------\n")

# Funciones de visualización
def muestra_evolucion_audiencias(audiencias):
    shares = [s for _, s in audiencias]
    plt.plot(shares, label ='audiencia')
    plt.legend()
    plt.show()

muestra_evolucion_audiencias(AUDIENCIASGH) # Test de la función muestra_evolucion_audiencias

def muestra_medias_ediciones(audiencias):
    # Muestra un diagrama de barras con la media de audiencia por edicion
    ediciones = calcula_ediciones(audiencias)
    dicc_medias = medias_por_ediciones(audiencias)
    lista_medias = [dicc_medias[e] for e in ediciones]
    # Componemos y formamos la gráfica
    plt.bar(ediciones, lista_medias)
    plt.xticks(ediciones, ediciones, fontsize=8)
    plt.show()

muestra_medias_ediciones(AUDIENCIASGH)

# Para calcular la mediana, debemos saber que si nuestra lista tiene un número impar de elementos la mediana será la puntuación central
# y si tiene un número par será la media de las dos puntuaciones centrales.
# Calcularemos la longitud de la lista para comprobar esto.
def mediana(lista):
    index_lista = len(lista) / 2
    print(int(index_lista))
    if len(lista)%2 == 0:
        print(len(lista))
        print(lista[int(index_lista)])
        mediana_lista = lista[int(index_lista)] + lista[int(index_lista)+1]
        return mediana_lista
    else:
        mediana_lista = lista[index_lista]
        return mediana_lista

print(mediana(AUDIENCIASGH))


def calcula_estadisticos(audiencias):
# Calcula la media ,mediana, máximo y mínimo de una lista de audiencias
    pass

