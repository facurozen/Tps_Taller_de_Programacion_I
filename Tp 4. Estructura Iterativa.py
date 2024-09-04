# Trabajo Práctico 4

# Ejercicio 1

"""
numero = int(input("Ingrese un número: "))

primerValor = numero

while numero != -1 :
    numero = int(input("Ingrese un número: "))
    if numero != -1 :
        ultimoValor = numero
   
print("El primer valor ingresado fue:",primerValor)
print("El ultimo valor ingresado fue:",ultimoValor)


# Ejercicio 2

numero = int(input("Ingrese un número: "))



# Ejercicio 3

numero = int(input("Ingrese un número: "))
numMayor = numero
numMenor = numero

while numero != -1 :
    numero = int(input("Ingrese un número: "))

    if numero != -1 :
        if numero > numMayor :
            numMayor = numero

        elif numero < numMenor :
            numMenor = numero

print("El número mayor del conjunto de numeros que ingresaste fue:",numMayor)
print("El número menor del conjunto de numeros que ingresaste fue:",numMenor)



# Ejercicio 4

suma = 0

for i in range(42,177) :
    if i % 2 != 0 :
        suma += i

print("La suma de todos los numeros impares comprendidos entre 42 y 176 es:",suma)



# Ejercicio 5

n = int(input("Ingrese un número: "))
i = 1
while i <= n :
    print(i)
    i+=1

# OTRA FORMA DE REALIZARLO CON FOR

n = int(input("Ingrese un número: "))

for i in range (1,n+1) :
    print(i)

"""

# Ejercicio 6

numero = 4
i = 1

print("La tabla del 4 es: ")
while i <= 12 :
    print(numero "*"i,"=",numero*i)
    i+=1