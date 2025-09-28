from validacionesCuadrado import *


def calcularConstanteMagica(orden: int) -> int:
    constante = orden*(orden**2 + 1) // 2
    return constante


def comprobarCuadradoMagico (matriz: list) -> bool:
    constaneMagica = calcularConstanteMagica(len(matriz[0]))
    esCuadradoMagico = False
    filasValidas = chequearFilas(matriz, constaneMagica)
    if (filasValidas):
        chequeaColumnas = chequearColumnas(matriz, constaneMagica)
        if (chequeaColumnas):
            chequeaDiagonales = chequearDiagonales(matriz, constaneMagica)
            if (chequeaDiagonales):
                esCuadradoMagico = True
    return esCuadradoMagico
    


