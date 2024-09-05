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



# Ejercicio 6

numero = 4
i = 1

print("La tabla del 4 es: ")
while i <= 12 :
    print(numero, "*",i,"=",numero*i)
    i+=1

# Otra forma para que yo decida el numero de la tabla
    
numero = int(input("Ingrese el número de la tabla que quiera resolver: "))
i = 1

print("La tabla del",numero,"es: ")
while i <= 12 :
    print(numero, "*",i,"=",numero*i)
    i+=1



# Ejercicio 7
contador = 0
acumulador = 0
numMayor = -9999

for i in range(1,11) :
    numero = int(input("Ingrese un numero: "))
    contador += 1
    acumulador += numero

    if numero > numMayor :
        numMayor = numero
        posMayor = i

promedio = acumulador / contador
print(" ")
print("El promedio de los datos ingresados es:",promedio)
print("El número ingresado mas grande es:",numMayor)
print("La posicion en la que se encuentra el número mas grande es:",posMayor)



# Ejercicio 8

acumulador = 0
contador = 0

while acumulador <= 100 :
    numero = int(input("Ingrese un número: "))

    if numero % 2 == 0:
        acumulador += numero 
        print(acumulador)  
    contador += 1
    
print("Para que la suma de los números pares llegue a 100, se ingresaron: ",contador,"números")

"""
# Ejercicio 9
numPatente = 0
contadorPar = 0
contadorImpar = 0

while numPatente != -1 :
    numPatente = int(input("Ingrese el número de la patente: "))
    while numPatente !=-1 and (numPatente <0 or numPatente > 9) :
        print("ERROR, la terminación de la patente debe estar entre 0 y 9")
        
        if numPatente % 2 == 0 :
            contadorPar += 1
        
        else: 
            contadorImpar += 1

print("Al final del día, han pasado:",contadorPar,"vehiculos con la patente con numeración par y",contadorImpar,"vehiculos con la patente con numeración impar")
