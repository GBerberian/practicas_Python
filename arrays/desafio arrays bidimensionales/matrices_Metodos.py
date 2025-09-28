from vectores_Metodos import *
import random


def matrizCargaManual(orden:int, matriz:list) -> list:
    numerosDisponibles = crearVectorAuxiliar(len(matriz[0]))
    for fila in range (len(matriz)):
        for columna in range (len(matriz[0])):
            numero = inputNumeroValido(numerosDisponibles)
            actualizarVector(numero, numerosDisponibles)
            matriz[fila][columna] = numero
    return matriz

def matrizAleatoria(orden:int ,matriz: list) ->list:
    posAuxiliar = 0
    numeros = random.sample(range(1, orden**2 + 1),  orden**2)
    for fila in range (len(matriz)):
        for columna in range (len(matriz[0])):
            matriz[fila][columna] = numeros[posAuxiliar]
            posAuxiliar +=1
    return matriz

    

def iniciarMatriz(orden:int) -> list|None:
    matriz = crearMatrizCuadrada(orden)
    ingreso = int(input("Que tipo de carga desea para su matriz Opcion 1: Manual - Opcion 2: Aleatoria: "))
    while (ingreso != 1 and ingreso != 2):
        ingreso = int(input("Ingerso invalido. Opcion 1: Manual - Opcion 2: Aleatoria: "))
    match ingreso:
        case 1:
            matriz = matrizCargaManual(orden,matriz)
        case 2:
            matriz = matrizAleatoria(orden,matriz)
        case _:
            matriz = None
    return matriz


def crearMatrizCuadrada (orden:int) -> list:
    matriz = []
    for i in range (orden):
        fila = [0] * orden
        matriz += [fila]
    return matriz

def imprimirMatriz(matriz:list):
    for fila in range (len(matriz)):
        for columna in range (len(matriz[0])):
            print(matriz[fila][columna], end=" ")
        print ("")


