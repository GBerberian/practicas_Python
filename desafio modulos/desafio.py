from input import get_float,get_int,get_string

mensaje = "Ingrese un numero: "
mensaje_error = "El numero ingresado no es valido, intente nuevamente"
min = 0
max = 100
intentos = 3

print (get_string(10))
print (get_int(mensaje,mensaje_error, min, max, intentos))
print (get_float("Ingrese un flotante: ", "Error! Vuelva a intentarlo", 0,100,3))