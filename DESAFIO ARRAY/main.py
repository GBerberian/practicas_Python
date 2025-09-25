vector = ["none"] * 10 
salida = True
bandera = True

def cargarVector (vector: list):
    for i in range(len(vector)):
        numero = int(input("Ingrese un numero entre -1000 y 1000: "))
        while (numero > 1000 or numero < -1000):
            numero = int(input("numero invalido, ingrese un numero entre -1000 y 1000: "))
        vector[i] = numero

def mostrarVector (vector: list):
    print (vector)

def cuentaPositivosNegativos (vector: list):
    positivos = 0
    negativos = 0
    for i in range (len(vector)):
        if vector[i] >= 0:
            positivos += 1
        else:
            negativos +=1
    print (f"Cantidad de numero positivos: {positivos}")
    print (f"Cantidad de numero negativos: {negativos}")

def sumaPares(vector: list):
    sumaTotal = 0
    for i in range (len(vector)):
        if vector[i] % 2 != 0:
            sumaTotal += vector[i]
    print (f"La suma total de los numeros pares es: {sumaTotal}")


def mayorImpar(vector: list):
    primerVuelta = True
    for i in range (len(vector)):
        if (vector[i] % 2 != 0) and (primerVuelta):
            mayorImpar = vector[i]
            primerVuelta =False
        elif (vector[i] % 2 != 0) and (not primerVuelta):
            if mayorImpar < vector[i]:
                mayorImpar = vector[i]
    if (primerVuelta):
        print ("No habia numeros impares")
    else: 
        print (f"El mayor numero impar es {mayorImpar}")

def esPar (numero: int):
    esPar = False
    if (numero % 2 == 0):
        esPar = True
    return esPar

def mostarPares (vector: list):
        for i in range (len(vector)):
            if esPar(vector):
                print (vector[i])


def mostrarImpares (vector: list):
        for i in range (len(vector)):
            if vector[i] % 2 != 0:
                print (vector[i])



while (salida):
    opciones = input("Ingrese una opcion: \n " 
    "1: Cargar el arreglo \n " 
    "2: Ver Cantidad positivos y negativos \n " 
    "3: Suma de los numeros pares \n " 
    "4: Mayor numero impar \n " 
    "5: Lista de los numeros ingresados \n " 
    "6: Listar los numeros pares \n " 
    "7: Listar los numeros impares \n "
    "8: Salir  \n" 
    "=>: ")
    while (opciones != "1" or opciones != "8" and bandera):
        opciones = input("En el primer ingreso, solo valido 1 u 8: ")
        if (opciones == "1" or opciones == "8"):
            bandera = False
    match opciones:
        case "1":
            cargarVector(vector)
        case "2":
            cuentaPositivosNegativos(vector)
        case "3":
            sumaPares(vector)
        case "4":
            mayorImpar(vector)
        case "5":
            mostrarVector(vector)
        case "6":
            mostarPares(vector)
        case "7":
            mostrarImpares(vector)
        case "8":
            salida = False
    


