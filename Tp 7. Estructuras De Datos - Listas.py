# Trabajo Práctico 6

# Ejercicio 1


def ingresarNumerosLista(n1,n2) :
    numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))
    vecNumeros = [] 

    if n1 < n2 :
        while (numero < n1 or numero > n2) and numero != -1 :
            print()
            print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
            numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

    elif n1 == n1 :
        while (numero != n1 or numero != n2) and numero != -1 :
            print()
            print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
            numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

    else :
        while (numero > n1 or numero < n2) and numero != -1 :
            print()
            print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
            numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))


    while numero != -1 :
        vecNumeros.append(numero)
        numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

        if n1 < n2 :
            while (numero < n1 or numero > n2) and numero != -1 :
                print()
                print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
                numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

        elif n1 == n2 :
            while (numero != n1 or numero != n2) and numero != -1 :
                print()
                print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
                numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

        else :
            while (numero > n1 or numero < n2) and numero != -1 :
                print()
                print("ERROR. El número ingresado debe estar entre el primero y segundo. ")
                numero = float(input("Ingrese un número. El mismo debe estar dentro del rango de valores que hay entre ambos números. Para finalizar, ingrese -1: "))

    return vecNumeros

"""
numA = int(input("Ingrese el primer número: "))
numB = int(input("Ingrese el segundo número, para determinar el rango de valores validos: "))

vecNumeros = ingresarNumerosLista(numA,numB)
print()

largo = len(vecNumeros)
if largo <= 0 :
    print("No se han ingresado números a la lista")

else :
    print("La lista de números es:",vecNumeros)



# Ejercicio 2


numA = int(input("Ingrese el primer número: "))
numB = int(input("Ingrese el segundo número, para determinar el rango de valores validos: "))

vecNumeros = ingresarNumerosLista(numA,numB)
suma = 0

print()

largo = len(vecNumeros)
if largo <= 0 :
    print("No se han ingresado números a la lista")

else :
    for i in range(largo):
        suma+= vecNumeros[i]

print("La suma de la lista de números es:",suma)



# Ejercicio 3

# Ejercicio 4

def contarApariciones(vec,num) :
    largo = len(vec)
    contador = 0

    for i in range(largo) :
        if num == vec[i] :
            contador += 1

    return contador

numA = int(input("Ingrese el primer número: "))
numB = int(input("Ingrese el segundo número, para determinar el rango de valores validos: "))

vecNumeros = ingresarNumerosLista(numA,numB)

print()
num_a_buscar = float(input("Ingrese el valor que desea saber cuantas veces está en la lista: "))

print()
contadorApariciones = contarApariciones(vecNumeros,num_a_buscar)
print("El número",num_a_buscar,"está",contadorApariciones,"veces en la lista")

"""

# Ejercicio 5


numA = int(input("Ingrese el primer número: "))
numB = int(input("Ingrese el segundo número, para determinar el rango de valores validos: "))

vecNumeros = ingresarNumerosLista(numA,numB)

# HACER UN FOR QUE LA RECORRA AL REVES LA LISTA, Y A LA NUEVA LISTA PONERLE EL VALOR DE VEC[I]