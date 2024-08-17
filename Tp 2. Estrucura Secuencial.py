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

# % SIGNIFICA EL MODULO, EL RESIDUO DE LA DIVISIÓN
# q)
print("q)")
opreracion_17 = 12 % 5
print("El resultado de la operación 12 % 5 es:",opreracion_17)
print("--------------------------------------------------------------------")

"""

# Ejercicio 2

numA = int(input("Ingrese un numero entero"))
numB= int(input("Ingrese otro numero entero"))

def sumar(numA, numB):
    resultado = numA + numB
    return resultado


print(sumar(numA,numB))