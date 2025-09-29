def validarParBool (numero:int) -> bool:
    esPar = False
    if numero%2 == 0:
        esPar = True
    return esPar


numero = 11

print (validarParBool(numero))