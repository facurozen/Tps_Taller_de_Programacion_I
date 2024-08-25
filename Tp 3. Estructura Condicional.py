# Trabajo Práctico 2

# Ejercicio 1

"""
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))

if num1 == num2:
    print("Los dos números que ingresaste son iguales")
else:
    print("Los dos números que ingresaste son distintos")
    


# Ejercicio 2

num_par_impar = int(input("Ingrese un número entero: "))

if num_par_impar % 2 == 0:
    print("El número",num_par_impar,"es par")
else:
    print("El número",num_par_impar,"es impar")
    


# Ejercicio 3

numMes = int(input("Ingrese el número de mes: "))

if numMes == 1:
    print("El mes número",numMes,"es Enero")

elif numMes == 2:
    print("El mes número",numMes,"es Febrero")

elif numMes == 3:
    print("El mes número",numMes,"es Marzo")

elif numMes == 4:
    print("El mes número",numMes,"es Abril")

elif numMes == 5:
    print("El mes número",numMes,"es Mayo")

elif numMes == 6:
    print("El mes número",numMes,"es Junio")

elif numMes == 7:
    print("El mes número",numMes,"es Julio")

elif numMes == 8:
    print("El mes número",numMes,"es Agosto")

elif numMes == 9:
    print("El mes número",numMes,"es Septiembre")

elif numMes == 10:
    print("El mes número",numMes,"es Octubre")

elif numMes == 11:
    print("El mes número",numMes,"es Noviembre")

elif numMes == 12:
    print("El mes número",numMes,"es Diciembre")

else:
    print("ERROR. Los números de meses validos van del 1 al 12")



# Ejercicio 4

votos_a_favor = int(input("Ingrese la cantidad de votos a favor: "))
votos_en_contra = int(input("Ingrese la cantidad de votos en contra: "))

votosTotal = votos_a_favor + votos_en_contra

porcentaje_a_favor = (votos_a_favor * 100) / votosTotal
porcentaje_en_contra = (votos_en_contra * 100) / votosTotal

print("Hubo un total de",porcentaje_a_favor,"% de votos a favor")
print("Hubo un total de",porcentaje_en_contra,"% de votos en contra")

if porcentaje_a_favor > porcentaje_en_contra:
    print("La ley ha sido aprobada")
else:
    print("La ley NO ha sido aprobada")
    


# Ejercicio 5

nota1 = int(input("Ingrese la nota del primer parcial: "))
nota2 = int(input("Ingrese la nota del segundo parcial: "))

if nota1 <0 or nota1>10 or nota2 <0 or nota2 >10 :
    print("ERROR, ingrese el valor de las notas debe ser de 0 a 10")
else:
    if nota1>=7 and nota2>=7 :
        print("Felicitaciones, promocionaste la materia!!")

    elif nota1>= 4 and nota2>=4 :
        print("Felicitaciones, aprobaste la materia!")

    elif nota1 < 4 or nota2 < 4:
        print("Tenés que recuperar la materia")



# Ejercicio 6

numPag = int(input("Ingrese la cantidad de páginas que contiene el libro: "))
costoLibroBase = 5000
encuadernacion_tela = 1200
encuadernacion_especial = 3360

if numPag <= 0 :
    print("ERROr, ingrese una cantidad de páginas valida, de 1 en adelante") 

else:
    if numPag <= 300 :
        costoLibro = costoLibroBase + (numPag * 32)
        print("El costo del libro es de: $",costoLibro)
    
    elif numPag > 300 and numPag <= 600 :
        costoLibro = costoLibroBase + (numPag * 32) + encuadernacion_tela
        print("El costo del libro es de: $",costoLibro)
    
    elif numPag > 600 :
        costoLibro = costoLibroBase + (numPag * 32) + encuadernacion_tela + encuadernacion_especial
        print("El costo del libro es de: $",costoLibro)



# Ejercicio 7

kmRecorridos = float(input("Ingrese la cantidad de km que debe recorrer el flete: "))
if kmRecorridos < 0 :
    print("ERROR, la cantidad de km recorridos debe ser mayor a 0")

else :
    viajeMinimo = 2700 
    precioFinal = 0

    if kmRecorridos > 0 and kmRecorridos < 10:
            precioFinal = kmRecorridos * 400
            
    elif kmRecorridos >= 10 :
            precioFinal = kmRecorridos * 200

    if precioFinal < viajeMinimo :
            precioFinal = viajeMinimo

print("El precio del viaje es de: $",precioFinal)

"""

# Ejercicio 8
