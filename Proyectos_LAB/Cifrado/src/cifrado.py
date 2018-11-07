# -*- coding: utf-8 -*-
'''
Cifrado y descifrado por el método César

AUTOR: Carlos G. Vallejo
REVISOR: Fermín Cruz, José A. Troyano
ÚLTIMA MODIFICACIÓN: 30/10/2018

La criptografía es el proceso de oscurecer la información para hacerla ilegible
si no se tiene cierta información especial. Durante siglos se han estado
desarrollando esquemas para encriptar (cifrar) mensajes – unos mejores que
otros – pero la llegada de los ordenadores e internet ha revolucionado este
campo. Actualmente es difícil no encontrar algún tipo de encriptación en muchos
aspectos de nuestras vidas. La encriptación nos permite compartir información
con otras personas o entidades de confianza sin temor a que sea revelada.

Un cifrado es un algoritmo para ejecutar la encriptación (cifrar) y la inversa,
la desencriptación (descrifrar). La información original se denomina texto
plano. Después de que es encriptado, se denomina texto crifrado. El texto
cifrado contiene toda la información del texto plano, pero no está en un
formato legible por un humano o un ordenador si no se dispone del mecanismo
adecuado para descifrarlo; debe parecer texto aleatorio para aquellos a los
que no está destinado.

Un cifrado normalmente depende de una pieza de información adicional,
denominada clave. La clave es incorporado en el proceso de cifrado; el mismo
texto plano cifrado con dos claves diferentes debe tener dos textos cifrados
diferentes. Sin la clave debería ser difícil descifrar el texto cifrado para
obtener el texto plano.

Aquí se va a tratar con un método de cifrado muy bien conocido (aunque nada
seguro) denominado el Cifrado César
(https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar).

El Cifrado César
La idea del Cifrado César es tomar un entero y desplazar (shift) cada letra
del mensaje por ese entero. En otras palabras, supóngase que el desplazamiento
es k. Todas las instancias de la i-ésima letra del alfabeto que aparezca en el
texto plano debe convertirse en la (i + k) letra del alfabeto en el texto
cifrado. Hay que ser cuidadoso con el caso en el que i + k supere el número
total de letras del alfabeto. En lo que sigue vamos a considerar exclusivamente
el código ASCII básico, sin tildes ni diéresis, ni la letra eñe. De este modo
la longitud del alfabeto es 26. Así es como se vería el alfabeto si se desplaza
tres lugares hacia la derecha:

Original:  a b c d e f g h i j k l m n o p q r s t u v w x y z
 3-shift:  d e f g h i j k l m n o p q r s t u v w x y z a b c

Usando la clave anterior, podemos traducir rápidamente el mensaje “feliz” en
“iholc” (obsérvese cómo se comporta el desplazamiento en las letras finales,
de modo que w → z, x → a, y → b y z → c).

Las letras con tildes y eñes se dejarán igual al cifrar y, naturalmente, al
descifrar. Las mayúsculas se dejarán mayúsculas y las minúsculas, minúsculas.

El vocabulario de palabras en español lo obtendrémos de un fichero
de texto plano, en el que cada línea contiene una palabra válida.

FUNCIONES DISPONIBLES:
----------------------
- carga_vocabulario(fichero):
    lee el fichero y devuelve un conjunto de cadenas
- es_palabra_valida(palabra, vocabulario):
    comprueba si la palabra está en el vocabulario y devuelve un booleano
- construye_diccionario_codificacion(desplazamiento):
    devuelve un diccionario con el que se va a cifrar/descifrar
- aplica_cifrado(texto, desplazamiento):
    aplica el diccionario de cifrado a un texto
- cuenta_palabras(texto, vocabulario):
    cuenta el número de palabras de un vocabulario presentes en un texto
- descifra_mensaje(texto, vocabulario):
    descifra un texto usando el vocabulario
'''
import string

# EJERCICIO 1:
def carga_vocabulario(fichero):
    ''' Lee el fichero y devuelve un conjunto de cadenas
    
    ENTRADA: 
       - fichero: nombre del fichero donde se encuentra el vocabulario -> str 
    SALIDA: 
       - lista de palabras -> [str)]

    Carga las palabras contenidas en el 'fichero'; en el archivo es.dic
    cada línea representa una palabra válida del castellano; contiene 292342
    palabras, recopiladas por Juan Luis Varona, de la Universidad de La Rioja.
    Las palabras están todas en minúsculas, y contienen tildes y diéresis.
    La función devolverá un conjunto formado por las palabras del fichero.
    Para eliminar el salto de línea ('\n') al final de las cadenas podemos
    usar el método strip de las cadenas.
    '''
    pass


# EJERCICIO 2:
def es_palabra_valida(palabra, vocabulario):
    ''' Comprueba si la palabra está en el vocabulario y devuelve un booleano
    
    ENTRADA: 
       - palabra: que será buscada en el vocabulario -> str
       - volcabulario: lista de palabras del vocabulario -> [str] 
    SALIDA: 
       - pertenencia o no al vocabulario -> bool
    
    Recibe una palabra y el vocabulario de palabras válidas en español,
    y devuelve un booleano indicando si la palabra está en el vocabulario o no.
    Para ello, la pasaremos a minúsculas y eliminaremos todos los signos de
    puntuación que pueda llevar al principio o al final, como comas, abre o
    cierra paréntesis o admiración, etc. Los símbolos a eliminar son:
        " !@#$%^&*()-_+={}[]|\:;'<>?,./\"¡¿"
    '''
    pass


# EJERCICIO 3:
def construye_diccionario_codificacion(desplazamiento):
    ''' Devuelve un diccionario con el que se va a cifrar/descifrar
    
    ENTRADA: 
       - desplazamiento: número de posiciones a desplazar al codificar -> int
    SALIDA: 
       - diccionario con la codificación de cada letra mayúscula o minúscula -> {str: str}
    
    Recibe un desplazamiento, que es un número entero, y devuelve un
    diccionario que hace corresponder a cada letra (minúscula o mayúscula) otra
    letra (minúscula o mayúscula como la anterior), que está desplazamiento
    lugares más adelante en el alfabeto. Si el lugar resultante es posterior al
    último, volveremos por el principio.
    
    Para resolver el ejercicio, calcularemos las siguientes variables:
      - minusculas: lista con todas las letras minúsculas (¿qué función ofrece Python?)
      - mayusculas: lista con todas las letras mayúsculas en el mismo orden
      - numero_letras: tamaño de la lista de letras minúsculas
      - nuevas_posiciones: lista con las nuevas posiciones calculada para cada 
        posición 'i' con la siguiente fórmula:
               (i + desplazamiento) % numero_letras
      - codificacion_min: diccionario con la codificación de las letras minúsculas
      - codificacion_may: diccionario con la codificación de las letras mayúsculas
      - codificacion: mezcla de los anteriores diccionarios     
    '''
    pass


# EJERCICIO 4:
def aplica_cifrado(texto, desplazamiento):
    ''' Aplica el diccionario de cifrado a un texto
    
    ENTRADA: 
       - texto: texto a codificar -> str
       - desplazamiento: número de posiciones a desplazar al codificar -> int
    SALIDA: 
       - texto codificado -> str
    
    Aplica el cifrado César al parámetro texto con el desplazamiento indicado.
    Para ello, crea un vocabulario de codificación con el desplazamiento
    indicado y aplica ese desplazamiento a cada uno de los caracteres del texto
    que sean ascii puro (string.ascii_letters) omitiendo los caracteres de
    puntuación pero también las vocales con tilde o diéresis y la eñe.
    Devuelve el mensaje codificado con ese desplazamiento.
    
    Para resolver el ejercicio, calcularemos las siguientes variables:
      - codificacion: diccionario calculado con la función 'construye_diccionario_codificacion'
      - texto_cifrado: lista con las nuevas letras tras aplicar la codificación al texto. Si una
        letra no aparece en el diccionario se mantiene la letra original (usar el método get 
        de los diccionarios) 
    '''
    pass


# EJERCICIO 5:
def cuenta_palabras(texto, vocabulario):
    ''' Cuenta el número de palabras de un vocabulario presentes en un texto
    
    ENTRADA: 
       - texto: texto en el que se buscarán palabras -> str
       - volcabulario: lista de palabras del vocabulario -> [str] 
    SALIDA: 
       - número de palabras encontradas -> int
    
    Para resolver el ejercicio, calcularemos las siguientes variables:
      - tokens: secuencias de caracteres que aparecen separadas por espacios, de las
        que se quitan los símbolos de puntuación " !@#$%^&*()-_+={}[]|\:;'<>?,./\"¡¿"
      - palabras: solo se mantienten los tokens que aparecen en el vocabulario 
    '''
    pass


# EJERCICIO 6:
def descifra_mensaje(texto, vocabulario):
    ''' Descifra un texto usando el vocabulario
    
    ENTRADA: 
       - texto: texto en el que se buscarán palabras -> str
       - volcabulario: lista de palabras del vocabulario -> [str] 
    SALIDA: 
       - mejor desplazamiento posible -> int
       - texto descrifrado con el mejor desplazamiento -> str
    
    Recibe un texto, que ha sido codificado con un desplazamiento que ignoramos,
    y el vocabulario de palabras válidas en español, y devuelve una tupla
    formada por el desplazamiento que ha sido necesario para decodificar y el
    texto decodificado.
    Para resolver el ejercicio, calcularemos las siguientes variables:
      - posibles_desplazamientos: rango de valores de 0 a número de letras menos 1
      - aciertos: diccionario en el que a cada posible desplazamiento se le asocia
        el número de palabras que contiene el cifrado del texto con dicho
        desplazamiento
    La entrada del diccionario que contenga el número de aciertos mayor se
    corresponderá con el mejor desplazamiento posible.
    '''
    pass