def  chequearFilas(matriz: list, constaneMagica: int) -> bool:
    sumaValida = True
    auxiliar = 0
    for fila in range (len(matriz)):
        for columna in range (len(matriz[0])):
            auxiliar += matriz[fila][columna]
        if auxiliar != constaneMagica:
            sumaValida = False
            break
        auxiliar = 0
    return sumaValida


def  chequearColumnas(matriz: list, constaneMagica: int) -> bool:
    sumaValida = True
    auxiliar = 0
    for columna in range (len(matriz)):
        for fila in range (len(matriz[0])):
            auxiliar += matriz[fila][columna]
        if auxiliar != constaneMagica:
            sumaValida = False
            break
        auxiliar = 0
    return sumaValida

def  chequearDiagonales(matriz: list, constaneMagica: int) -> bool:
    sumaValida = True
    auxiliar = 0
    for posDiagonal in range (len(matriz[0])):
        auxiliar += matriz[posDiagonal][posDiagonal]
    if auxiliar != constaneMagica:
        sumaValida = False
    auxiliar = 0
    if (sumaValida):
        iteradorFila=0
        for posDiagonal in range (len(matriz[0]) -1, -1, -1):
            posDiagonal 
            auxiliar += matriz[iteradorFila][posDiagonal]
            iteradorFila +=1
        if auxiliar != constaneMagica:
            sumaValida = False
    return sumaValida
