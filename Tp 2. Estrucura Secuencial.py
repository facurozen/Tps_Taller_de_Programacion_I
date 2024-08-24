# Trabajo Práctico 2

# Ejercicio 1

"""
# a)
print("a)")
opreracion_1 = 12*4 + 4*5
print("El resultado de la operación 12*4 + 4*5 es:",opreracion_1)
print("--------------------------------------------------------------------")

# b)
print("b)")
opreracion_2 = (12 * (1-5) + 4) * 3
print("El resultado de la operación(12 * (1-5) + 4) * 3 es:",opreracion_2)
print("--------------------------------------------------------------------")

# c)
print("c)")
opreracion_3 = 12*1 -5 + 4*3
print("El resultado de la operación 12*1 -5 + 4*3 es:",opreracion_3)
print("--------------------------------------------------------------------")

# d)
print("d)")
opreracion_4 = (17-2) / 5
print("El resultado de la operación (17-2) / 5 es:",int(opreracion_4))
print("--------------------------------------------------------------------")

# e)
print("e)")
opreracion_5 = 3 + 2*2 - (8*4 + 1/2.0) * 3
print("El resultado de la operación 3 + 2*2 - (8*4 + 1/2.0) * 3 es:",opreracion_5)
print("--------------------------------------------------------------------")

# f)
print("f)")
opreracion_6 = 5 * 4/2
print("El resultado de la operación 5 * 4/2 es:",int(opreracion_6))
print("--------------------------------------------------------------------")

# g)
print("g)")
opreracion_7 = 5 * (4/2)
print("El resultado de la operación 5 * 4/2 es:",int(opreracion_7))
print("--------------------------------------------------------------------")

# ** SIGNIFICA ELEVADO A
# h)
print("h)")
opreracion_8 = 24 / 2**2
print("El resultado de la operación 24 / 2**2 es:",int(opreracion_8))
print("--------------------------------------------------------------------")

# i)
print("i)")
opreracion_9 = (24/2) **2
print("El resultado de la operación (24/2) **2 es:",int(opreracion_9))
print("--------------------------------------------------------------------")

# j)
print("j)")
opreracion_10 = 3 + 4*6 / 2-5
print("El resultado de la operación 3 + 4*6 / 2-5 es:",int(opreracion_10))
print("--------------------------------------------------------------------")

# k)
print("k)")
opreracion_11 = 3 + 4*6 / (2-5)
print("El resultado de la operación 3 + 4*6 / (2-5) es:",int(opreracion_11))
print("--------------------------------------------------------------------")

# l)
print("l)")
opreracion_12 = (-0.1) * 3
print("El resultado de la operación (-0.1) * 3 es:",opreracion_12)
print("--------------------------------------------------------------------")

# m)
print("m)")
opreracion_13 = -9 ** 2
print("El resultado de la operación -9 ** 2 es:",opreracion_13)
print("--------------------------------------------------------------------")

# n)
print("n)")
opreracion_14 = (-9) ** 2
print("El resultado de la operación (-9) ** 2 es:",opreracion_14)
print("--------------------------------------------------------------------")

# o)
print("o)")
opreracion_15 = 10 /3
print("El resultado de la operación 10 /3 es:",opreracion_15)
print("--------------------------------------------------------------------")

# // ES UNA DIVISIÓN NORMAL, SOLO QUE REDONDEA AL ENTERO MAS CHIQUITO. SI LA DIVISÓN DA 3.5, EL RESULTADO CON EL // VA A SER 3, Y SI LA DIVISIÓN DA 3.9, EL RESULTADO TAMBIÉN VA A SER 3
# p)
print("p)")
opreracion_16 = 10 // 3
print("El resultado de la operación 10 // 3 es:",opreracion_16)
print("--------------------------------------------------------------------")

# % SIGNIFICA EL MODULO, EL RESTO DE LA DIVISIÓN
# q)
print("q)")
opreracion_17 = 12 % 5
print("El resultado de la operación 12 % 5 es:",opreracion_17)
print("--------------------------------------------------------------------")


# Ejercicio 2

numA = int(input("Ingrese un numero entero: "))
numB= int(input("Ingrese otro numero entero: "))

def sumar(numA, numB):
    resultado = numA + numB
    return resultado

def restar(numA, numB):
    resultado = numA - numB
    return resultado


print("El resultado de sumar",numA, "+",numB, "es:", sumar(numA,numB))
print("El resultado de restar",numA, "-",numB, "es:", restar(numA,numB))


# Ejercicio 3

notaA = int(input("Ingrese la nota del primer parcial: "))
notaB= int(input("Ingrese la nota del segundo parcial: "))

def promedio(notaA, notaB):
    promedioNotas = int((notaA + notaB) / 2)
    return promedioNotas

print("El promedio de notas del alumno fue:",promedio(notaA,notaB))


# Ejercicio 4

edad = int(input("Ingrese la edad en años: "))

def convertir_edad_a_dias (edad):
    convertir = edad * 365
    return convertir

print(edad, "años, son:",convertir_edad_a_dias(edad),"días")   


# Ejercicio 5

precioMedicamento = float(input("Ingrese el precio del medicamento: "))
descuento = (precioMedicamento * 35) / 100
importeFinal = precioMedicamento - descuento

print("El precio original del medicamento es de:",precioMedicamento)
print("El monto del descuento del medicamento es de:",descuento)
print("El importe final a pagar es:",importeFinal)


# Ejercicio 6

aporte1 = float(input("Ingrese el aporte que realizó la primer persona: "))
aporte2 = float(input("Ingrese el aporte que realizó la segunda persona: "))
aporte3 = float(input("Ingrese el aporte que realizó la tercer persona: "))
total = aporte1 + aporte2 + aporte3

porcentaje1 = (aporte1 * 100) / total
porcentaje2 = (aporte2 * 100) / total
porcentaje3 = (aporte3 * 100) / total

print("La primera persona aportó:", porcentaje1,"%")
print("La segunda persona aportó:", porcentaje2,"%")
print("La tercera persona aportó:", porcentaje2,"%")


# Ejercicio 7

dineroInvertido = float(input("Ingrese el dinero invertido en el banco: "))
rendimientoMensual = (2 * dineroInvertido) / 100
rendimientoTotal = rendimientoMensual * 6

print("Si deja su dinero invertido en el banco, ganará un total de: $",rendimientoTotal)


# Ejercicio 8

medidaMetros = float(input("Ingrese la medida expresada en metros: "))
conversionCm = round(float(medidaMetros * 100),2)
conversionPulgadas = round(float(conversionCm / 2.54),2)
conversionPies = round(float(conversionPulgadas / 12),2)
conversionYardas = round(float(conversionPies/3),2)

print(medidaMetros,"metros, equivalen a",conversionCm,"centímetros")
print(medidaMetros,"metros, equivalen a",conversionPulgadas,"pulgadas")
print(medidaMetros,"metros, equivalen a",conversionPies,"pies")
print(medidaMetros,"metros, equivalen a",conversionYardas,"yardas")



# Ejercicio 9

numVendedor = int(input("Ingrese el numero del vendedor: "))
cantVentas = int(input("Ingrese la cantidad de ventas que realizó: "))
valorTotalVentas = int(input("Ingrese el valor total de las ventas que realizó: "))
salarioBase = 250000
comisionXVentas = 50000 * cantVentas
comisionTotalVentas = (5 * valorTotalVentas) / 100

salarioTotal = int(salarioBase + comisionXVentas + comisionTotalVentas)

print("El vendedor número",numVendedor,"debe recibir un salario de $",salarioTotal)


# Ejercicio 10

largo = float(input("Ingrese la medida del largo de su parcela, expresada en metros: "))
ancho = float(input("Ingrese la medida del ancho de su parcela, expresada en metros: "))
areaParcela = largo*ancho

# Así calculo cuantos grupos de 2 quintales hay en la parcela, porque en 10 m2, hay 2 quintales.
grupo_de_quintales_en_10m2 = areaParcela / 10

# Así calculo la cantidad de quintales, ya que en 10 m2 hay dos quintales, y la variable grupo_de_quintales_en_10m2 va a tener cuantos bloques de 2 quintales hay en la parcela, por lo que lo multiplico por dos.
cantQuintales = grupo_de_quintales_en_10m2 * 2

print("En la parcela se pueden producir",cantQuintales,"quintales de trigo")


# Ejercicio 11

periodoEnSegundos = int(input("Ingrese un período de segundos: "))

conversionDias = periodoEnSegundos // 86400 
segundos_restantes_dias = periodoEnSegundos % 86400 # (Segundos restantes que no llegan a completar un día entero)
conversionHoras = segundos_restantes_dias // 3600 # (Cantidad de segundos que tiene una hora)
segundos_restantes_horas = segundos_restantes_dias % 3600
conversionMinutos = segundos_restantes_horas // 60 # cantidad de segundos en un minuto
segundos_restantes_minutos = segundos_restantes_horas % 60

print(periodoEnSegundos,"segundos equivalen a:",conversionDias,"días,",conversionHoras,"horas,",conversionMinutos,"minutos y",segundos_restantes_minutos,"segundos")


# Ejercicio 12

cantDinero = int(input("Ingrese la cantidad de dinero que quiere retirar: "))

billetes1000 = cantDinero // 1000
restantes1000 = cantDinero % 1000

billetes500 = restantes1000 // 500
restantes500 = restantes1000 % 500

billetes100 = restantes500 // 100
restantes100 = restantes500 % 100

billetes50 = restantes100 // 50
restantes50 = restantes100 % 50

billetes10 = restantes50 // 10
restantes10 = restantes50 % 10

billetes5 = restantes10 // 5
restantes5 = restantes10 % 5

# en este como ya no quedan billetes de menor valor, y tampoco hay monedas, no calculo el resto
billetes1 = restantes5 // 1

print("El cajero debe entregar:",billetes1000, "billetes de $1000,",billetes500,"billetes de $500,",billetes100,"billetes de $100,",billetes50,"billetes de $50,",billetes10,"billetes de $10,",billetes5,"billetes de $5,", billetes1," billetes de $1")


# Ejercicio 13

numBinario = int(input("Ingrese un numero binario de 4 cifras. Recordá que un numero binario, solo acepta 0 y 1: "))

# este orden es contando desde la izquierda de todo, cuando lo paso de decimal a binario, sería el que esta elevado a la mayor potencia
primerNumero = numBinario // 1000

# el % 10 lo uso para obtener el numero de la derecha, ya que cuando divido el numero binario por 100, me quedan dos numero, si yo hago el % 10 de esos dos numeros, me da el digito de la derecha, y en ese caso, busco el digito de la derecha, porque el de la izquierda es el que calcule ariba, al hacer // 1000, me sacó los ultimo 3 numeros, por lo tanto, al hacer // 100, obtengo 2 numeros, pero como el de la izquierda ya lo tengo, hago % 10, y así me da el de la derecha.
# % 10 siempre me va a dar como resultado el numero de la derecha
segundoNumero = (numBinario // 100) % 10

tecerNumero = (numBinario // 10) % 10

cuartoNumero = numBinario % 10

numDecimal = (primerNumero * 2**3) + (segundoNumero * 2**2) + (tecerNumero * 2 **1) + (cuartoNumero*2**0)
print("El número binario",numBinario,"equivale al número decimal:",numDecimal)

"""

