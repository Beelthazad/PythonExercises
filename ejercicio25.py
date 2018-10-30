# Convertir una lista de listas e nuna sola se denomina aplanamiento.
def aplanar(lista):
    return [y for x in lista for y in x]


lista_de_listas = [['u','n','o'],['d','o','s'],['t','r','e','s']]
print("Mediante nuestra función aplanar = ", aplanar(lista_de_listas))




