#funcion de generar un numero aleatorio del 1 al 100
import random

def generar_numero_aleatorio():
    resultado =  random.randint(1, 100)
    return resultado
print(generar_numero_aleatorio())


#funcion de imprimir fecha actual
import datetime

def obtener_fecha_actual():
    fecha_actual = datetime.datetime.now()
    return fecha_actual.strftime("%d/%m/%Y")

print(obtener_fecha_actual())

# funcion de imprimir un mensaje ingresado por el usuario 
def imprimir_mensaje():
    msj = input("Ingrese un mensaje: ")
    return msj

print(imprimir_mensaje())

#funcion hora actual
import datetime

def obtener_hora_actual():
    hora_actual = datetime.datetime.now().time()
    return hora_actual
print(obtener_hora_actual())

#multiplicar numeros
def sumar_numeros():
    x = int(input("Ingrese un numero: "))
    y = int(input("Ingrese numero para sumar al anterior: "))
    resultado = x + y
    return resultado

print((sumar_numeros)())

##correccion funcion5: 
#Función sumar_numeros:
#Hay un error en la llamada a la función sumar_numeros. 
#Debes eliminar los paréntesis adicionales alrededor de sumar_numeros.
#Además, puedes cambiar el nombre de la función a multiplicar_numeros para
#que sea más coherente con la descripción.

def multiplicar_numeros():
    x = int(input("Ingrese un número: "))
    y = int(input("Ingrese un número para multiplicarlo por el anterior: "))
    resultado = x * y
    return resultado

print(multiplicar_numeros())




