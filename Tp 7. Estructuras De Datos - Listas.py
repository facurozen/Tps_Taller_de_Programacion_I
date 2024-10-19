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

"""
# Ejercicio 3

def invertirLista(vec) :
    largo = len(vec)
    nuevaLista = []
    for i in range(largo-1,-1,-1) :

        nuevaLista.append(vec[i])

    return nuevaLista 


def determinarCapicua(vec): 
    listaInvertida = invertirLista(vec) # USO LA FUNCIÓN QUE CREE EN EL EJERCICIO 5

    if listaInvertida == vec :
        capicua = True

    else :
        capicua = False

    return capicua

numA = int(input("Ingrese el primer número: "))
numB = int(input("Ingrese el segundo número, para determinar el rango de valores validos: "))

vecNumeros = ingresarNumerosLista(numA,numB)

print()
capicua = determinarCapicua(vecNumeros)

if capicua == True :
    print("La lista es capicúa")

else :
    print("La lista NO es capicúa")


"""
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

def invertirLista(vec) :
    largo = len(vec)
    nuevaLista = []
    for i in range(largo-1,-1,-1) :

        nuevaLista.append(vec[i])

    return nuevaLista 

"""   

numA = int(input("Ingrese el primer número: "))
numB = int(input("Ingrese el segundo número, para determinar el rango de valores validos: "))

vecNumeros = ingresarNumerosLista(numA,numB)

vecNumerosInvertido = invertirLista(vecNumeros)
print()
print("La lista original es:", vecNumeros)
print("La lista invertida es: ",vecNumerosInvertido)


# Ejercicio 6

def obtenerPosicion(valor,vec) :
    largo = len(vec)
    nuevaLista = []
    pos = -1

    for i in range(largo):
        if valor == vecNumeros[i] :
            pos = i
            nuevaLista.append(pos)
    
    return nuevaLista


numA = int(input("Ingrese el primer número: "))
numB = int(input("Ingrese el segundo número, para determinar el rango de valores validos: "))
vecNumeros = ingresarNumerosLista(numA,numB)

print()
valor = float(input("Ingrese el número que desea saber en que posición/es se encuentra en la lista: "))
listaPosiciones = obtenerPosicion(valor,vecNumeros)

print()
print("Lista de posiciones del valor",valor,"en la lista original:",listaPosiciones)

"""