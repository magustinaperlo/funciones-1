# funciones con parametros
#suma de dos numeros
def suma(a,b):
    resultado = a + b
    return resultado

print(suma(10,5))

#cociente
def division(d,e):
    if (e == 0):
        print("No se puede dividir por cero")
    else:
        cociente = (d/e) 
    return cociente

print(division(10,5))

#cual es el mayor de dos numeros
def mayor(f,g):
    if (f > g):
        print("El mayor es: " + str(f))
    if (g > f):
        print("El mayor es " + str(g))
    if (g == f):
        print("Nnguno es mayor")
    return mayor

print(mayor(9,400))

#numero par o impar
def par(h):
    if h % 2 == 0:
        print("El numero es par")
    else: 
        print("El numero es impar")
    return par

print(par(2))

#mayor de un vector
def mayor_vector(vec):
    for i in range(0, len(vec)):
        if (i == 0):
            mayor = vec[i]
        if (vec[i] > mayor):
            mayor = vec[i]
    return mayor

vec = [2,3,1,900]

print(mayor_vector(vec))
  
