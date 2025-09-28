from matrices_Metodos import imprimirMatriz, crearMatrizCuadrada,iniciarMatriz
from cuadradoMagico import comprobarCuadradoMagico


cuadradoMagicoN3 = [[8,1,6],[3,5,7],[4,9,2]]

#Declare esa funcion aca solo por comodidad y para no crear un modulo de pantalla 
def mensaje (bandera: bool):
    if bandera:
        print (f"\nLa matriz que usted ingreso es un cuadrado magico")
    else:
        print (f"\nLa matriz que usted ingreso no es un cuadrado magico")




matriz = iniciarMatriz(3) #parametro = orden de la matriz. Ejemplo 3 = matriz 3x3
print(f"\nLa matriz que usted cargo es la siguiente  \n")
imprimirMatriz(matriz) #Imprimir la matriz creada por el usuario, ya sea que se completo de manera manual o aleatoria
mensaje(comprobarCuadradoMagico(matriz))#Comprobar si la matriz creada por el usuario es cuadrado magico o no

print ("\nEl siguiente ejemplo es para comprobar como responde el programa con un caso verdadero. por lo que utilizamos de ejemplo la matriz: \n")
imprimirMatriz(cuadradoMagicoN3)
mensaje(comprobarCuadradoMagico(cuadradoMagicoN3)) #Mostrar un caso donde el cuadrado magico sea verdadero

