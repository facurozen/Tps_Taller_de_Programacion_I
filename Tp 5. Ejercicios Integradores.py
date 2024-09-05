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

"""

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
    print(i)
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

            