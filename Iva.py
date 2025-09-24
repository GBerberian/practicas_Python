"""" FUCION QUE RECIBA UN NUMERO Y LE CALCULE EL IVA QUE POR DEFECTO ES 21 Y EN CASO DE PASAR POR PARAMETRO OTRO IVA LO CAMBIE """

def calcula_iva (precio, iva = 21):
    return precio + precio * (iva / 100)

print (calcula_iva (1000))