def validarPar (numero:int) -> bool:
    esPar = False
    if numero%2 == 0:
        esPar = True
    return esPar


def textoParImpar (numero:int) -> str:
    if (validarPar(numero)):
        texto = f"El numero {numero} es par"
    else:
        texto = f"El numero {numero} es impar"
    return texto


numero = 10
for i in range (numero):
    print (textoParImpar(i))