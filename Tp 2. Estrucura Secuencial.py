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

"""

# Ejercicio 9

numVendedor = int(input("Ingrese el numero del vendedor: "))


