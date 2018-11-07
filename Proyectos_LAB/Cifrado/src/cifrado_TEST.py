# -*- coding: utf-8 -*-

from cifrado import *

################################################################
#  Funciones de test
################################################################
def test_es_palabra_valida():
    print('\nSalida esperada:\nhola: True\nxyz: False\n')
    print('hola:', es_palabra_valida('hola', VOCABULARIO))
    print('xyz:', es_palabra_valida('xyz', VOCABULARIO))


def test_construye_diccionario_codificacion():
    codificacion = construye_diccionario_codificacion(10)
    print('\nSalida esperada:\na -> k\nF -> P\n')
    print('a ->', codificacion['a'])
    print('F ->', codificacion['F'])


def test_aplica_cifrado():
    texto_cifrado = aplica_cifrado('Programación', 24)
    print('\nSalida esperada: Npmepykyagól')
    print('Salida real:', texto_cifrado)


def test_cuenta_palabras():
    print('\nSalida esperada: 4\n')
    print(cuenta_palabras('Aquí hay cuatro palabras xxx hatat fff', VOCABULARIO))


def test_descifra_mensaje():
    texto_descifrado = descifra_mensaje("Npmepykyagól", VOCABULARIO)
    print('\nSalida esperada:', (2, 'Programación'))
    print('Salida real:', texto_descifrado)
    
    with open("../data/historia.txt", encoding='utf-8') as f:
        historia_cifrada = f.read()
    desplazamiento, historia = descifra_mensaje(historia_cifrada, VOCABULARIO)
    print("\nMejor desplazamiento para historia.txt: ", desplazamiento)
    print("Historia descifrada:\n" + historia)


################################################################
#  Programa principal
################################################################
VOCABULARIO = carga_vocabulario('../data/es.dic')
print('Hay {} palabras en el vocabulario'.format(len(VOCABULARIO)))
print(list(VOCABULARIO)[:10])

#test_es_palabra_valida()
#test_construye_diccionario_codificacion()
#test_aplica_cifrado()
#test_cuenta_palabras()
#test_descifra_mensaje()
