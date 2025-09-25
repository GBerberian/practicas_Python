from arrayPorParametro import crearArray


def arrayPorTeclado () -> list:
    tamanio = int(input("Ingrese el tamanio del array: "))
    array = crearArray(tamanio)
    for i in range (len(array)):
        numero = int(input("Ingrese un numero para su array: "))
        array[i] = numero
    return array


print(arrayPorTeclado())