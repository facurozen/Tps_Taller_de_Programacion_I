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

# Función que valida la categoría
def validarCategoria() :
    categoria = int(input("Ingrese la categoría del producto. 1 (Auto) - 2 (Moto) - 3 (Camioneta): ")) # Se le pide al usuario que ingrese la categoría del producto
    while categoria != 1 and categoria != 2 and categoria != 3 : # Validamos que la misma sea 1,2,3
        print("ERROR, el número de categoría no es válido. El mismo debe ser 1, 2 o 3") # Mensaje de error para avisarle que debe ser 1, 2 o 3
        categoria = int(input("Ingrese la categoría del producto. 1 (Auto) - 2 (Moto) - 3 (Camioneta): ")) # Se le vuelve a pedir que ingrese la categoría, y repite el ciclo hasta que la misma sea 1,2 o 3
    return categoria # La función devuelve la categoría validada

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
        while fechaDia < 0 or fechaDia> 31:  # Validamos que el día sea mayor a cero y menor a 31
            print("ERROR, el día debe ser mayor a 0 y menor a 31")  # Mensaje de error para avisarle que el día debe estar entre 1 y 31
            fechaDia = int(input("Ingrese el día que se realizó la venta: ")) # Se le vuelve a pedir que ingrese el día, y repite el ciclo hasta que el mismo este entre 1 y 31

    elif mes == 2 : # Verifica el mes de febrero
        while fechaDia < 0 or fechaDia> 29: # Validamos que el día sea mayor a cero y menor a 29, ya que 2024 es año bisiesto
            print("ERROR, el día debe ser mayor a 0 y menor a 29") # Mensaje de error para avisarle que el día debe estar entre 1 y 29 
            fechaDia = int(input("Ingrese el día que se realizó la venta: ")) # Se le vuelve a pedir que ingrese el día, y repite el ciclo hasta que el mismo este entre 1 y 29

    else: 
        while fechaDia < 0 or fechaDia> 30: # Verifica los meses que tienen 30 días 
            print("ERROR, el día debe ser mayor a 0 y menor a 30") # Mensaje de error para avisarle que el día debe estar entre 1 y 30
            fechaDia = int(input("Ingrese el día que se realizó la venta: ")) # Se le vuelve a pedir que ingrese el día, y repite el ciclo hasta que el mismo este entre 1 y 30
    return fechaDia

# Función para cargar los datos de cada venta
def cargarDatosVentas(cant) : # Pasamos como parametro la cantidad de ventas que ingreso el usurio que hubo en todo el mes

    # Creamos las listas vacías, que luego serán todas parte de la matriz vecVentas
    vecVentas = []

    idProducto = []
    categoria = []
    precio = []
    cantVendida = []  
    fechaMes = []
    fechaDia = []
 
    for i in range(cant) : # Ciclo for para ingresar todos los datos de cada venta. El mismo va hasta cant, que es la variable que pasamos como parametro
        print()
        print("N° VENTA:",i +1) # Print para saber que número de venta es
        print()
        
        id = validarId() # Llamamos a la función para ingresar el id, ya que la misma también se encarga de validarlo
        idProducto.append(id) # Se agrega a la lista de idProducto

        cat = validarCategoria() # Llamamos a la función para ingresar la categoría, ya que la misma también se encarga de validarla
        categoria.append(cat) # Se agrega a la lista de categoria

        prec = validarPrecio() # Llamamos a la función para ingresar el precio, ya que la misma también se encarga de validarlo
        precio.append(prec) # Se agrega a la lista de precio

        cantVen = validarCantidadVendida() # Llamamos a la función para ingresar la cantidad vendida de ese producto, ya que la misma también se encarga de validarlo
        cantVendida.append(cantVen) # Se agrega a la lista de cantVendida

        fechaM = validarFechaMes() # Llamamos a la función para ingresar la fecha del mes de la venta, ya que la misma también se encarga de validarla
        fechaMes.append(fechaM) # Se agrega a la lista de fechaMes

        fechaD = validarFechaDia(fechaM) # Llamamos a la función para ingresar la fecha del día de la venta, ya que la misma también se encarga de validarla
        fechaDia.append(fechaD) # Se agrega a la lista de fechaDia

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

# Se le pide al usuario que ingrese la cantidad de ventas que realizó en el último mes. Al ser ventas, el tipo de dato es entero, no puede ser decimal
cantVentas = int(input("Ingrese la cantidad de ventas realizadas en el último mes: "))

# Al tener que ingresar como minimo 10 ventas, si el usuario ingresa menos, se le vuelve a pedir
while cantVentas < 0 :
    print("ERROR, la cantidad de ventas mínima debe ser 10")
    cantVentas = int(input("Ingrese la cantidad de ventas realizadas en el último mes: "))

vecVentas = cargarDatosVentas(cantVentas) # Llamamos a la función que carga la matriz con cada venta, y la igualamos a vecVentas, por lo que ahora, vecVentas almacena todas las ventas

print()
categoriaABuscar = int(input("Ingrese el número de la categoría del producto que desea saber cuantos productos se han vendido en total. 1 (Auto) - 2 (Moto) - 3 (Camioneta): : ")) # Se le pide al usuario que ingrese la categoría que desea saber cuantos productos se han vendido
while categoriaABuscar != 1 and categoriaABuscar != 2 and categoriaABuscar != 3 : # Validamos que la misma sea 1,2,3
        print("ERROR, el número de categoría no es válido. El mismo debe ser 1, 2 o 3") # Mensaje de error para avisarle que debe ser 1, 2 o 3
        categoriaABuscar = int(input("Ingrese el número de la categoría del producto que desea saber cuantos productos se han vendido en total. 1 (Auto) - 2 (Moto) - 3 (Camioneta): : ")) # Se le pide al usuario que ingrese la categoría que desea saber cuantos productos se han vendido
print()

totalIngresos = calcularTotalIngresos(vecVentas) # Se iguala la función para calcular el total de ingresos a una variable, que almacena el número que devuelve la función
print("En el último mes, la empresa a generado ingresos de $",totalIngresos) # Se muestra por pantalla los ingresos

print()

totalProductosXCategoria = obtenerCantProductosCategoria(vecVentas,categoriaABuscar) # Se iguala la función para obtener la cantidad de productos vendidos de una categoría específica a una variable, que almacena el número que devuelve la función
print("De la categoria",categoriaABuscar,"se han vendido",totalProductosXCategoria,"productos") # Se muestra por pantalla la cantidad


cantDias = obtenerDiasDeVentas(vecVentas) # Se iguala la función para obtener los días distintos de venta a una variable, que almacena la lista de días distintos de ventas para poder utilizarla para calcualr el promedio de ingresos diarios

largoDias = len(cantDias) # Se obtiene el largo de la lista de cantDias, eso nos permite almacenar la cantidad de días de ventas distintos

promedio = calcularPromedioIngresosDiarios(vecVentas,largoDias) # Se iguala la función para obtener el promedio de ingresos diarios a una variable, que almacena el número que devuelve la función
print("El promedio de ingresos diarios es de:",promedio) # Se muestra por pantalla el promedio de ingresos diarios

print()
print("CARGA DE DATOS FINALIZADA ")