def crearVectorAuxiliar(size: int) -> list:
    vector = [None] * (size*size)
    cargarVectorfrom1toN(vector)
    return vector
    
def cargarVectorfrom1toN(vector: list) -> list:
    for i in range (len(vector)):
        vector[i] = i+1
    return vector

def mostrarNumerosDisponibles(vector: list):
    for i in range (len(vector)):
        if vector[i] != None:
            print (vector[i], end=" ")
    print ("")

def inputNumeroValido( disponibles: list):
    numeroDisponible = False
    while (not numeroDisponible):
        mostrarNumerosDisponibles(disponibles)
        numero = int(input(f"Ingrese un numero valido: "))
        if numero <= 0 or numero>len(disponibles):
            print (f"El numero no puede ser menor a 0 o mayor a {len(disponibles)}: ")
        else:
            if disponibles[numero-1] != None:
                numeroDisponible = True
    return numero

def actualizarVector(numero: int, vector:list):
    vector[numero-1] = None


