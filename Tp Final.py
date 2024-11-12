# TRABAJO PRÁCTICO FINAL
# Tema Análisis de ventas online

# Funciones para validad los datos de cada venta

# Función que valida el ID
def validarId() :
    id = int(input("Ingrese el ID del producto: ")) 
    while id < 0 :
        print("ERROR, el ID del producto debe ser mayor a 0") 
        id = int(input("Ingrese el ID del producto: "))
    return id 

# Función que valida la categoría
def validarCategoria() :
    categoria = int(input("Ingrese la categoría del producto. 1 (Auto) - 2 (Moto) - 3 (Camioneta): ")) 
    while categoria != 1 and categoria != 2 and categoria != 3 : 
        print("ERROR, el número de categoría no es válido. El mismo debe ser 1, 2 o 3") 
        categoria = int(input("Ingrese la categoría del producto. 1 (Auto) - 2 (Moto) - 3 (Camioneta): ")) 
    return categoria 

# Función que valida el precio
def validarPrecio() :
    precio = float(input("Ingrese el precio del producto: "))  
    while precio < 0 : 
        print("ERROR, el precio del producto debe ser mayor a 0")  
        precio = float(input("Ingrese el precio del producto: ")) 
    return precio 
    
# Función que valida la cantidad vendida
def validarCantidadVendida() :
    cantVendida = int(input("Ingrese la cantidad del producto: ")) 
    while cantVendida < 0 : 
        print("ERROR, la cantidad del producto debe ser mayor a 0") 
        cantVendida = int(input("Ingrese la cantidad del producto: ")) 
    return cantVendida 

# Función que valida el mes   
def validarFechaMes () :
    mes = int(input("Ingrese el mes en el que se realizó la venta: ")) 
    while mes <=0 or mes > 12 : 
        print("ERROR, el mes debe estar entre 1 y 12") 
        mes = int(input("Ingrese el mes en el que se realizó la venta: ")) 
    return mes 

# Función que valida el día
def validarFechaDia(mes) :
    fechaDia = int(input("Ingrese el día que se realizó la venta: ")) 
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 : 
        while fechaDia < 0 or fechaDia> 31:  
            print("ERROR, el día debe ser mayor a 0 y menor a 31") 
            fechaDia = int(input("Ingrese el día que se realizó la venta: ")) 

    elif mes == 2 : 
        while fechaDia < 0 or fechaDia> 29: 
            print("ERROR, el día debe ser mayor a 0 y menor a 29") 
            fechaDia = int(input("Ingrese el día que se realizó la venta: "))

    else: 
        while fechaDia < 0 or fechaDia> 30: 
            print("ERROR, el día debe ser mayor a 0 y menor a 30") 
            fechaDia = int(input("Ingrese el día que se realizó la venta: ")) 
    return fechaDia

# Función para cargar los datos de cada venta
def cargarDatosVentas(cant) : 

    vecVentas = []

    idProducto = []
    categoria = []
    precio = []
    cantVendida = []  
    fechaMes = []
    fechaDia = []
 
    for i in range(cant) : 
        print()
        print("N° VENTA:",i +1) 
        print()
        
        id = validarId() 
        idProducto.append(id) 

        cat = validarCategoria() 
        categoria.append(cat) 

        prec = validarPrecio() 
        precio.append(prec)

        cantVen = validarCantidadVendida() 
        cantVendida.append(cantVen) 

        fechaM = validarFechaMes() 
        fechaMes.append(fechaM) 

        fechaD = validarFechaDia(fechaM) 
        fechaDia.append(fechaD) 

        venta = [id,cat,prec,cantVen,fechaM,fechaD] 
        vecVentas.append(venta)

    return vecVentas

def calcularTotalIngresos(vec) :
    largo = len(vec)

    acumIngresos = 0

    for i in range(largo) :
        
       ingreso = vec[i][2] * vec[i][3]
       acumIngresos += ingreso

    return acumIngresos


def obtenerCantProductosCategoria(vec,cat) :
    largo = len(vec)
    cantTotal = 0  

    for i in range(largo) :
        if cat == vec[i][1] :
            cantTotal += vec[i][3]

    return cantTotal


def obtenerDiasDeVentas(vec):
    largo = len(vec)  
    listaFechas = []  
    for i in range(largo):  
        mes1 = vec[i][4]  
        dia1 = vec[i][5]  

        fecha = (mes1, dia1)
        
        if fecha not in listaFechas:
            listaFechas.append(fecha)

    return listaFechas


def calcularPromedioIngresosDiarios(vec,cantDias) :

    promedio = calcularTotalIngresos(vec) / cantDias

    return promedio


# PROGRAMA PRINCIPAL

print("Bienvenidos al sistema de registración de ventas de Fast Cars")
print("-------------------------------------------------------------------------------")

# Se le pide al usuario que ingrese la cantidad de ventas que realizó en el último año. Al ser ventas, el tipo de dato es entero, no puede ser decimal
cantVentas = int(input("Ingrese la cantidad de ventas realizadas en el último año: "))

# Al tener que ingresar como minimo 10 ventas, si el usuario ingresa menos, se le vuelve a pedir
while cantVentas < 10 :
    print("ERROR, la cantidad de ventas mínima debe ser 10")
    cantVentas = int(input("Ingrese la cantidad de ventas realizadas en el último mes: "))

vecVentas = cargarDatosVentas(cantVentas) # Se carga el vector con las ventas

print()
categoriaABuscar = int(input("Ingrese el número de la categoría del producto que desea saber cuantos productos se han vendido en total. 1 (Auto) - 2 (Moto) - 3 (Camioneta): : ")) 
while categoriaABuscar != 1 and categoriaABuscar != 2 and categoriaABuscar != 3 :
        print("ERROR, el número de categoría no es válido. El mismo debe ser 1, 2 o 3") 
        categoriaABuscar = int(input("Ingrese el número de la categoría del producto que desea saber cuantos productos se han vendido en total. 1 (Auto) - 2 (Moto) - 3 (Camioneta): : ")) 
print()

totalIngresos = calcularTotalIngresos(vecVentas) # Se almacenan los ingresos totales en una variable
print("En el último mes, la empresa a generado ingresos de $",totalIngresos) 

print()

totalProductosXCategoria = obtenerCantProductosCategoria(vecVentas,categoriaABuscar) # Se almacenan el total de productos de la categoría que el usuario ingreso en la variable categoriaABuscar
print("De la categoria",categoriaABuscar,"se han vendido",totalProductosXCategoria,"productos") 

cantDias = obtenerDiasDeVentas(vecVentas) 
largoDias = len(cantDias) # Se obtiene el largo del vector con los dias distintos de venta

promedio = calcularPromedioIngresosDiarios(vecVentas,largoDias) # Se almacena el promedio de ingresos diaros teniendo en cuenta los días distintos de ventas
print("El promedio de ingresos diarios es de:",promedio) 

print()
print("CARGA DE DATOS FINALIZADA ") # Finaliza el programa