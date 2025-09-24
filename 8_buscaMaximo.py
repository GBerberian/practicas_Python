def buscaMaximos (num1: int,num2: int,num3: int):
    mayor = num1
    if num1 != num2:
        if num2 > num1:
            mayor = num2
    if mayor != num3:
        if mayor < num3:
            mayor = num3
    return mayor


print (buscaMaximos(10,10,64))