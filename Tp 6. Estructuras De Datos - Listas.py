# Trabajo Práctico 6

# Ejercicio 1

"""
numA = int(input("Ingrese el primer número: "))
numB = int(input("Ingrese el segundo número, para determinar el rango de valores validos: "))
vecNumeros = [] 

print()
numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

if numA < numB :
    while (numero < numA or numero > numB) and numero != -1 :
        print()
        print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
        numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

elif numA == numB :
    while (numero != numA or numero != numB) and numero != -1 :
        print()
        print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
        numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

else :
    while (numero > numA or numero < numB) and numero != -1 :
        print()
        print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
        numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))


while numero != -1 :
    vecNumeros.append(numero)
    numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

    if numA < numB :
        while (numero < numA or numero > numB) and numero != -1 :
            print()
            print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
            numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

    elif numA == numB :
        while (numero != numA or numero != numB) and numero != -1 :
            print()
            print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
            numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

    else :
        while (numero > numA or numero < numB) and numero != -1 :
            print()
            print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
            numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))


largo = len(vecNumeros)
if largo <= 0 :
    print("No se han ingresado números a la lista")

else :
    print("La lista de números es:",vecNumeros)

"""

# Ejercicio 2

numA = int(input("Ingrese el primer número: "))
numB = int(input("Ingrese el segundo número, para determinar el rango de valores validos: "))
vecNumeros = [] 
suma = 0

print()
numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

if numA < numB :
    while (numero < numA or numero > numB) and numero != -1 :
        print()
        print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
        numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

elif numA == numB :
    while (numero != numA or numero != numB) and numero != -1 :
        print()
        print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
        numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

else :
    while (numero > numA or numero < numB) and numero != -1 :
        print()
        print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
        numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))


while numero != -1 :
    suma += numero
    vecNumeros.append(numero)
    numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

    
    if numA < numB :
        while (numero < numA or numero > numB) and numero != -1 :
            print()
            print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
            numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

    elif numA == numB :
        while (numero != numA or numero != numB) and numero != -1 :
            print()
            print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
            numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

    else :
        while (numero > numA or numero < numB) and numero != -1 :
            print()
            print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
            numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

largo = len(vecNumeros)
if largo <= 0 :
    print("No se han ingresado números a la lista")

else :
    print("La suma de la lista de números es:",suma)



