#Muestra por pantalla lenguaje favorito predeterminado
def fav_lenguaje(lenguaje="Python"):
    favorito = ("Mi lenguaje favorito de programación es " + lenguaje)
    return favorito
print(fav_lenguaje())


#saludo con dos variables predeterminadas
def saludar(nombre="amigo", mensaje="Hola"):
    saludo = (mensaje + ", " + nombre + "!")
    return saludo
print(saludar())


#sumar dos numeros con un valor predeterminado
def sumar_numeros(num1, num2=4):
    resultado = num1 + num2
    return resultado

print(sumar_numeros(2))

#Saluda predeterminado
def saludar(nombre, saludo="Hola"):
    accion = (saludo + ", " + nombre + "!")
    return accion
print(saludar("Matias"))

# Función que devuelve una lista con los primeros n números pares
def obtener_numeros_pares(n, inicio=0):
    numeros = []
    for i in range(inicio, inicio + 2*n, 2):
        numeros.append(i)
    return numeros

print(obtener_numeros_pares(5))