def imprimirRecaudacionPorLinea (vectorLineas:list):
    for linea in range (len(vectorLineas)):
        print (f"La recaudacion de la linea {linea + 1} es de: {vectorLineas[linea]}")

def imprimirRecaudacionTotalPorLineas(vectorLineas:list):
    acumulador = 0
    for linea in range(len(vectorLineas)):
        acumulador += vectorLineas[linea]
    print (f"La recaudacion total de las lineas fue de {acumulador}")

def imprimirRecaudacionPorCoche (vectorCoche:list, coche: int):
    print (f"La recaudacion del coche {coche + 1} es de: ", end= " ")
    print (vectorCoche[coche])

def imprimirMatrizRecaudacion(matriz:list):
    for fila in range (len(matriz)):
        print(f"Linea: {fila+1} -> ", end= " ")
        for columna in range (len(matriz[0])):
            print(matriz[fila][columna], end=" ")
        print ("")

def imprimirMatrizLegajos(matriz:list):
    print ("Lista de legajos: ", end=" ")
    for fila in range (len(matriz)):
        for columna in range (len(matriz[0])):
            print(matriz[fila][columna], end=" ")
    print ("")
