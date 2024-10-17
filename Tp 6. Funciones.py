# Trabajo Práctico 6

# Ejercicio 1
"""
def calcularResultadoMultiplicación(n1,n2) :
    i = 0
    resultado = 0
    if n2 < 0 :
        while i > n2 :
            resultado -= n1 
            i -= 1
    
    elif n1 < 0 and n2 < 0 :
         
        while i > n2 :
            resultado += n1 
            i -= 1

    else :    
        while i < n2 :
            resultado += n1 
            i += 1
        
    return resultado


num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero: "))

resultado = calcularResultadoMultiplicación(num1,num2)
print("El resultado de multiplicar",num1,"*",num2,"es:",resultado)


# Ejercicio 2

def calcularResultadoMultiplicación(n1,n2) :
    i = 0
    resultado = 1

    if n2 == 0 :
        resultado = 0

    if n2 < 0 :
        while i > n2 :
            resultado *= n1  
            i -= 1
        resultado = 1 / resultado

    else :    
        while i < n2 :
            resultado *= n1  
            print(resultado)
            i += 1
        
    return resultado


num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero: "))

resultado = calcularResultadoMultiplicación(num1,num2)
print("El resultado de",num1,"elevado a la",num2,"es:",resultado)


# Ejercicio 3

def imprimirColumnaDeAsteristicos(h) :
    i = 0
    while i < h :
        print("*")
        i += 1

altura = int(input("Ingrese la altura de la columa de asteriscos: "))

imprimirColumnaDeAsteristicos(altura)


# Ejercicio 4

def calcularSiEsMultiplo(n1,n2) :
    esMultiplo = False

    if n1 % n2 == 0 :
        esMultiplo = True
    
    else :
        esMultiplo = False
    
    return esMultiplo



num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero: "))

esMultiplo = calcularSiEsMultiplo(num1,num2)
print(esMultiplo)

"""

def signo(n) :
    if num > 0:
        resultadoSigno = 1
    
    elif num < 0 :
        resultadoSigno = -1
    
    else :
        resultadoSigno = 0
    
    return resultadoSigno

num = int(input("Ingrese un número entero: "))
resultadoSigno = signo(num)
print(resultadoSigno)