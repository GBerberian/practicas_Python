from inputValido import identificarse, ingresarLineaCocheValido, recaudacionValida
from imprimir import imprimirMatrizRecaudacion,imprimirRecaudacionPorCoche,imprimirRecaudacionPorLinea,imprimirRecaudacionTotalPorLineas,imprimirMatrizLegajos
from especificas import actualizarRecaudaciones,inicializarLegajos

choferes = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15]]
empresa = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
vectorLineas = [0,0,0]
vectorCoches = [0,0,0,0,0]
salida = False


choferes = inicializarLegajos(15) 
imprimirMatrizLegajos(choferes)
legajoValido = identificarse(choferes)
while (not salida):
    opcion = int(input("Ingrese una opcion: \n " 
    "1: Cargar planilla recaudacion \n " 
    "2: Mostrar la recaudacion por cada coche y linea \n " 
    "3: Calcular y mostrar recaudacion por linea\n " 
    "4: Calcular y mostrar la recaucacion por coche\n " 
    "5: Calcular y mostrar la recaudacion total\n " 
    "6: Salir del programa \n " 
    "=>: "))
    match opcion:
        case 1:
            linea = ingresarLineaCocheValido(empresa,"Ingrese una linea valida: 1, 2 o 3: ")
            coche = ingresarLineaCocheValido(empresa,"Ingrese un coche valido: 1, 2, 3, 4, 5: ")
            recaudacion = recaudacionValida()
            actualizarRecaudaciones(empresa,linea,coche, recaudacion,vectorLineas,vectorCoches)
        case 2:
            imprimirMatrizRecaudacion(empresa)
        case 3:
            imprimirRecaudacionPorLinea(vectorLineas)
        case 4:
            coche = ingresarLineaCocheValido(empresa,"Ingrese el coche del cual desea ver su recaudacion: ")
            imprimirRecaudacionPorCoche(empresa,coche)
        case 5:
            imprimirRecaudacionTotalPorLineas(vectorLineas)
        case 6:
            salida = True
        case _:
            print ("Ingreso invalido!")

