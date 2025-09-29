def verificarRango (linea:int, lineasValidas: int) -> bool:
    valida=False
    if (linea < lineasValidas ) and (linea >= 0):
        valida=True
    return valida

def ingresoValido (ingreso: int, rangoValido:int) -> bool:
    lineaValida = verificarRango(ingreso, rangoValido)
    return lineaValida

def verificarLegajo (legajo:int, choferes:list) -> bool:
    valido = False
    for chofer in range (len(choferes)):
        if choferes[chofer][0] == legajo:
            valido = True
            break
    return valido

