from random import *

def simple_list():
    # CREO LA LISTA Y RECORRO 10 veces
    list = []
    for x in range(10):
        dict = {}
        dict['id'] = x
        dict['age'] = randint(1, 100)  # NUMERO ALEATORIO DE 1 a 100
        list.append(dict)  # AGREGO A LA LISTA
    return list

def sort_list(dicts):
    return sorted(dicts, key=ordenar_edad_ascendente)  # UTILIZO SORTED

def ordenar_edad_ascendente(dicts):
    return dicts['age']

Lista = simple_list()
print(Lista)
ordenado_edad = sort_list(Lista)
print(ordenado_edad)

