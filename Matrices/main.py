matriz = [[2,1],[-3,4]]

constante = 3


def matriz_Por_K (matriz: list, constante: int) -> list:
    for fila in range (len(matriz[0])):
        for columna in range (len(matriz)):
            matriz[fila][columna] *= constante
    return matriz

def imprimirMatriz(matriz: list):
    for fila in range (len(matriz)):
        for columna in range (len(matriz[fila])):
            print (matriz[fila][columna],)
        print ("")

nuevaMatriz = matriz_Por_K(matriz, constante)
imprimirMatriz(nuevaMatriz)