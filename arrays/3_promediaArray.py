def promedioArray (array: list) -> int:
    promedio = 0
    for i in range (len(array)):
        promedio += array[i]
    promedio = promedio / len(array)
    return promedio


print (promedioArray([1,1,10,10,10]))