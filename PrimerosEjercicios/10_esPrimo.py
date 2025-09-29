def esPrimo (numero:int) -> bool:
    primo = True
    for i in range (1,numero):
        if i != 1:
            if numero % i == 0:
                primo = False
                break
    return primo

for i in range (1,10):
    print (f"el numero {i} {esPrimo(i)}")