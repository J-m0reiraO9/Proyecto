#Se importan todos los datos usados
from Productos import Producto
from Ventas import Venta
from Clientes import Cliente
from Pagos import Pagos
from Envios import Envios
from Envios import Repartidor
from Clientes import Juridico

import urllib.request
import dataclasses
import json
import os.path
import datetime
import matplotlib.pyplot as plt
import pandas as pd
path = './Salir.txt'

check_file = os.path.isfile(path)
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
                        name = data.get("name")
                        id = data.get("id")
                        description = data.get("description")
                        price = data.get("price")
                        category = data.get("category")
                        inventory = data.get("inventory")
                        new_data = Producto(name, id, description, price, category, inventory)
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
                    self.juridicos.append(nuevo_juridico)
                    
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
                    nuevo_producto = Producto(nombre, id, descripción, precio, categoria, inventario)
                    self.products.append(nuevo_producto)
                    
                for envio in y["Envios"]:
                    cliente = envio.get("cliente")
                    cedula = envio.get("cedula")
                    fecha_de_entrega = envio.get("fecha_de_entrega")
                    orden_compra = envio.get("orden_compra")
                    servicio_envio = envio.get("servicio_envio")
                    producto = envio.get("producto")
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
                    cantidad = venta.get('cantidad')
                    metodo_de_pago = venta.get('metodo_de_pago')
                    metodo_de_envio = venta.get('metodo_de_envio')
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
                    with open("salir.txt","w", encoding = "utf8") as file:
                        diccionario = {
                            "Productos": self.products,
                            "Ventas": self.ventas,
                            "Clientes": self.clients,
                            "Pagos": self.payments,
                            "Envios": self.Envios,
                            "Repartidor": self.repartidor,
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
                    print("-----Bienvenido a la parte de incorporación de productos-----")
                    nuevo_productos = []
                    vehiculo_compatible = []
                    nombre = input("Introduzca el nombre del producto: ")
                    try:
                        id = int(input("Ingrese el ID del producto: "))
                    except ValueError:
                        id = int(input("!!!ERROR!!! Ingrese el ID del producto: "))
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
                    
                    product = None
                    for busqueda in self.products:
                        if busqueda.id == id:
                            print(busqueda.id)
                            product = busqueda 
                    
                    if product != None:
                        nuevo_productos = Producto(nombre, id, descripción, precio, categoria, inventario)
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
                                                                Ingreselo aqui -> """,6) 
                        if sección != None: 
                            if sección == 1:
                                categoria = input('Ingrese la categoria del vehiculo: ')
                                for category in self.products['category']:
                                    if category.categoria == categoria:
                                        print(f"La categoria {category.categoria} pertenece a la lista")
                                    else:
                                        print(f"No se ha encontrado la categoria: {categoria}")
                            elif sección == 2:
                                precio = float(input('Ingrese el precio del producto: '))
                                for prize in self.products['price']:
                                    if prize.precio == precio:
                                        print(f"El precio {prize.precio} pertenece a la lista")
                                    else:
                                        print(f"No se ha encontrado el precio: {precio}")
                            elif sección == 3:
                                nombre = input('Ingrese el nombre del producto: ')
                                for name in self.products['name']:
                                    if name.nombre == nombre:
                                        print(f"El nombre del {name.nombre} del producto pertenece a la lista")
                                    else:
                                        print(f"No se ha encontrado el nombre de: {nombre}")
                            elif sección == 4:
                                inventario = int(input('Ingrese la cantidad en el inventario: '))
                                for disponibilidad in self.products['inventory']:
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
                                                                6. Volver a inicio
                                                                Ingreselo aqui -> """,7)
                        if sección != None:
                            if sección == 1:
                                nuevo_nombre = input("Nuevo nombre de la pieza: ").capitalize()
                                # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                new_product = Producto(nuevo_nombre,descripción, precio, categoria, inventario)
                                self.products.append(new_product)
                            elif sección == 2:
                                nueva_description = input("Nueva descripción de la pieza: ").capitalize()
                                # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                new_product= Producto(nombre, nueva_description, precio, categoria, inventario)
                                self.products.append(new_product)
                            elif sección == 3:
                                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                                # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                new_product= Producto(nombre, descripción, nuevo_precio, categoria, inventario)
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
                                break
                        else:
                            print("Seleccion invalida, introduzca un valor correspondiente al menu")
                elif sección == 4:
                    # En esta sección se podran eliminar información de cada producto
                    print("-----Bienvenido a la parte donde eliminas piezas-----")
                    while True:
                        sección = self.entrada_menu("""Indique un numero para eliminar un producto: 
                                                                1. Nombre
                                                                2. Descripción
                                                                3. Precio
                                                                4. Categoria
                                                                5. Inventario
                                                                6. Volver a inicio
                                                                Ingreselo aqui -> """,7)
                        if sección != None:
                            if sección == 1:
                                nombre = input("Ingrese el nombre del producto: ")                               
                                for i, product in enumerate(self.products):
                                    if product.nombre == nombre:
                                        self.products.pop(i)
                                        print("Se ha eliminado el producto de manera exitosa")
                            elif sección == 2:
                                descripción = input("Ingrese la descripción del producto: ")
                                for i, desc in enumerate(self.products):
                                    if desc.descripción == descripción:
                                        self.products.pop(i)
                                    print("Se ha eliminado la descripción del producto de manera exitosa")
                            elif sección == 3:
                                precio = input("Ingrese el precio del producto: ")
                                for i, price in enumerate(self.products):
                                    if price.precio == precio:
                                        self.precio.pop(i)
                                print("Se ha eliminado el usuario de manera exitosa")
                            elif sección == 4:
                                categoria = input("Ingrese la categoria del producto")
                                for i, cate in enumerate(self.products):
                                    if cate.categoria == categoria:
                                        self.categoria.pop(i)
                                print("Se ha eliminado el usuario de manera exitosa")
                            elif sección == 5:
                                inventario = int(input("Ingrese el numero de productos que hay en el inventario: "))
                                for i, invent in enumerate(self.products):
                                    if invent.inventario == inventario:
                                        self.inventario.pop(i)
                                print("Se ha eliminado el usuario de manera exitosa")
                            elif sección == 6:
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
                        
                    fecha_de_la_venta = input("Ingrese la fecha de la venta (2024-12-03): ")   
                    try: 
                        fecha_de_la_venta = datetime.date.fromisoformat(fecha_de_la_venta)
                    except ValueError:
                        fecha_de_la_venta = input("""Error!!!. Ingrese unos (-) para que sea una opcion valida (2024-12-03):  """)   
                        
                    id= int(input("Ingrese el ID del producto: "))
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
                                                                        Ingrese la opcion correspondiente -> """).lower()  
                    metodo_de_envio = (input("""  Introduzca el metodo de envio:
                                                                            1.Zoom
                                                                            2.Delivery
                                                                            Ingrese la opcion correspondiente -> """)).lower()
                    while metodo_de_envio not in ['zoom', 'delivery']: 
                         metodo_de_envio = (input(""" !!!ERROR !!! Ingrese el metodo de pago:
                                                                        - Bolivares
                                                                        - Divisas extranjeras
                                                                        Ingrese la opcion correspondiente -> """)).lower()
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
                    
                    if cliente == 'juridico':
                        print(f"Descuento juridico: {total * descuento_juridico}")
                        total -= total * descuento_juridico
                           
                    print(f"El iva es: {total* iva}")    
                    total += total * iva
                    
                    if metodo_de_pago == 'divisas':
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
                                                    Natural
                                                    Juridico
                                                    Ingrese su opcion aqui -> """)).lower()                               
                                for usuario in self.ventas:
                                    if usuario.cliente == cliente:
                                        print(f"El cliente {usuario.cliente} se ha encontrado")
                                        break
                                    else:
                                        print(f"No se ha encontrado el cliente: {cliente}")
                            elif selección == 2:
                                fecha_de_la_venta = input("Seleccione la fecha de venta del producto (aaaa-mm-dd): ")
                                for date in self.ventas:
                                    if date.fecha_de_la_venta == fecha_de_la_venta:
                                        print(f"La fecha de la venta fue el {date.fecha_de_la_venta}")   
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
                                                        Ingreselo aqui -> """,4) # Se le da la opción al cliente al registrar si es natural o juridico
                        if sección != None:   
                            if sección == 1:
                                nombre = input("Cual es tu nombre: ")
                                apellido = input("Cual es tu apellido: ")
                                try: 
                                    cedula = int(input("Ingrese la cedula (No use puntos ni letras): "))
                                except ValueError:
                                    cedula = int(input("Error!!, Introduzca un número entero (ejm: 30291432): "))
                                correo = input("Cual es tu correo?: ").lower()
                                while correo not in ["@correo.unimet.edu.ve", '@gmail.com']:
                                    correo = input("Error. Ingrese una opción de correo valida: ").lower()
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
                                while correo_juridico not in ['@correo.unimet.edu.ve', '@gmail.com']:
                                    correo_juridico = input("!!ERROR!!. Ingrese una opción de correo valida entre('@correo.unimet.edu.ve', '@gmail.com'): ")
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
                                try:
                                    buscar = int(input("Ingrese su cedula: ")) 
                                #Se le pide al usuario la cedula para que pueda modificar sus datos
                                except ValueError:
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
                                            print("La informarción se guardo de manera exitosa")
                                        elif sección == 2: 
                                            nuevo_apellido = input("Seleccione su nuevo apellido: ")
                                            # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                            new_client = Cliente(nombre, nuevo_apellido, cedula, correo, telefono)
                                            print("La informarción se guardo de manera exitosa")
                                        elif sección == 3:
                                            nueva_cedula = int(input("Introduzca su nuevo numero de cedula: "))
                                            # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                            new_client = Cliente(nombre, apellido, nueva_cedula, correo, telefono)
                                            print("La informarción se guardo de manera exitosa")
                                        elif sección == 4:
                                            nuevo_correo = input("Introduzca su nuevo correo electronico: ")
                                            # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                            new_client = Cliente(nombre, apellido, cedula, nuevo_correo, telefono)
                                            print("La informarción se guardo de manera exitosa")
                                        elif sección == 5:
                                            nuevo_telefono = int(input("Seleccione un nuevo numero de telefono: "))
                                            # Para modificar un producto, se crea una variable y esta se almacena en el objeto ya antes creado
                                            new_client = Cliente(nombre, apellido, cedula, correo, nuevo_telefono)
                                            print("La informarción se guardo de manera exitosa")
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
                            try:
                                eliminar = int(input("Escriba su cedula (No use puntos ni letras): "))
                            except ValueError:
                                eliminar = int(input("!ERROR! Escriba correctamente su cedula (No use puntos ni letras): "))
                            #Recorremos i y cliente en self.clients, para eliminar la variable ya antes asignadas
                            for i, cliente in enumerate(self.clients):
                                if cliente.cedula == eliminar:
                                    self.clients.pop(i)
                                    print("Se ha eliminado el usuario de manera exitosa")
                        
                        elif sección == 2:
                            try:
                                eliminar = int(input("Escriba el rif de la empresa: "))
                            except:
                                eliminar = int(input("!ERROR! Escriba correctamente el rif de la empresa: "))
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
                                try: 
                                    cedula = int(input("Indique su cedula (No use puntos ni letras): "))
                                except:
                                    cedula = int(input(" !ERROR! Indique correctamente su cedula (No use puntos ni letras): "))
                                for client in self.clients:
                                    if client.cedula == cedula:
                                        print(f"La cedula {cedula} pertenece a {client.nombre} {client.apellido}")
                                    else:
                                        print(f"No se ha encontrado la cedula: {cedula}")
                            elif sección == 2:
                                try:
                                    rif = int(input("Indique su rif: "))
                                except:
                                    rif = int(input(" !ERROR! Indique correctamente su rif: "))
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
                    tipo_de_pago = input("""Ingrese el tipo de pago: 
                                        -Punto de Venta 
                                        -Pago Movil
                                        -Transferencia
                                        -Zelle
                                        -Efectivo.
                                        Ingreselo aqui -> """).lower()
                    while tipo_de_pago not in ['punto de venta', 'pago movil', 'transferencia', 'zelle', 'efectivo']:
                        tipo_de_pago = input("""Error. Ingrese correctamente un tipo de pago entre:
                                             -Punto de venta
                                             -Pago movil,
                                             -Transferencia
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
                                tipo_de_pago = input("Ingrese el tipo de pago: ").lower()
                                for pago in self.payments:
                                    if pago.tipo_de_pago == tipo_de_pago:
                                        print(f"El pago fue por {pago.tipo_de_pago}")
                                        break
                                    else:
                                        print(f"No se ha encontrado ningun pago: {tipo_de_pago}")
                            elif sección == 4:
                                moneda = input("Ingrese la moneda de pago: ").lower()
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
                        cedula = int(input("Error!!, Introduzca un número entero (ejm: 30291): "))
                    fecha_de_entrega = input("Ingrese la fecha de entrega(2023-8-21): ")    
                    try: 
                        fecha_de_entrega = datetime.date.fromisoformat(fecha_de_entrega)
                    except ValueError:
                        fecha_de_entrega = input("""Error!!!. Ingrese unos (-) para que sea una opcion valida (2024-12-03):  """) 
                    try:
                        producto = input("Que producto desea comprar: ")
                    except ValueError:
                        producto = input("!!ERROR!! Ingrese el producto que desea comprar: ")
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
                    new_shipment = Envios(cliente, cedula, producto, fecha_de_entrega, orden_compra, servicio_envio, costo)
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
                            fecha_de_entrega = (input("Ingrese la fecha de entrega: "))
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
            sección = self.entrada_menu("""¿A que desea acceder?: 
                            1. Informes de Ventas
                            2. Informes de Pagos
                            3. Informes de envios
                            4. Volver a inicio
                            Ingreselo aqui -> """,5)
            if sección != None:
                if sección == 1:
                    print("----- Bienvenido a los informes de ventas -----")
                    sección = self.entrada_menu("""¿A que desea acceder?: 
                            1. Ventas totales por dia, semanas, mes y año
                            2. Productos mas vendidos
                            3. Clientes mas frecuentes
                            4. Volver a inicio
                            Ingreselo aqui -> """,5)
                    if sección != None:
                        if sección == 1:
                            #Lista para recorrer las ventas por los años, de los años pasas a meses y de ahi a semanas y dias.
                            pass
                        elif sección == 2:
                            productos_vendidos = {}

                            # ... (dentro del bucle donde registras una venta)
                            productos_vendidos[id] = productos_vendidos.get(id, 0) 

                            # Al final, encontrar el producto más vendido
                            producto_mas_vendido = max(productos_vendidos, key=productos_vendidos.get)
                            print(f"El producto más vendido es: {producto_mas_vendido}")
                            
                            #Creando el grafico de productos mas vendidos
                            plt.bar(productos_vendidos.keys(), productos_vendidos.values())
                            plt.xlabel('ID del producto')
                            plt.ylabel('Cantidad vendida')
                            plt.title('Productos más vendidos')
                            plt.show()
                        elif sección == 3:
                               # Lista para almacenar los IDs de los clientes
                                clientes_ventas = []

                                # Diccionario para contar la frecuencia de cada cliente
                                conteo_clientes = {}

                                # Contar la frecuencia de cada cliente
                                for cliente in clientes_ventas:
                                    if cliente in conteo_clientes:
                                        conteo_clientes[cliente] += 1
                                    else:
                                        conteo_clientes[cliente] = 1

                                # Ordenar el diccionario por valor (frecuencia)
                                clientes_mas_frecuentes = sorted(conteo_clientes.items(), key=lambda x: x[1], reverse=True)

                                # Crear el gráfico de barras
                                plt.bar(range(len(clientes_mas_frecuentes)), [x[1] for x in clientes_mas_frecuentes], tick_label=[x[0] for x in clientes_mas_frecuentes])
                                plt.xlabel('ID del Cliente')
                                plt.ylabel('Número de Ventas')
                                plt.title('Clientes Más Frecuentes')
                                plt.show()
                        elif sección == 4:
                            break
                    else:
                        print("Selección Invalida")
                elif sección == 2:
            #Lugar donde puedes consultar los registros de pago
                    print("----- Bienvenido a los Informes de pago -----")
                    sección = self.entrada_menu(""" ¿A que desea acceder?:
                            1. Pagos totales por dia, semana, mes y año
                            2. Clientes con pagos pendientes
                            3. Volver a inicio
                            Ingreselo aqui -> """,4)
                    if sección != None:
                        if sección == 1:
                            # Ejemplo: calcular totales por día y graficar
                            def pagos_por_periodo(pagos, periodo):
                                resultados = {}
                                for pago in pagos:
                                    if periodo == 'dia':
                                        fecha_clave = pago.fecha.strftime('%Y-%m-%d')
                                    elif periodo == 'semana':
                                        fecha_clave = pago.fecha.isocalendar()[1]  # Número de semana del año
                                    elif periodo == 'mes':
                                        fecha_clave = pago.fecha.strftime('%Y-%m')
                                    else:
                                        fecha_clave = pago.fecha.year

                                    if fecha_clave not in resultados:
                                        resultados[fecha_clave] = 0
                                    resultados[fecha_clave] += pago.monto_pago

                                return resultados
                    
                            pagos_por_dia = pagos_por_periodo(self.payments, 'dia')
                            pagos_por_semana = pagos_por_periodo(self.payments, 'semana')
                            pagos_por_mes = pagos_por_periodo(self.payments, 'mes')
                            pagos_por_año = pagos_por_periodo(self.payments, 'año')
                           # Visualización (ejemplo para pagos por día)
                            plt.plot(list(pagos_por_dia.keys()), list(pagos_por_dia.values()))
                            plt.xlabel('Fecha')
                            plt.ylabel('Monto Total')
                            plt.title('Pagos Totales por Día')
                            plt.show()
                            
                            plt.plot(list(pagos_por_semana.keys()), list(pagos_por_semana.values()))
                            plt.xlabel('Fecha')
                            plt.ylabel('Monto Total')
                            plt.title('Pagos Totales por Día')
                            plt.show()
                            
                            plt.plot(list(pagos_por_mes.keys()), list(pagos_por_mes.values()))
                            plt.xlabel('Fecha')
                            plt.ylabel('Monto Total')
                            plt.title('Pagos Totales por Día')
                            plt.show()
                            
                            plt.plot(list(pagos_por_año.keys()), list(pagos_por_año.values()))
                            plt.xlabel('Fecha')
                            plt.ylabel('Monto Total')
                            plt.title('Pagos Totales por Día')
                            plt.show()
                        elif sección == 2:
                            pagos_pendientes = []
                            print("""Estos son los clientes con pedidos pendientes: """)
                            for pago in pagos_pendientes:
                                print(pago)
                            plt.bar(pagos_pendientes, [1] * len(pagos_pendientes)) #Funcion donde crea el grafico de barras.
                            #El grafico
                            plt.xlabel('Clientes')
                            plt.ylabel('Pagos pendientes')
                            plt.title('Clientes con pagos pendientes')
                            #Muestra el grafico
                            plt.show()
                        elif sección == 3:
                            break
                    else:
                        print("Selección Invalida")
                elif sección == 3:
                    #Lugar donde revisaras los registros de envios
                    print("----- Bienvenido al registro de envios -----")
                    sección = self.entrada_menu(""" ¿A que desea acceder?
                            1. Envios totales por dia, semana, mes y año
                            2. Productos mas enviados
                            3. Clientes con envios pendientes
                            4. Volver a inicio
                            Ingreselo aqui -> """,5)
                    if sección != None:
                        if sección == 1:
                            # Crear un DataFrame para almacenar los envíos
                            data = []
                            # ... (agregar cada nuevo envío a la lista data)
                            df = pd.DataFrame(data)
                            df['fecha_de_entrega'] = pd.to_datetime(df['fecha_de_entrega'])

                            # Cálculo de indicadores y visualización
                            def graficar_envios(df, agrupacion='D'):
                                df_agrupado = df.groupby(pd.Grouper(key='fecha_de_entrega', freq=agrupacion)).size()
                                plt.figure(figsize=(10, 6))
                                plt.plot(df_agrupado.index, df_agrupado.values)
                                plt.xlabel('Fecha')
                                plt.ylabel('Número de Envíos')
                                plt.title(f'Envíos Totales por {agrupacion}')
                                plt.show()
                                #Ejemplo de uso:
                                graficar_envios(df, 'D')  # Envíos por día
                            graficar_envios(df, 'W')  # Envíos por semana
                            graficar_envios(df, 'M')  # Envíos por mes
                            graficar_envios(df, 'Y')  # Envíos por año
                        elif sección == 2:
                            productos_mas_enviados = {}
                            # Actualizar el conteo del producto
                            productos_mas_enviados[Producto] = productos_mas_enviados.get(Producto, 0) + 1
                            # Crea el gráfico de barras
                            plt.bar(productos_mas_enviados.keys(), productos_mas_enviados.values())
                            plt.xlabel('Producto')
                            plt.ylabel('Cantidad de Envíos')
                            plt.title('Productos Más Enviados')
                            plt.xticks(rotation=45)  # Rotar las etiquetas del eje x si son muy largas
                            plt.show()
                                                        
                        elif sección == 3:
                            # Archivo de datos (ajusta la ruta si es necesario)
                            envios = [] # Lista para almacenar los objetos Envios        
                            def calcular_envios_pendientes(envios):
                                hoy = datetime.date.today()
                                pendientes = 0
                                for envio in envios:
                                    if envio.fecha_de_entrega > hoy:
                                        pendientes += 1
                                return pendientes

                            # Crear un gráfico de línea simple
                            def graficar_envios_pendientes(envios_pendientes_por_dia):
                                plt.plot(envios_pendientes_por_dia.keys(), envios_pendientes_por_dia.values())
                                plt.xlabel('Fecha')
                                plt.ylabel('Envíos Pendientes')
                                plt.title('Evolución de Envíos Pendientes')
                                plt.show()
                            graficar_envios_pendientes(calcular_envios_pendientes)
                                                    
                        elif sección == 4:
                            break
                    else:
                        print("Selección Invalida")
                elif sección == 4:
                    break
            else:
                print("Selección Invalida")        
                
