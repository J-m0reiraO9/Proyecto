#Se importan todos los datos usados
from Productos import Producto
from Ventas import Venta
from Clientes import Cliente
from Pagos import Pagos
from Envios import Envios
from Envios import Repartidor
from Indicadores_de_gestion import Indicadores_de_gestion
from Clientes import Juridico
import urllib.request
import dataclasses
import json
import os.path
path = './Salir.txt'

check_file = os.path.isfile(path)

print(check_file)

class EnhancedJSONEncoder(json.JSONEncoder):
        def default(self, o):
            if dataclasses.is_dataclass(o):
                return dataclasses.asdict(o)
            return super().default(o)
        
class Tienda:
    #Lista para almacenar las Apis
    def __init__(self):
        self.products = []
        self.indicadores_gestion = []
        self.Envios = []
        self.payments = []
        self.ventas = []
        self.clients = []
        self.juridicos = []
        self.repartidor = []
        
        if check_file != True:
            url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json"
            with urllib.request.urlopen(url) as response:
                if response.status == 200:
                    data = response.read()  # Lee los datos
                    json_data = json.loads(data)  # Lo convierte a diccionario
                    for data in json_data:
                        print(data)
                        name = data.get("name")
                        id = data.get("id")
                        description = data.get("description")
                        price = data.get("price")
                        category = data.get("category")
                        inventory = data.get("inventory")
                        compatible_vehicles = data.get("compatible_vehicles")
                        new_data = Producto(name, id, description, price, category, inventory, compatible_vehicles)
                        self.products.append(new_data)
                else:
                    print(f"Error: {response.status}")
        
        else: 
            with open("Salir.txt","r", encoding = "utf8") as file:
                x = file.read()
                y = json.loads(x)
                                  
                for cliente in y["Clientes"]:
                    nombre = cliente.get("nombre")
                    apellido = cliente.get("apellido")
                    cedula = cliente.get("cedula")
                    correo = cliente.get("correo")
                    telefono = cliente.get("telefono")
                    nuevo_cliente = Cliente(nombre, apellido, cedula, correo, telefono)
                    self.clients.append(nuevo_cliente)
                    
                for juridico in y["Juridico"]:
                    nombre_juridico = juridico.get("nombre_juridico")
                    rif = juridico.get("rif")
                    telefono = juridico.get("telefono")
                    correo_juridico = juridico.get("correo_juridico")
                    nuevo_juridico = Juridico(nombre_juridico, rif, correo_juridico, nuevo_juridico)
                    
                for pago in y["Pagos"]:
                    cliente = pago.get("cliente")
                    cedula = pago.get("cedula")
                    monto_pago = pago.get("monto_pago")
                    moneda = pago.get("moneda_pago")
                    tipo_de_pago = pago.get("tipo_de_pago")
                    fecha = pago.get("fecha")
                    nuevo_pago = Pagos(cliente, cedula, monto_pago, moneda, tipo_de_pago, fecha)
                    self.payments.append(nuevo_pago)
                
                
                for producto in y["Productos"]:
                    nombre = producto.get("nombre")
                    id = producto.get("id")
                    descripción = producto.get("descripción")
                    precio = producto.get("precio")
                    categoria = producto.get("categoria")
                    inventario = producto.get("inventario")
                    vehiculo_compatible = producto.get("vehiculo_compatible", [])
                    nuevo_producto = Producto(nombre, id, descripción, precio, categoria, inventario, vehiculo_compatible)
                    self.products.append(nuevo_producto)
                    
                for envio in y["Envios"]:
                    cliente = envio.get("cliente")
                    cedula = envio.get("cedula")
                    fecha_de_entrega = envio.get("fecha_de_entrega")
                    orden_compra = envio.get("orden_compra")
                    servicio_envio = envio.get("servicio_envio")
                    costo = envio.get("costo")
                    nuevo_envio = Envios(cliente, cedula, fecha_de_entrega, orden_compra, servicio_envio, costo)
                    self.Envios.append(nuevo_envio)
                    
                for reparte in y["Repartidor"]:
                    nombre = reparte.get("nombre")
                    apellido = reparte.get("apellido")
                    cedula = reparte.get("cedula")
                    edad = reparte.get("edad")
                    nuevo_repartidor = Repartidor(nombre, apellido, cedula, edad)
                    self.repartidor.append(nuevo_repartidor)
                
                for venta in y['Ventas']:
                    cliente = venta.get('cliente')
                    fecha_de_la_venta = venta.get('fecha_de_la_venta')
                    id = venta.get('id')
                    cantidad = venta.get()
                    metodo_de_pago = venta.get()
                    metodo_de_envio = venta.get()
                    nueva_venta = Venta(cliente, fecha_de_la_venta, id, cantidad, metodo_de_pago, metodo_de_envio)
                    self.ventas.append(nueva_venta)
                              
    def entrada_menu(self, mensaje, rango_maximo): #Menu otorgado por un try y que controla todo el codigo, aplicando polimorfismo
        try:
            num = int(input(mensaje))
            if num in range(1,rango_maximo):
                return num
            else:
                return None
        except: 
            return None    
        
    def app(self):
    #Constructor de la clase Tienda:
        while True: #Bucle del menu hasta que se rompa, usando el numero 7
            sección = self.entrada_menu("""!!!Bienvenido a nuestra tienda en linea!!! Seleccione un numero:
                                1. Productos
                                2. Venta
                                3. Cliente
                                4. Pagos
                                5. Envios
                                6. Indicadores de Gestión
                                7. Salir de la tienda
                                Ingrese aqui su numero -> """,8)
            if sección != None:
                if sección == 1:
                    self.menu_productos()
                elif sección == 2:
                    self.menu_ventas()
                elif sección == 3:
                    self.menu_clientes()
                elif sección == 4:
                    self.menu_pagos()
                elif sección == 5:
                    self.menu_envios()
                elif sección == 6:
                    self.menu_indicadores_de_gestion()
                elif sección == 7:
                    print("Vuelva Pronto")
                    with open("Salir.txt","w", encoding = "utf8") as file:
                        diccionario = {
                            "Productos": self.products,
                            "Ventas": self.ventas,
                            "Clientes": self.clients,
                            "Pagos": self.payments,
                            "Envios": self.Envios,
                            "Indicadores de Gestion": self.indicadores_gestion,
                            "Juridico" : self.juridicos
                            }
                        file.write(json.dumps(diccionario, indent = 4, cls=EnhancedJSONEncoder))
                    break
            else:
                print("Selección Invalida")   
                               
    def menu_productos(self):
        #Constructor de la función menu de producto
         while True:
            print("Bienvenidos al area de productos:")
            sección = self.entrada_menu("""¿Que desea Realizar?: 
                                1. Agregar nuevo productos
                                2. Busqueda de productos
                                3. Modificar información
                                4. Eliminar productos
                                5. Volver al inicio
                                Ingreselo aqui -> """, 6)
            if sección != None:
                if sección == 1:
                    #Registro para almacenar los repuestos
                    print("-----Bienvenido a la parte de incorporación de piezas-----")
                    nuevo_productos = []
                    vehiculo_compatible = []
            
                    nombre = input("Introduzca el nombre del producto: ")
                    
                    id = int(input("Ingrese el ID del vehiculo (Que sea un valor del 1 al 50): "))
                    while not (id >= 1 and id <=50):
                        id = int(input(" !!ERROR!!, vuelve a ingresar el ID del vehiculo (Que sea un valor del 1 al 50): "))
                    descripción = input("Introduzca la descripción del producto: ")
                    try:
                        precio = float(input("Introduzca el precio del vehiculo(Numero decimal): "))
                    except ValueError:
                        precio = float(input(" !!!ERROR!!! Introduzca el precio del vehiculo: "))
                    categoria = input("Ingrese la categoria del vehiculo: ")
                    
                    try:
                        inventario = int(input("Ingrese la cantidad en el inventario: "))
                    except ValueError:
                        inventario = int(input("!!!ERROR!!! Ingrese la cantidad en el inventario: "))
                    # Se crea un objeto que recopila todos los atributos de la clase otorgados por el cliente
                    nuevo_productos = Producto(nombre, id, descripción, precio, categoria, inventario, vehiculo_compatible)
                    self.products.append(nuevo_productos)
            
                elif sección == 2:
                    #En esta parte se buscan las piezas
                    print("-----Bienvenido a busqueda de piezas-----")
                    while True:
                        sección = self.entrada_menu("""Indique un numero para buscar las piezas en el inventario: 
                                                                1. Categoría
                                                                2. Precio 
                                                                3. Nombre
                                                                4. Disponibilidad de inventario
                                                                5. Volver a inicio
                                                                Ingreselo aqui -> """,6) #Busca 
                        if sección != None: 
                            if sección == 1:
                                categoria = input('Ingrese la categoria del vehiculo: ')
                                for category in self.products:
                                    if category.categoria == categoria:
                                        print(f"La categoria {category.categoria} pertenece a la lista")
                                    else:
                                        print(f"No se ha encontrado la categoria: {categoria}")
                            elif sección == 2:
                                precio = float(input('Ingrese el precio del producto: '))
                                for prize in self.products:
                                    if prize.precio == precio:
                                        print(f"El precio {prize.precio} pertenece a la lista")
                                    else:
                                        print(f"No se ha encontrado el precio: {precio}")
                            elif sección == 3:
                                nombre = input('Ingrese el nombre del producto')
                                for name in self.products:
                                    if name.nombre == nombre:
                                        print(f"El nombre del {name.nombre} del producto pertenece a la lista")
                                    else:
                                        print(f"No se ha encontrado el nombre de: {nombre}")
                            elif sección == 4:
                                inventario = int(input('Ingrese la cantidad en el inventario: '))
                                for disponibilidad in self.products:
                                    if disponibilidad.inventario == inventario:
                                        print(f"La disponibilidad del producto en el inventario es de: {disponibilidad.inventario}")
                                    else: 
                                        print(f"No se ha encontrado disponiblidad en el {inventario}")
                            elif sección == 5:
                                break  
                        else:
                            print("Selección Invalida, introduzca un valor correspondiente al menu")
                elif sección == 3:
                    # En esta sección se podra modificar información de cada producto
                    print("-----Bienvenido a la modificación de productos existentes-----")
                    while True:
                        sección = self.entrada_menu("""Indique un numero para modificar un producto: 
                                                                1. Nombre
                                                                2. Descripción
                                                                3. Precio
                                                                4. Categoria
                                                                5. Inventario
                                                                6. Vehiculo Compatible
                                                                7. Volver a inicio
                                                                Ingreselo aqui -> """,8)
                        if sección != None:
                            if sección == 1:
                                nuevo_nombre = input("Nuevo nombre de la pieza: ").capitalize()
                                # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                new_product = Producto(nuevo_nombre,descripción, precio, categoria, inventario, vehiculo_compatible)
                                self.products.append(new_product)
                            elif sección == 2:
                                nueva_description = input("Nueva descripción de la pieza: ").capitalize()
                                # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                new_product= Producto(nombre, nueva_description, precio, categoria, inventario, vehiculo_compatible)
                                self.products.append(new_product)
                            elif sección == 3:
                                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                                while True:
                                    if nuevo_precio != float:
                                        print("Selección invalida")
                                    else:
                                        # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                        new_product= Producto(nombre, descripción, nuevo_precio, categoria, inventario, vehiculo_compatible)
                                        self.products.append(new_product)
                                        break
                            elif sección == 4:
                                nueva_categoria = input("Introduzca la modificación de la categoria: ").capitalize()
                                # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                new_product= Producto(nombre, descripción, precio, nueva_categoria, inventario, vehiculo_compatible)
                                self.products.append(new_product)
                            elif sección == 5:
                                    nuevo_inventario = (input("Ingrese la nueva descripción de inventario: "))
                                    new_product= Producto(nombre, descripción, precio, categoria, nuevo_inventario, vehiculo_compatible)
                                    self.products.append(new_product)
                            elif sección == 6:
                                nuevo_vehiculo = input("Ingrese un nuevo modelo de vehiculo: ")
                                # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                new_product= Producto(nombre, descripción, precio, categoria, inventario, nuevo_vehiculo)
                            elif sección == 7:
                                break
                        else:
                            print("Seleccion invalida, introduzca un valor correspondiente al menu")
                elif sección == 4:
                    # En esta sección se podran eliminar información de cada producto
                    print("-----Bienvenido a la parte donde eliminas piezas")
                    while True:
                        sección = self.entrada_menu("""Indique un numero para eliminar un producto: 
                                                                1. Nombre
                                                                2. Descripción
                                                                3. Precio
                                                                4. Categoria
                                                                5. Inventario
                                                                6. Vehiculo Compatible
                                                                7. Volver a inicio
                                                                Ingreselo aqui -> """,8)
                        if sección != None:
                            if sección == 1:                               
                                for i in enumerate(self.products):
                                    self.nombre.pop(i)
                                    print("Se ha eliminado el producto de manera exitosa")
                            elif sección == 2:
                                for i in enumerate(self.products):
                                    self.descripción.pop(i)
                                    print("Se ha eliminado la descripción del producto de manera exitosa")
                            elif sección == 3:
                                for i, precio in enumerate(self.products):
                                    self.precio.pop(i)
                                print("Se ha eliminado el usuario de manera exitosa")
                            elif sección == 4:
                                for i, categoria in enumerate(self.products):
                                    self.categoria.pop(i)
                                print("Se ha eliminado el usuario de manera exitosa")
                            elif sección == 5:
                                for i, inventario in enumerate(self.products):
                                    self.inventario.pop(i)
                                print("Se ha eliminado el usuario de manera exitosa")
                            elif sección == 6:
                                for i, vehiculo_compatible in enumerate(self.products):
                                    self.vehiculo_compatible.pop(i)
                                print("Se ha eliminado el usuario de manera exitosa")
                            elif sección == 7:
                                break
                        else:
                            print("Seleccion invalida, introduzca un valor correspondiente al menu")
                elif sección == 5:
                    break
            else:
                print("Selección Invalida, introduzca un valor correspondiente al menu")    
            
    def menu_ventas(self):
         #Constructor de la función menu de ventas
        while True:
            print("Bienvenido al area de Ventas:") 
            sección = self.entrada_menu("""¿Que desea realizar?:
                    1. Registro de Venta
                    2. Generación de facturas por cada compra
                    3. Buscador de Ventas
                    4. Volver al Inicio
                    Ingreselo aqui -> """,5)
            if sección != None:
                if sección == 1:
                # Sección donde podras y registrar ventas
                    print("----- Registro de Ventas -----")
                    
                    cliente = (input("""Eres cliente:
                                                - Natural 
                                                - Juridico
                                                Ingrese su opcion: """)).lower()
                    while cliente not in ['natural', 'juridico']:
                        cliente = input("""Error!!!. Ingrese una opcion valida: 
                                       - Natural
                                       - Juridico
                                       Ingreselo aqui -> """).lower()
                    fecha_de_la_venta = input("Ingrese la fecha de la venta (aaaa/mm/dd): ")
                    id= int(input("Ingrese el ID del producto: "))
                    while not (id >= 1 and id <=50) :
                        id = int(input(" !!ERROR!!, vuelve a ingresar el ID del vehiculo (Que sea un valor del 1 al 50): "))
                    try:
                        cantidad = int(input("Ingrese la cantidad que quiere comprar (Ejm: 7): "))
                    except ValueError:
                        cantidad = int(input(" !!ERROR!! Ingrese la cantidad que quiere comprar (Ejm: 7): "))
                      
                    metodo_de_pago = (input("""Ingrese el metodo de pago:
                                                                        - Bolivares
                                                                        - Divisas 
                                                                        Ingrese la opcion correspondiente -> """)).lower()
                    while metodo_de_pago not in ['bolivares', 'divisas']:  
                        metodo_de_pago = input(""" !!!ERROR !!! Ingrese el metodo de pago:
                                                                        - Bolivares
                                                                        - Divisas extranjeras
                                                                        Ingrese la opcion correspondiente -> """).lower ()  
                    metodo_de_envio = (input("""  Introduzca el metodo de envio:
                                                                            1.Zoom
                                                                            2.Delivery
                                                                            Ingrese el numero correspondiente -> """)).lower()
                    while metodo_de_envio not in ['zoom', 'delivery']: 
                         metodo_de_envio = (input(""" !!!ERROR !!! Ingrese el metodo de pago:
                                                                        - Bolivares
                                                                        - Divisas extranjeras
                                                                        Ingrese numero correspondiente -> """)).lower()
                    product = None
                    for busqueda in self.products:
                        if busqueda.id == id:
                            print(busqueda.id)
                            product = busqueda 
                            
                    if product != None:
                        # Se crea un objeto que recopila todos los atributos de la clase otorgados por el cliente                     
                        nueva_venta = Venta(cliente, cantidad, fecha_de_la_venta, id, metodo_de_pago, metodo_de_envio)
                        self.ventas.append(nueva_venta)
                    else: 
                        print("Selección invalida")
                        
                    subtotal = cantidad * product.precio
                    print(f"El subtotal es: {subtotal}")
                    total = subtotal
                    
                    iva = 0.16
                    IGTF = 0.03
                    descuento_juridico = 0.05
                    
                    if cliente == 2:
                        print(f"Descuento juridico: {total * descuento_juridico}")
                        total -= total * descuento_juridico
                           
                    print(f"El iva es: {total* iva}")    
                    total += total * iva
                    
                    if metodo_de_pago == 2:
                        print(f"El IGTF es: { total * IGTF}")
                        total += total * IGTF
                        
                    print(f"El total es {total}")
                                 
                elif sección == 2:
                # Sección donde se generan las facturas por cada compra
                    print("----- Factura -----")
                    print(f"1. Nombre = {cliente}")
                    print(f"2. Fecha: {fecha_de_la_venta}")
                    print("------------------------------------------")
                    print(f"3.ID: {id}")
                    print(f"4.Cantidad: {cantidad}")
                    print("------------------------------------------")
                    print(f"5.Metodo de pago: {metodo_de_pago}")
                    print(f"6.Metodo de envio: {metodo_de_envio}")
                    print("-----------------------------------------------------")
                    print(f"Subtotal: {subtotal}")
                    print(f"Iva: {iva}")
                    print("-----------------------------------------------------")
                    print(f"IGTF : {IGTF}")
                    print(f"Descuento Juridico: {descuento_juridico}")
                    print("-----------------------------------------------------")
                    print(f"Total: {total}")
                    
                elif sección == 3:
                # Sección a la que podras buscar a los clientes
                    print("----- Bienvenido a la busqueda de ventas ----- ")
                    while True:
                        selección = self.entrada_menu("""Indique un numero para buscar la venta: 
                                                                1. Cliente 
                                                                2. Fecha de la venta
                                                                3. Volver a inicio
                                                                Ingreselo aqui -> """,4)
                        if sección != None: 
                            if selección == 1: 
                                cliente = (input(f"""Que tipo de cliente es: 
                                                    1. Natural
                                                    2. Juridico
                                                    Ingrese su opcion aqui -> """)).lower()                               
                                for usuario in self.ventas:
                                    if usuario.cliente == cliente:
                                        print(f"El cliente {usuario.cliente} se ha encontrado")
                                        break
                                    else:
                                        print(f"No se ha encontrado el cliente: {cliente}")
                            elif selección == 2:
                                fecha = input("Seleccione la fecha de venta del producto (aaaa/mm/dd): ")
                                for date in self.ventas:
                                    if date.fecha == fecha_de_la_venta:
                                        print(f"La fecha de la venta fue el {date.fecha}")   
                                        break
                                    else: 
                                        print(f"No se ha encontrado la fecha: {fecha_de_la_venta}")
                            elif selección == 3:
                                break
                elif sección == 4:
                    break
            else:
                print("Selección Invalida")   
    def menu_clientes(self):
         #Constructor de la función menu de clientes
        while True:
            print("Bienvenido a la función Clientes!!") #Se pregunta al usuario que opcion quiere visualizar
            sección = self.entrada_menu("""¿Que desea realizar?:  
                                1. Registro de cliente
                                2. Modificar información del cliente 
                                3. Eliminar cliente
                                4. Busqueda de cliente
                                5. Volver al inicio
                                Ingrese el numero aqui -> """, 6)
            if sección != None:
                if sección == 1:
            # Sección donde podras registrar a los clientes
                    print("----- Bienvenido al registro de clientes -----") 
                    while True:
                        sección= self.entrada_menu("""Indique un numero: 
                                                        1. Cliente Natural
                                                        2. Cliente Juridico
                                                        3. Salir
                                                        Ingreselo aqui ->""",4) # Se le da la opción al cliente al registrar si es natural o juridico
                        if sección != None:   
                            if sección == 1:
                                nombre = input("Cual es tu nombre: ")
                                apellido = input("Cual es tu apellido: ")
                                try: 
                                    cedula = int(input("Ingrese la cedula (No use puntos ni letras): "))
                                except ValueError:
                                    cedula = int(input("Error!!, Introduzca un número entero (ejm: 30291432):"))
                                correo = input("Cual es tu correo?: ")
                                telefono = input("Indique su numero telefonico: ")
                                # Se crea un objeto que recopila todos los atributos de la clase otorgados por el cliente
                                new_client = Cliente(nombre, apellido, cedula, correo, telefono) 
                                
                                encontrado = False #Se verifica si el cliente se registra con la misma cedula
                                for client in self.clients:
                                    if client.cedula == cedula:
                                        encontrado = True
                                if encontrado:
                                    print("Esa cedula ya existe")
                                else:
                                    self.clients.append(new_client) #Filtro para saber si el rif que se va a agregar ya existe
                                                                      
                            elif sección == 2:
                                nombre_juridico = input("Ingrese el nombre juridico: ")
                                try:
                                    rif = int(input("Ingrese el Rif de la empresa: "))
                                except ValueError:
                                    rif = int(input(" !ERROR! Ingrese el Rif de la empresa: "))
                                telefono = (input("Ingrese el numero de Telefono de la empresa: "))
                                correo_juridico = input("Ingrese el Correo de la empresa: ")
                                new_company = Juridico(nombre_juridico, rif, telefono, correo_juridico)
                                
                                encontrado_rif = False #Filtro para saber si el rif que se va a agregar ya existe
                                for juridico in self.juridicos:
                                    if juridico.rif == rif:
                                        encontrado_rif = True
                                if encontrado_rif:
                                    print("El rif ya existe")
                                else:
                                    self.juridicos.append(new_company)
                            elif sección == 3:
                                break
                        else:
                            print("Seleccion invalida")
                elif sección == 2:
                # Sección donde podras registar la información del cliente
                    print("----- Bienvenido a la Modificación de Información del cliente -----")
                    while True: 
                        #Primero se consulta si el cliente es Natural o Juridico
                        sección = self.entrada_menu("""Quisiera modificar un aspecto de: 
                                                        1. Cliente Natural
                                                        2. Cliente Juridico
                                                        3. Volver al inicio
                                                        Ingreselo aquí -> """,4) 
                        if sección != None:
                            if sección == 1: 
                                buscar = int(input("Ingrese su cedula: ")) 
                                #Se le pide al usuario la cedula para que pueda modificar sus datos
                                if buscar != int and buscar != cedula:
                                    print("Selección invalida")
                                else:
                                    sección = self.entrada_menu("""Seleccione un numero para modificar los datos: 
                                                            1. Nombre
                                                            2. Apellido
                                                            3. Cedula
                                                            4. Correo
                                                            5. Telefono
                                                            6. Volver a inicio
                                                            Ingreselo -> """,7)
                                    if sección != None:         
                                        if sección == 1:
                                            nuevo_nombre = input("Selecciona su nuevo nombre: ")
                                            # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                            new_client = Cliente(nuevo_nombre, apellido, cedula, correo, telefono)
                                        elif sección == 2: 
                                            nuevo_apellido = input("Seleccione su nuevo apellido: ")
                                            # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                            new_client = Cliente(nombre, nuevo_apellido, cedula, correo, telefono)
                                        elif sección == 3:
                                            nueva_cedula = int(input("Introduzca su nuevo numero de cedula: "))
                                            if nueva_cedula != int:
                                                print("Selección invalida")
                                            # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                            new_client = Cliente(nombre, apellido, cedula, correo, telefono)
                                        elif sección == 4:
                                            nuevo_correo = input("Introduzca su nuevo correo electronico: ")
                                            # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                            new_client = Cliente(nombre, apellido, cedula, nuevo_correo, telefono)
                                        elif sección == 5:
                                            nuevo_telefono = int(input("Seleccione un nuevo numero de telefono: "))
                                            # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                            new_client = Cliente(nombre, apellido, cedula, correo, nuevo_telefono)
                                        elif sección == 6:
                                            break  
                            elif sección == 2:
                                buscar_rif = int(input("Escriba el rif de la empresa: "))
                                if buscar_rif != int or buscar_rif != rif:
                                    print("Selección invalida")
                                else:
                                    sección = self.entrada_menu("""Seleccione un numero para modificar los datos: 
                                                                1. Nombre de la empresa
                                                                2. Rif 
                                                                3. Telefono
                                                                4. Correo
                                                                5. Volver a inicio
                                                                Ingreselo -> """,6)
                                    if sección != None:
                                            if sección == 1:
                                                nuevo_nombre_juridico = input("Introduzca el nuevo nombre de la empresa: ")
                                                new_company = Juridico(nuevo_nombre_juridico, rif, telefono, correo)
                                            elif sección == 2:
                                                nuevo_rif = int(input("Introduce el nuevo rif de la empresa: "))
                                                new_company = Juridico(nombre_juridico, nuevo_rif, telefono, correo)
                                            elif sección == 3:
                                                nuevo_telefono = input("Introduzca el nuevo numero: ")
                                                new_company = Juridico(nombre_juridico, rif, nuevo_telefono, correo)
                                            elif sección == 4:
                                                nuevo_correo = input("Introduzca el nuevo correo de la empresa: ")
                                                new_company = Juridico(nombre_juridico, rif, telefono, nuevo_correo)
                                            elif sección == 5:
                                                break           
                            elif sección == 3:
                                break
                        else:
                            print("Seleccion invalida")        
                elif sección == 3:
                # Sección donde puedes eliminar clientes, eliminando a partir de su cedula
                    print("----- Bienvenido a la eliminación del registro de cliente -----")
                    sección = self.entrada_menu("""Seleccione un numero para eliminar datos: 
                                                        1. Cedula
                                                        2. Rif
                                                        3. Volver a Inicio
                                                        Ingreselo -> """,4)
                    if sección != None:
                        if sección == 1:
                            eliminar = int(input("Escriba su cedula (No use puntos ni letras): "))
                            #Recorremos i y cliente en self.clients, para eliminar la variable ya antes asignadas
                            for i, cliente in enumerate(self.clients):
                                if cliente.cedula == eliminar:
                                    self.clients.pop(i)
                                    print("Se ha eliminado el usuario de manera exitosa")
                        
                        elif sección == 2:
                            eliminar = int(input("Escriba el rif de la empresa: "))
                            for j, empresa in enumerate(self.juridicos):
                                if empresa.rif == eliminar:
                                    self.juridicos.pop(j)
                                    print("Se ha eliminado el usuario de manera exitosa")
                        elif sección == 3:
                            break
                    else: 
                        print("Seleccion invalida")
                elif sección == 4:
                # Sección donde podras buscar a los clientes
                    print("----- Bienvenido a la busqueda de cliente -----")
                    while True:
                        sección = self.entrada_menu("""Indique un numero para buscar el cliente: 
                                                                1. Cedula 
                                                                2. Rif
                                                                3. Correo Electronico (Persona Natural)
                                                                4. Correo Electronico (Persona Juridica)
                                                                5. Volver a inicio
                                                                Ingeselo aquí -> """,6) #Busca el usuario catalogando segun la cedula, rif y correo electronico
                        if sección != None:
                            if sección == 1: 
                                cedula = int(input("Indique su cedula (No use puntos ni letras): "))
                                for client in self.clients:
                                    if client.cedula == cedula:
                                        print(f"La cedula {cedula} pertenece a {client.nombre} {client.apellido}")
                                        break
                                    else:
                                        print(f"No se ha encontrado la cedula: {cedula}")
                            elif sección == 2:
                                rif = int(input("Indique su rif: "))
                                for company in self.juridicos:
                                    if company.rif == rif:
                                        print(f"El rif {rif} pertenece a {company.nombre_juridico}")
                                        break
                                    else:
                                        print(f"No se ha encotrado el rif: {rif}")      
                            elif sección == 3:
                                correo = input("Indique su correo electronico: ")
                                for mail in self.clients:
                                    if mail.correo == correo:
                                        print(f"El correo {correo} pertenece a {client.nombre} {client.apellido}")
                                        break
                                    else:
                                        print(f"No encontramos el correo: {correo}")
                            elif sección == 4:
                                correo = input("Indique su correo electronico: ")
                                for mail_juridico in self.juridicos:
                                    if mail_juridico.correo == correo_juridico:
                                        print(f"El correo juridico {correo_juridico} pertenece a {company.nombre_juridico}")
                                        break
                                    else:
                                        print(f"No encontramos el correo juridico: {correo}") 
                            elif sección == 5:
                                break
                        else:
                            print("Selección Invalida")  #El else pertenece al elif de la selección 5
                elif sección == 5:
                    break
            else:
                print("Selección Invalida")
                           
    def menu_pagos(self):
         #Constructor de la función menu de pagos
        while True:
            print("Bienvenido a la función de pago de la Tienda!!!")
            sección = self.entrada_menu("""¿Que desea realizar?:
                            1. Registro de pagos
                            2. Busqueda de pagos
                            3. Volver al inicio
                            Ingreselo aqui -> """, 4)
            if sección != None:
                if sección == 1:
            #Sección en donde registras los pagos hechos.
                    print("----- Bienvenido al lugar donde puedes registrar los pagos -----")
                    cliente = input("Ingrese su nombre: ")
                    try: 
                        cedula = int(input("Ingrese la cedula (No use puntos ni letras): ")) 
                    except ValueError:
                        cedula = int(input("Error!!, Introduzca un número entero (ejm: 30291432):"))
                    try:
                        monto_pago = float(input("Ingrese el monto del pago (No use letras): "))
                    except ValueError:
                        monto_pago = float(input("Error, Ingrese un valor con numero decimal (ejm: 4.32): "))
                    moneda = input("""Ingrese la moneda de pago:
                                   - Bolivares
                                   - Euros
                                   - Dolares
                                   Ingreselo aqui -> """).lower()
                    while moneda not in ['bolivares', 'euros', 'dolares']:
                        moneda = input("""Error!!!. Ingrese una moneda de la lista: 
                                       - Bolivares
                                       - Euros
                                       - Dolares
                                       Ingreselo aqui -> """).lower()
                    tipo_de_pago = input("""Ingrese el medio de pago: 
                                        -Punto de Venta 
                                        -Pago Movil
                                        -Transferencia
                                        -Zelle
                                        -Efectivo.
                                        Ingreselo aqui -> """).lower()
                    while tipo_de_pago not in ['punto de venta', 'pago movil', 'transferencia', 'zelle', 'efectivo']:
                        tipo_de_pago = input("""Error. Ingrese una opción entre:
                                             -Punto de venta
                                             -Pago movil,
                                             -Transferenci
                                             -Zelle
                                             -Efectivo
                                            Ingreselo aqui -> """).lower()
                    fecha = input("Ingrese la fecha de pago (aaaa-mm-dd): ") #En lo que en parentesis significa: 
                                                                                     # a = Años
                                                                                     # m = meses
                                                                                     # d = dias
                    new_payment = Pagos(cliente, cedula, monto_pago, moneda, tipo_de_pago, fecha)
                    self.payments.append(new_payment)
              
                elif sección == 2:
            #En esta sección se podran Buscar los pagos anteriormente hechos
                    print("----- Bienvenido a la busqueda de pagos -----") 
                    while True:
                        sección = self.entrada_menu("""Indique un numero para buscar el cliente: 
                                                                1. Cliente
                                                                2. Fecha
                                                                3. Tipo de Pago
                                                                4. Moneda de Pago
                                                                5. Volver a inicio
                                                                Ingreselo aqui -> """,6)
                        if sección != None:
                            if sección == 1: 
                                cliente = input("Ingrese su nombre: ") 
                                for client in self.payments:
                                    if client.cliente == cliente:
                                        print(f"Se ha encontrado el cliente de nombre: {client.cliente}")
                                        break
                                    else:
                                        print(f"No se ha encontrado el cliente de nombre {cliente} ")
                            elif sección == 2:
                                fecha = input("Ingrese la fecha de la compra(aaaa-mm-dd): ")
                                for date in self.payments:
                                    if date.fecha == fecha:
                                        print(f"El producto se compro el {date.fecha}")
                                        break
                                    else:
                                        print(f"El producto no se compro el {fecha}")   
                            elif sección == 3:
                                tipo_de_pago = input("Ingrese el tipo de pago: ")
                                for pago in self.payments:
                                    if pago.tipo_de_pago == tipo_de_pago:
                                        print(f"El pago fue por {pago.tipo_de_pago}")
                                        break
                                    else:
                                        print(f"No se ha encontrado ningun pago: {tipo_de_pago}")
                            elif sección == 4:
                                moneda = input("Ingrese la moneda de pago: ")
                                for coin in self.payments:
                                    if coin.moneda == moneda:
                                        print(f"El pago se hizo con {coin.moneda}")
                                        break
                                    else:
                                        print(f"No se encontro ningun pago en {moneda}")
                            elif sección == 5:
                                break
                        else:
                            print("Selección invalida, seleccione u")
                elif sección == 3:
                    break
            else:
                print("Selección Invalida")
    def menu_envios(self):
         #Constructor de la función menu de envios
        while True:
            print("Bienvenido a la zona de envios!!")
            sección = self.entrada_menu("""¿A que desea acceder?: 
                            1. Registro de envios
                            2. Busqueda de envio
                            3. Volver a inicio
                            Ingreselo aqui -> """,4)
            if sección != None:
                if sección == 1:
                     # Lugar donde podras registrar los registros de envios
                    print("----- Bienvenido al registro de envios -----")
                    cliente = input("Ingrese su nombre: ")
                    try: 
                        cedula = int(input("Ingrese la cedula (No use puntos ni letras): ")) 
                    except ValueError:
                        cedula = int(input("Error!!, Introduzca un número entero (ejm: 30291):"))
                    fecha_de_entrega = input("Ingrese la fecha de entrega(aaaa/mm/dd): ")
                    try:
                        orden_compra = int(input("Cual es el ID orden de compra (Ejm: 5): "))
                    except ValueError:
                        orden_compra = int(input(" !!!ERROR!!!, Seleccione cual es el ID orden de compra (Ejm: 5): "))
                    servicio_envio = input("Cual es el servicio de envio (Delivery o Zoom): ").lower()
                    while servicio_envio not in ['delivery', 'zoom']:
                        servicio_envio = input("Error. Ingrese una opción entre Delivery o Zoom: ").lower()
                    try:
                        costo = float(input("Introduzca el costo del envio (Use un punto para usar los decimales): "))
                    except ValueError:
                        costo = float(input("Introduzca el costo del envio (Use un punto para usar los decimales): "))
                    new_shipment = Envios(cliente, cedula, fecha_de_entrega, orden_compra, servicio_envio, costo)
                    # Se crea un objeto que recopila todos los atributos de la clase otorgados por el cliente
                    self.Envios.append(new_shipment)
                    
                    if servicio_envio == "delivery": #Si el usuario dice que el servicio de envio es un delivery    
                        print("-----Bienvenido al registro del repartidor-----")
                        nombre = input("Ingresa el nombre del repartidor: ")
                        apellido = input("Ingresa el apellido del repartidor: ")
                        try:
                            cedula = int(input("Ingresa la cedula del repartidor: "))
                        except ValueError:
                            cedula = int(input("Error!!, Introduzca un número entero (ejm: 30291):"))
                        edad = int(input("Ingresa la edad del repartidor: "))
                        try:
                            edad = int(input("Ingresa la cedula del repartidor: "))
                        except ValueError:
                            edad = int(input("!!Error!!, Ingrese una edad valida (ejm: 20): "))
                        new_service = Repartidor(nombre, apellido, cedula, edad)
                        self.repartidor.append(new_service)
                        
                elif sección == 2:
                     # Sitio donde podras buscar los envios
                    print("----- Bienvenido a la busqueda de envios -----")
                    sección = self.entrada_menu("""Ingrese un numero para buscar el envio: 
                                                  1. Cliente
                                                  2. Fecha
                                                  3. Salir
                                                  Ingreselo aqui -> """,4)
                    if sección != None:
                        if sección == 1:
                             nombre = (input("Ingrese su nombre: "))
                             # Se recorre la lista para encontrar un atributo de esa.
                             for name in self.Envios:
                                if name.cliente == nombre:
                                    print(f"El envio se hizo a nombre de {name.cliente}")
                                    break
                                else:
                                    print(f"No se encontro ningun envio a nombre de {nombre}")
                        elif sección == 2: 
                            fecha_de_entrega = int(input("Ingrese su cedula: "))
                            for date in self.Envios:
                                if date.fecha_de_entrega == fecha_de_entrega:
                                    print(f"El envio se hizo en la fecha: {date.fecha_de_entrega}")
                                else:
                                    print(f"No se encontro ningun envio en esa fecha {fecha_de_entrega}")
                        elif sección == 3:
                            break
                    else:
                        print("Selección invalida")
                elif sección == 3:
                    break
            else:
                print("Selección Invalida")

    def menu_indicadores_de_gestion(self):
         #Constructor de la función menu de indicadores de gestión
        while True:
            print("Bienvenido a la sección de Indicadores de gestion!!")
            sección = self.entrada_menu(""" 
                            1. Informes de Ventas
                            2. Informes de Pagos
                            3. Informes de envios
                            4. Graficas con las respectivas estadisticas
                            5. Volver a inicio
                            Ingreselo aqui -> """,6)
            if sección == None:
                if sección == 1:
            #Lugar donde podras consultar los registros de ventas pasados
                    print("-----Bienvenido a los informes de ventas -----")
                elif sección == 2:
            #Lugar donde puedes consultar los registros de pago
                    print("----- Bienvenido a los Informes de pago -----")
                elif sección == 3:
            #Lugar donde revisaras los registros de envios
                    print("----- Bienvenido al registro de envios -----")
                elif sección == 4:
            #Lugar donde veras graficas con las respectivos datos
                    print("-----")
                elif sección == 5:
                    break
            else:
                print("Selección Invalida")        
