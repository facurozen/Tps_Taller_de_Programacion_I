# TRABAJO PRÁCTICO FINAL
# Tema Análisis de ventas online

# Funciones para validad los datos de cada venta
def validarId() :
    id = int(input("Ingrese el ID del producto: "))
    while id < 0 :
        print("ERROR, el ID del producto debe ser mayor a 0")
        id = int(input("Ingrese el ID del producto: "))
    return id

def validarPrecio() :
    precio = float(input("Ingrese el precio del producto: "))
    while precio < 0 :
        print("ERROR, el precio del producto debe ser mayor a 0")
        precio = float(input("Ingrese el precio del producto: "))
    return precio
    
def validarCantidadVendida() :
    cantVendida = int(input("Ingrese la cantidad del producto: "))
    while cantVendida < 0 :
        print("ERROR, la cantidad del producto debe ser mayor a 0")
        cantVendida = int(input("Ingrese la cantidad del producto: "))
    return cantVendida
    
def validarFechaMes () :
    mes = int(input("Ingrese el mes en el que se realizó la venta: "))
    while mes <=0 or mes > 12 :
        print("ERROR, el mes debe estar entre 1 y 12")
        mes = int(input("Ingrese el mes en el que se realizó la venta: "))
    return mes


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

        cat = input("Ingrese la categoría del producto: ")
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
        
        vec[i precio] * vec[i cantidad]

    return acumIngresos


def obtenerCantProductosCategoria(vec,cat) :
    largo = len(vec)
    cantTotal = 0  

    for i in range(largo) :
        if cat == vec[i categoria] :
            cantTotal += vec[i cantVendida]

    return cantTotal



# PROGRAMA PRINCIPAL

# Se le pide al usuario que ingrese la cantidad de ventas que realizó en el último mes. Al ser ventas, el tipo de dato es entero, no puede ser decimal
cantVentas = int(input("Ingrese la cantidad de ventas realizadas en el último mes: "))

# Al tener que ingresar como minimo 10 ventas, si el usuario ingresa menos, se le vuelve a pedir
while cantVentas < 0 :
    print("ERROR, la cantidad de ventas mínima debe ser 10")
    cantVentas = int(input("Ingrese la cantidad de ventas realizadas en el último mes: "))

vecVentas = cargarDatosVentas(cantVentas)

categoriaABuscar = input("Ingrese la categoría del producto que desea saber cuantos productos se han vendido en total: ")

print()

totalIngresos = calcularTotalIngresos(vecVentas)
print("En el último mes, la empresa a generado ingresos de $",totalIngresos)

print()

totalProductosXCategoria = obtenerCantProductosCategoria(vecVentas,categoriaABuscar)
print("De la categoria",categoriaABuscar,"se han vendido",totalProductosXCategoria,"productos")


