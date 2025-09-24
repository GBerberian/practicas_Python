def numeroEnRangoValido (minimo:float|int, maximo:float|int, numero:float|int) -> bool:
    valido = False
    if (numero>= minimo and numero<=maximo):
        valido=True
    return valido 



def longitudValida(longitud: int, tamanioCadena: int) -> bool:
    esValida = True
    if longitud < tamanioCadena:
        esValida = False
    return esValida