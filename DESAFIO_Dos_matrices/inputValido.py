from validaciones import ingresoValido,verificarLegajo

def recaudacionValida () -> int:
    recaudacionValida = False
    while (not recaudacionValida):
        recaudacion = int(input("Ingrese la recaudacion del colectivo: "))
        if (recaudacion >= 0):
            recaudacionValida=True
    return recaudacion


def ingresarLineaCocheValido(empresa: list,texto:str) -> int:
    esValido = False
    while (not esValido):
        ingreso = int(input(texto))
        ingreso -=1
        esValido = ingresoValido(ingreso, len(empresa))
    return ingreso

def identificarse(choferes:list) ->int:
    legajoValido = False
    while (not legajoValido):
        legajo = int(input("Ingrese un legajo valido: "))
        legajoValido = verificarLegajo(legajo,choferes)
    return legajo
