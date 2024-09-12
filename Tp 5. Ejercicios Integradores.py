# Trabajo Práctico 5

"""
# Ejercicio 1

contadorMenor = 0
contadorMayor = 0
acumMenor = 0
acumMayor = 0
promedioMenor = 0
promedioMayor = 0

edad = int(input("Ingrese la edad o -1 para finalizar el programa: "))

while edad != -1 :
    if edad < 0 or edad > 100 :
        print("ERROR, la edad válida esta entre 0 y 100 ")

    else:
        if edad < 18 :
            contadorMenor += 1
            acumMenor += edad

        else :
            contadorMayor += 1
            acumMayor += edad
    edad = int(input("Ingrese la edad o -1 para finalizar el programa: "))

promedioMenor = acumMenor / contadorMenor
promedioMayor = acumMayor / contadorMayor 

print("Hay",contadorMenor,"personas menores de 18 años")
print("Hay",contadorMayor,"personas mayores de 18 años")
print("El promedio de edad de las personas menores de 18 años es:",promedioMenor,"años")
print("El promedio de edad de las personas mayores de 18 años es:",promedioMayor,"años")



# Ejercicio 2

contadorAprobados = 0
contadorReprobados = 0
contadorAplazados = 0
i = 0
porcentajeAplazados = 0

numLegajo = int(input("Ingrese el número de legajo del alumno o -1 para finalizar el programa: "))

while numLegajo != -1 :
    nota = int(input("Ingrese la nota del examen final: "))

    while nota < 1 or nota > 10 :
        print("ERROR, la nota debe estar entre 1 y 10")
        nota = int(input("Ingrese la nota del examen final: "))

    if nota >= 4 :   
        print("Aprobaste el examen!!")
        contadorAprobados += 1
    else :
        print("Reprobaste el examen")
        contadorReprobados += 1

    if nota == 1 :
        contadorAplazados += 1
        
    i += 1
    numLegajo = int(input("Ingrese el número de legajo del alumno o -1 para finalizar el programa: "))

if numLegajo == -1 and i == 0 :
    print("No se han ingresado datos")

else :
    if i != 0 :
        porcentajeAplazados = (contadorAplazados * 100) / i
    else :
        print("ERROR, no se puede dividir por cero")

    print(" ")
    print("La cantidad de alumnos que aprobaron con una nota mayor o igual a 4 es:",contadorAprobados)
    print("La cantidad de alumnos que desaprobaron con una nota menor a 4 es:",contadorReprobados)
    print("El porcentaje de alumnos que estan aplazados es:",porcentajeAplazados,"%")



# Ejercicio 3

cantProducto = int(input("Ingrese la cantidad de productos que solicitó o -1 para finalizar el programa: "))

valorTotal = 0
promedioUnidad = 0
cantVentasTotal = 0
cantVentasDescuento10 = 0
cantVentasPrecioBase = 0

while cantProducto != -1 :

    while cantProducto < 0 :
        print("ERROR, la cantidad ingresada no puede ser menor a 0")
        cantProducto = int(input("Ingrese la cantidad de productos que solicitó o -1 para finalizar el programa: "))
        
    precioBase = int(input("Ingrese el precio base del producto: ")) 

    while precioBase <= 0 :
        print("ERROR, el precio base del producto no puede ser menor a 0")
        precioBase = int(input("Ingrese el precio base del producto: ")) 
    
    if cantProducto <= 12 :
        valorTotal = precioBase * cantProducto
        promedioUnidad = round((valorTotal / cantProducto),2)

        cantVentasPrecioBase += 1

        print(" ")
        print("El valor total de la venta es: $",valorTotal)
        print("El precio promedio por unidad es: $",promedioUnidad)
    
    elif cantProducto >= 13 and cantProducto <= 100 :

        unidadesBase = 12
        valorAux = (precioBase * unidadesBase) 

        unidadesDescuento10 = cantProducto - unidadesBase
        descuento10 = precioBase * 0.90

        valorTotal = valorAux + (descuento10 * unidadesDescuento10)
        promedioUnidad = round((valorTotal / cantProducto),2)
        
        cantVentasDescuento10 += 1

        print(" ")
        print("El valor total de la venta es: $",valorTotal)
        print("El precio promedio por unidad es: $",promedioUnidad)

    elif cantProducto > 100 :

        unidadesBase = 12
        valorAux1 = (precioBase * unidadesBase)

        descuento10 = precioBase * 0.90
        unidadesDescuento10 = 88
        valorAux2 = valorAux1 + (descuento10 * unidadesDescuento10)

        unidadesDescuento25 = cantProducto - 100
        descuento25 = precioBase * 0.75
        valorTotal = valorAux2 + (descuento25 * unidadesDescuento25)
        promedioUnidad = round((valorTotal / cantProducto),2)

        print(" ")
        print("El valor total de la venta es: $",valorTotal)
        print("El precio promedio por unidad es: $",promedioUnidad)

    cantVentasTotal += 1

    print(" ")
    cantProducto = int(input("Ingrese la cantidad de productos que solicitó o -1 para finalizar el programa: "))

print(" ")
print("Se han realizado un total de:",cantVentasTotal,"ventas")
print("Se han realizado un total de:",cantVentasDescuento10,"ventas en las que se aplicó un 10% de descuento")
print("Se han realizado un total de:",cantVentasPrecioBase,"en las que no se aplicó ningún descuento")



# Ejercicio 4

numCliente = int(input("Ingrese el número del cliente: "))
totalFactura = float(input("Ingrese el valor total de la factura: "))

descuentoPesos = 200
descuentoPorcentaje = totalFactura * 0.02

if descuentoPesos > descuentoPorcentaje :
    totalDescuento = totalFactura - descuentoPesos
    
else :
    totalDescuento = totalFactura - descuentoPorcentaje

totalFactura = totalFactura

multaPesos = 350
multaPorcentaje = totalFactura * 0.10

if multaPesos > multaPorcentaje :
    totalMulta = totalFactura + multaPesos 
    
else :
    totalMulta = totalFactura + multaPorcentaje

print(" ")
print("Cliente N°:",numCliente )
print(" ")
print("Si paga antes del día 10 del mes siguiente, debera pagar: ",totalDescuento)
print("Si no paga antes del día 10, pero paga antes del día 20 del mes siguiente, debera pagar:",totalFactura)
print("Si paga después del día 20 del mes siguiente, debera pagar:",totalMulta)



# Ejercicio 5

d = int(input("Ingrese el día: "))
m = int(input("Ingrese el mes: "))
a = int(input("Ingrese el año: "))

n = int(input("Ingrese la cantidad de días que le quiere sumar a la fecha: "))

while n <0 :
    print("ERROR, la cantidad de dias ingresados debe ser mayor o igual a 0 y menor o igual a 31")
    n = int(input("Ingrese la cantidad de días que le quiere sumar a la fecha: "))


if (m == 4 or m == 6 or m == 9 or m == 11) and n < 30 :     
        diasAgregados = d + n

        mesesAgregados = diasAgregados // 30 
        diasSobrantes = diasAgregados % 30

        if m

        a = a
        m = m + 1
        d = diasAgregados - 30

elif (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and diasAgregados > 31 and diasAgregados < 365 :
    a = a
    m = m + 1
    d = diasAgregados - 31

print("La nueva fecha es:",d,"/",m,"/",a)


if numAño % 4 != 0 :
    print("El año",numAño,"NO es bisiesto")

else :
    if numAño % 100 != 0 :
        print("El año",numAño," SÍ es bisiesto")

    else :
        if numAño % 400 == 0 :
            print("El año",numAño,"SÍ es bisiesto")
        
        else :
            print("El año",numAño,"NO es bisiesto")
            




# Ejercicio 6

num = int(input("Ingrese un número entero: ")) 



# Ejercicio 7

# Ejercicio 8

cantidadEmpleados = int(input("Ingrese la cantidad de empelados que hay en la empresa: "))
acumSalarios = 0
cantSalario200k = 0
cantSalario50k = 0
salarioMayor = 0
legajoMayor = 0
importeTotal1 = 0
importeTotal2 = 0
importeTotal3 = 0

while cantidadEmpleados <= 0 :
    print("ERROR, la cantidad de empleados debe ser mayor a cero")
    cantidadEmpleados = int(input("Ingrese la cantidad de empelados que hay en la empresa: "))

i = 1
while i <= cantidadEmpleados :
    print(" ")
    legajo = int(input("Ingrese el número de legajo: "))

    categoria = int(input("Ingrese la categoría del empleado (1,2,3): "))

    while categoria != 1 and categoria != 2 and categoria != 3 :
        print("ERROR, la categoría del empelado debe ser 1,2 o 3")
        categoria = int(input("Ingrese la categoría del empleado (1,2,3): "))

    salario = float(input("Ingrese el sueldo del empleado: "))

    while salario <= 0 :
        print("ERROR, el salario del empleado debe ser mayor a 0")
        salario = float(input("Ingrese el sueldo del empleado: "))

    acumSalarios = acumSalarios + salario
    if salario > 200000 :
        cantSalario200k += 1

    if categoria == 3 and salario < 50000 :
        cantSalario50k += 1

    if salario > salarioMayor :
        salarioMayor = salario
        legajoMayor = legajo
    
    salarioMenor = salario
    if salario < salarioMenor :
        salarioMenor = salario

    if categoria == 1 :
        importeTotal1 = importeTotal1 + salario

    elif categoria == 2 :
        importeTotal2 = importeTotal2 + salario

    else :
        importeTotal3 = importeTotal3 + salario

    i += 1

promedio = acumSalarios / cantidadEmpleados 

print(" ")
print("El importe total de salarios pagados por la empresa es:",acumSalarios)
print("La cantidad de empelados que ganan un salario mayor a $200000 es:",cantSalario200k)
print("La cantidad de empelados que ganan un salario menor a $50000 y su categoría es 3 es:",cantSalario50k)
print("El legajo del empleado que más gana es:",legajoMayor)
print("El sueldo más bajo es de: $",salarioMenor)
print("El importe total de sueldos de la categoría 1 es:",importeTotal1)
print("El importe total de sueldos de la categoría 2 es:",importeTotal2)
print("El importe total de sueldos de la categoría 3 es:",importeTotal3)
print("El salario promedio es:",promedio)

"""

# Ejercicio 9

numero = int(input("Ingrese un número mayor a 0: "))
numImpar = 0
sumaImpares = 0
i = 1
while numero <= 0 :
    print("ERROR, el número debe ser mayor a cero")
    numero = int(input("Ingrese un número mayor a 0: "))

while i <= numero :
    if i % 2 != 0 :
        numImpar = i
        print(numImpar)
        sumaImpares = sumaImpares + i
    i += 1

print("La suma de los números impares es: ",sumaImpares)


# Ejercicio 10

cantEspectadores = int(input("Ingrese la cantidad de espectadores: "))
descuento = int(input("Ingrese 1 (si la función tiene descuento) o 2 (si la función NO tiene descuento)"))