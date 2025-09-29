import random

def actualizarRecaudaciones (empresa:list, linea:int, coche:int, recaudacion:int, vectorLineas: list, vectorCoches:list):
    empresa[linea][coche] += recaudacion
    vectorCoches[coche] += recaudacion
    vectorLineas[linea] += recaudacion


def inicializarLegajos(rango:int) -> list:
    matriz = []
    vectorLegajos = random.sample(range(10, 100), 15)
    for i in range (rango):
        fila = [vectorLegajos[i]] * 1
        matriz += [fila]
    return matriz