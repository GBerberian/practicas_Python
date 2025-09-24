from validate import numeroEnRangoValido, longitudValida

def get_int (mensaje:str , mensaje_error: str, minimo: int, maximo:int , reintentos: int) -> int|None:
    ingreso = int(input(mensaje))
    numeroEnRango = numeroEnRangoValido(minimo,maximo, ingreso)
    reintentos -= 1
    while (reintentos > 0 and not numeroEnRango):
        print(mensaje_error)
        ingreso = int(input(f"Numero invalido, ingrese un numero dentro del rango {minimo} - {maximo}. Intentos restantes {reintentos}: ")) 
        numeroEnRango = numeroEnRangoValido(minimo,maximo,ingreso)
        if (not numeroEnRango):
            ingreso = None
        reintentos -= 1
    return ingreso


def get_float(mensaje:str , mensaje_error: str, minimo: int, maximo:int , reintentos: int) -> float|None:
    ingreso = float(input(mensaje))
    numeroEnRango = numeroEnRangoValido(minimo,maximo, ingreso)
    reintentos -= 1
    while (reintentos > 0 and not numeroEnRango):
        print(mensaje_error)
        ingreso = float(input(f"Numero invalido, ingrese un numero dentro del rango {minimo} - {maximo}. Intentos restantes {reintentos}: ")) 
        numeroEnRango = numeroEnRangoValido(minimo,maximo,ingreso)
        if (not numeroEnRango):
            ingreso = None
        reintentos -= 1
    return ingreso



def get_string (longitud: int) -> str|None:
    mensaje = str(input(f"Ingrese el mensaje que quiere para la funcion: la longitud no debe superar los {longitud} caracteres: "))
    while (not longitudValida(longitud, len(mensaje))):
        mensaje = str(input(f"Mensaje invalido. longitud maxima {longitud} caracteres: "))
    return mensaje