# TRABAJO PRÁCTICO FINAL
# Tema Análisis de ventas online

# Funciones para validad los datos de cada venta

# Función que valida el ID
def validarId() :
    id = int(input("Ingrese el ID del producto: ")) # Se le pide al usuario que ingrese el ID del producto
    while id < 0 : # Validamos que el mismo sea mayor a 0
        print("ERROR, el ID del producto debe ser mayor a 0") # Mensaje de error para avisarle que debe ser mayor a 0
        id = int(input("Ingrese el ID del producto: ")) # Se le vuelve a pedir que ingrese el ID, y repite el ciclo hasta que el mismo sea mayor a 0
    return id # La función devuelve el ID validado

# Función que valida el precio
def validarPrecio() :
    precio = float(input("Ingrese el precio del producto: "))  # Se le pide al usuario que ingrese el precio del producto
    while precio < 0 : # Validamos que el mismo sea mayor a 0
        print("ERROR, el precio del producto debe ser mayor a 0")  # Mensaje de error para avisarle que debe ser mayor a 0
        precio = float(input("Ingrese el precio del producto: ")) # Se le vuelve a pedir que ingrese el precio, y repite el ciclo hasta que el mismo sea mayor a 0
    return precio # La función devuelve el precio validado
    
# Función que valida la cantidad vendida
def validarCantidadVendida() :
    cantVendida = int(input("Ingrese la cantidad del producto: ")) # Se le pide al usuario que ingrese la cantidad vendida del producto
    while cantVendida < 0 : # Validamos que la mismo sea mayor a 0
        print("ERROR, la cantidad del producto debe ser mayor a 0") # Mensaje de error para avisarle que debe ser mayor a 0
        cantVendida = int(input("Ingrese la cantidad del producto: ")) # Se le vuelve a pedir que ingrese la cantidad vendida, y repite el ciclo hasta que el mismo sea mayor a 0
    return cantVendida # La función devuelve la cantidad vendida validada

# Función que valida el mes   
def validarFechaMes () :
    mes = int(input("Ingrese el mes en el que se realizó la venta: ")) # Se le pide al usuario que ingrese el mes en el que vendió el producto
    while mes <=0 or mes > 12 : # Validamos que la mismo sea mayor a 0 y menor a 12
        print("ERROR, el mes debe estar entre 1 y 12") # Mensaje de error para avisarle que el mes debe estar entre 1 y 12
        mes = int(input("Ingrese el mes en el que se realizó la venta: ")) # Se le vuelve a pedir que ingrese el mes, y repite el ciclo hasta que el mismo este entre 1 y 12
    return mes # La función devuelve el mes validado

# Función que valida el día
def validarFechaDia(mes) :
    fechaDia = int(input("Ingrese el día que se realizó la venta: "))  # Se le pide al usuario que ingrese el día en el que vendió el producto
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 :  # Verifica los meses que tienen 31 días 
        while fechaDia < 0 or fechaDia> 31:  # 
            print("ERROR, el día debe ser mayor a 0 y menor a 31")  # Mensaje de error para avisarle que el mes debe estar entre 1 y 12
            fechaDia = int(input("Ingrese el día que se realizó la venta: ")) # Se le vuelve a pedir que ingrese el mes, y repite el ciclo hasta que el mismo este entre 1 y 12

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
    cantdias=1
    
    for i in range(largo) :
        fecha1 = [vec[0][4], vec[0][5]]
        if [vec[i][4], vec[i][5]] != fecha1:
            cantdias+=1
            
    return cantdias
        

"""
def calcularPromedioIngresosDiarios(vec) :
    largo = len(vec)

    for i in range(largo) :
        if vec[i][4] == 
"""


# PROGRAMA PRINCIPAL

# Se le pide al usuario que ingrese la cantidad de ventas que realizó en el último mes. Al ser ventas, el tipo de dato es entero, no puede ser decimal
cantVentas = int(input("Ingrese la cantidad de ventas realizadas en el último mes: "))

# Al tener que ingresar como minimo 10 ventas, si el usuario ingresa menos, se le vuelve a pedir
while cantVentas < 0 :
    print("ERROR, la cantidad de ventas mínima debe ser 10")
    cantVentas = int(input("Ingrese la cantidad de ventas realizadas en el último mes: "))

vecVentas = cargarDatosVentas(cantVentas)


print()
categoriaABuscar = input("Ingrese la categoría del producto que desea saber cuantos productos se han vendido en total: ")

print()

totalIngresos = calcularTotalIngresos(vecVentas)
print("En el último mes, la empresa a generado ingresos de $",totalIngresos)

print()

totalProductosXCategoria = obtenerCantProductosCategoria(vecVentas,categoriaABuscar)
print("De la categoria",categoriaABuscar,"se han vendido",totalProductosXCategoria,"productos")

cantDias = obtenerDiasDeVentas(vecVentas)
print(cantVentas)

