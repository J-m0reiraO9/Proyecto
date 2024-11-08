#Se importan todos los datos usados
from Productos import Producto
from Ventas import Venta
from Clientes import Cliente
from Pagos import Pagos
from Envios import Envio
from Envios import Repartidor
from Indicadores_de_gestion import Indicadores_de_gestion
from Clientes import Juridico

import math
import dataclasses
import json

Url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json"

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
                self.juridicos.append(nombre_juridico)
                
            for pago in y["Pagos"]:
                pago_cliente = pago.get("pago_cliente")
                monto = pago.get("monto")
                moneda = pago.get("moneda")
                tipo_de_pago = pago.get("tipo_de_pago")
                fecha = pago.get("fecha")
                nuevo_pago = Pagos(pago_cliente, monto, moneda, tipo_de_pago, fecha)
                self.payments.append(nuevo_pago)

            for producto in y["Productos"]:
                nombre = producto.get("nombre")
                descripción = producto.get("descripción")
                precio = producto.get("precio")
                categoria = producto.get("categoria")
                inventario = producto.get("inventario")
                vehiculo_compatible = producto.get("vehiculo_compatible")
                nuevo_producto = Producto(nombre,descripción, precio, categoria, inventario, vehiculo_compatible)
                self.products.append(nuevo_producto)
            
            for envio in y["Envio"]:
                 cliente = envio.get("cliente")
                 fecha_de_entrega = envio.get("fecha_de_entrega")
                 orden_compra = envio.get("orden_compra")
                 servicio_envio = envio.get("servicio_envio")
                 costo = envio.get("costo")

                 nuevo_envio = Envio(cliente, fecha_de_entrega, orden_compra, servicio_envio, costo)
                 self.Envios.append(nuevo_envio)
                    
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
                                Ingrese aqui su numero: """,8)
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
                                5. Volver al inicio: """, 6)
            if sección != None:
                if sección == 1:
                    #Registro para almacenar los repuestos
                    print("-----Bienvenido a la parte de incorporación de piezas-----")
                    nuevo_productos = []
            
                    nombre = input("Introduzca el nombre del producto: ")
                    descripción = input("Introduzca la descripción del producto: ")
                    precio = float(input("Introduzca el precio del vehiculo: "))
                    categoria = input("Ingrese la categoria del vehiculo: ")
                    inventario = int(input("Ingrese la cantidad en el inventario: "))
                    vehiculo_compatible = input("Ingrese el vehiculo que es compatible con el vehiculo: ")
                    nuevo_productos = Producto(nombre, descripción, precio, categoria, inventario, vehiculo_compatible)
                    self.products.append(nuevo_productos)
                    
                    print(dataclasses.asdict(nuevo_productos))
                elif sección == 2:
                    #En esta parte se buscan las piezas
                    print("-----Bienvenido a busqueda de piezas-----")
                    while True:
                        sección = self.entrada_menu("""Indique un numero para buscar las piezas en el inventario: 
                                                                1. Categoría
                                                                2. Precio 
                                                                3. Nombre
                                                                4. Disponibilidad de inventario
                                                                5. Volver a inicio: """,6) #Busca el usuario catalogando segun la cedula, rif y correo electronico
                        
                        if sección != None: 
                            if sección == 1:
                                for category in self.products:
                                    if category.categoria == categoria:
                                        print(f"La categoria {categoria} pertenece a la lista")
                                    else:
                                        print(f"No se ha encontrado la categoria: {categoria}")
                            elif sección == 2:
                                for prize in self.products:
                                    if prize.precio == precio:
                                        print(f"El precio {precio} pertenece a la lista")
                                    else:
                                        print(f"No se ha encontrado la categoria: {categoria}")
                            elif sección == 3:
                                for name in self.products:
                                    if name.nombre == nombre:
                                        print(f"El nombre del {nombre} del producto pertenece a la lista")
                                    else:
                                        print(f"No se ha encontrado el nombre de: {nombre}")
                            elif sección == 4:
                                for disponibilidad in self.products:
                                    if disponibilidad.inventario == inventario:
                                        print(f"La disponibilidad del producto en el inventario es de: {inventario}")
                                    else: 
                                        print(f"No se ha encontrado disponiblidad del producto")
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
                                                                7. Volver a inicio: """,8)
                        if sección != None:
                            if sección == 1:
                                nuevo_nombre = input("Nuevo nombre de la pieza: ").capitalize()
                                new_product = Producto(nuevo_nombre,descripción, precio, categoria, inventario, vehiculo_compatible)
                                self.products.append(new_product)
                            elif sección == 2:
                                nueva_description = input("Nueva descripción de la pieza: ").capitalize()
                                new_product= Producto(nombre, nueva_description, precio, categoria, inventario, vehiculo_compatible)
                                self.products.append(new_product)
                            elif sección == 3:
                                while True:
                                    nuevo_precio = float(input("Ingrese el nuevo precio del producto"))
                                    if nuevo_precio != float:
                                        print("Selección invalida")
                                    else:
                                        new_product= Producto(nombre, descripción, nuevo_precio, categoria, inventario, vehiculo_compatible)
                                        self.products.append(new_product)
                                        break
                            elif sección == 4:
                                nueva_categoria = input("Introduzca la modificación de la categoria: ").capitalize()
                                new_product= Producto(nombre, descripción, precio, nueva_categoria, inventario, vehiculo_compatible)
                                self.products.append(new_product)
                            elif sección == 5:
                                while True:
                                    nuevo_inventario = int(input("Ingrese la nueva descripción de inventario: "))
                                    if nuevo_precio != int:
                                        print("Selección invalida")
                                    new_product= Producto(nombre, descripción, precio, categoria, nuevo_inventario, vehiculo_compatible)
                                    self.products.append(new_product)
                                    break
                            elif sección == 6:
                                nuevo_vehiculo = input("Ingrese un nuevo modelo de vehiculo: ")
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
                                                                7. Volver a inicio: """,8)
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
                    """,5)
            if sección != None:
                if sección == 1:
                # Sección donde podras y registrar ventas
                    print("----- Registro de Ventas -----")
                    nombre = input("Ingrese su nombre: ")
                    productos_comprados = []
                    cantidad_comprada= []
                    while True: 
                        producto_comprado= input("Ingrese el producto que quieres comprar: ")
                        cantidad = int(input("Ingrese la cantidad: "))
                        productos_comprados.append(producto_comprado)
                        cantidad_comprada.append(cantidad)
                        metodo_de_pago = self.entrada_menu("""Ingrese el metodo de pago: 
                                                           1. Efectivo
                                                           2. Transferencia
                                                           3. Zelle
                                                           4. Pago Movil
                                                           5. Salir""",6)
                        if metodo_de_pago != None:
                            if metodo_de_pago == 1:
                                pass
                            elif metodo_de_pago == 2:
                                pass
                            elif metodo_de_pago == 3:
                                pass
                            elif metodo_de_pago == 4:
                                pass
                            elif metodo_de_pago == 5:
                                break
                        else: 
                            print("Selección invalida")
                            
                        metodo_envio = self.entrada_menu(""" Ingrese el metdo de envio:
                                                         1. Zoom
                                                         2. Delivery
                                                         3. Salir
                                                         """, 4)
                        if metodo_envio != None:
                            if metodo_envio == 1:
                                pass
                            elif metodo_envio == 2:
                                pass
                            elif metodo_envio == 3:
                                break
                        else:
                            print("Selección invalida") 
                        nueva_venta = Venta(nombre, productos_comprados, cantidad_comprada, metodo_de_pago, metodo_envio)
                        self.ventas.append(nueva_venta)
                                
                elif sección == 2:
                # Sección donde se generan las facturas por cada compra
                    print("----- Factura -----")
                elif sección == 3:
                # Sección a la que podras buscar a los clientes
                    print("----- Bienvenido al registro de clientes ----- ")
                    while True:
                        selección = self.entrada_menu("""Indique un numero para buscar el cliente: 
                                                                1. Cliente 
                                                                2. Fecha de la venta
                                                                3. Volver a inicio """,4)
                        if sección != None:
                            if selección == 1: 
                                cliente = input("Indique el nombre del cliente: ")
                                for client in self.clients:
                                    if client.cliente == cliente:
                                        pass
                            elif selección == 2:
                                fecha = input("Seleccione la fecha de venta del producto: ")
                                for date in self.menu_ventas:
                                    pass      
                            elif selección == 3:
                                break
                elif sección == 4:
                    break
            else:
                print("Selección Invalida")
                
    def menu_clientes(self):
         #Constructor de la función menu de clientes
        while True:
            print("Bienvenido a la función Clientes!!")
            sección = self.entrada_menu("""¿Que desea realizar?: 
                                1. Registro de cliente
                                2. Modificar información del cliente 
                                3. Eliminar cliente
                                4. Busqueda de cliente
                                5. Volver al inicio
                                """, 6)
            if sección != None:
                if sección == 1:
            # Sección donde podras registrar a los clientes
                    print("----- Bienvenido al registro de clientes -----")
                    while True:
                        sección= self.entrada_menu("""Indique un numero: 
                                                        1. Cliente Natural
                                                        2. Cliente Juridico
                                                        3. Salir: """,4)
                        if sección != None:   
                            if sección == 1:
                                nombre = input("Cual es tu nombre: ")
                                apellido = input("Cual es tu apellido: ")
                                cedula = int(input("Indique su cedula: "))
                                correo = input("Cual es tu correo?: ")
                                telefono = input("Indique su numero telefonico: ")
                                new_client = Cliente(nombre, apellido, cedula, correo, telefono)
                                
                                encontrado = False
                                for client in self.clients:
                                    if client.cedula == cedula:
                                        encontrado = True
                                if encontrado:
                                    print("Esa cedula ya existe")
                                else:
                                    self.clients.append(new_client)
                                                                      
                            elif sección == 2:
                                nombre_juridico = input("Ingrese el nombre juridico: ")
                                rif = int(input("Ingrese el Rif de la empresa: "))
                                telefono = (input("Ingrese el numero de Telefono de la empresa: "))
                                correo_juridico = input("Ingrese el Correo de la empresa: ")
                                
                          
                                new_company = Juridico(nombre_juridico, rif, telefono, correo_juridico)
                                self.juridicos.append(new_company)
                                      
                            elif sección == 3:
                                break
                        else:
                            print("Seleccion invalida")
                elif sección == 2:
                # Sección donde podras registar la información del cliente
                    print("----- Bienvenido a la Modificación de Información del cliente -----")
                    while True: 
                        sección = self.entrada_menu("""Quisiera modificar un aspecto de: 
                                                        1. Cliente Natural
                                                        2. Cliente Juridico
                                                        3. Volver al inicio
                                                        Seleccione: """,4)
                        if sección != None:
                            if sección == 1: 
                                buscar = int(input("Ingrese su cedula: "))
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
                                                            Seleccione: """,7)
                                    if sección != None:         
                                        if sección == 1:
                                            nuevo_nombre = input("Selecciona su nuevo nombre: ")
                                            new_client = Cliente(nuevo_nombre, apellido, cedula, correo, telefono)
                                        elif sección == 2: 
                                            nuevo_apellido = input("Seleccione su nuevo apellido: ")
                                            new_client = Cliente(nombre, nuevo_apellido, cedula, correo, telefono)
                                        elif sección == 3:
                                            nueva_cedula = int(input("Introduzca su nuevo numero de cedula: "))
                                            if nueva_cedula != int:
                                                print("Selección invalida")
                                            new_client = Cliente(nombre, apellido, cedula, correo, telefono)
                                        elif sección == 4:
                                            nuevo_correo = input("Introduzca su nuevo correo electronico: ")
                                            new_client = Cliente(nombre, apellido, cedula, nuevo_correo, telefono)
                                        elif sección == 5:
                                            nuevo_telefono = int(input("Seleccione un nuevo numero de telefono: "))
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
                                                                Seleccione: """,6)
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
                                                        Seleccione: """,4)
                    if sección != None:
                        if sección == 1:
                            eliminar = int(input("Escriba su cedula: "))
                            for i, cliente in enumerate(self.clients):
                                if cliente.cedula == eliminar:
                                    self.clients.pop(i)
                                    print("Se ha eliminado el usuario de manera exitosa")
                        
                        elif sección == 2:
                            eliminar = int(input("Escriba el rif de la empresa"))
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
                                                                5. Volver a inicio: """,6) #Busca el usuario catalogando segun la cedula, rif y correo electronico
                        if sección != None:
                            if sección == 1: 
                                cedula = int(input("Indique su cedula: "))
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
                            """, 4)
            if sección != None:
                if sección == 1:
            #Sección en donde registras los pagos hechos.
                    print("----- Bienvenido al lugar donde puedes registrar los pagos -----")
                    
                    cliente = input("Ingrese su nombre: ")
                    monto_pago = float(input("Ingrese el monto del pago: "))
                    moneda_pago = input("Ingrese la moneda de pago (Bolivares, Euros o dolares): ").lower()
                    tipo_de_pago = input("""Ingrese el medio de pago: 
                                        -Punto de Venta 
                                        -Pago Movil
                                        -Transferencia
                                        -Zelle
                                        -Efectivo.
                                        Ingresa aqui -> """)
                    fecha = input("Ingrese la fecha de pago (aaaa-mm-dd): ") #En lo que en parentesis significa: 
                                                                                     # a = Años
                                                                                     # m = meses
                                                                                     # d = dias
                    new_payment = Pagos(cliente, monto_pago, moneda_pago, tipo_de_pago, fecha)
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
                                                                5. Volver a inicio: """,6)
                        if sección != None:
                            if sección == 1: 
                                cliente = input("Ingrese su nombre: ")
                                for client in self.payments:
                                    if client.cliente == cliente:
                                        print(f"Se ha encontrado el cliente de nombre {self.cliente}")
                                        break
                                    else:
                                        print(f"No se ha encontrado el cliente de nombre {self.cliente} ")
                            elif sección == 2:
                                fecha = input("Ingrese la fecha de la compra(aaaa-mm-dd): ")
                                for date in self.payments:
                                    if date.fecha == fecha:
                                        print(f"El producto se compro el {self.fecha}")
                                        break
                                    else:
                                        print(f"El producto no se compro el {self.fecha}")   
                            elif sección == 3:
                                tipo_de_pago = input("Ingrese el tipo de pago: ")
                                for pago in self.payments:
                                    if pago.tipo_de_pago == tipo_de_pago:
                                        print(f"El pago fue por {self.tipo_de_pago}")
                                        break
                                    else:
                                        print(f"No se ha encontrado ningun pago: {self.tipo_de_pago}")
                            elif sección == 4:
                                moneda_pago = input("Ingrese la moneda de pago: ")
                                for moneda in self.payments:
                                    if moneda.moneda_pago == moneda_pago:
                                        print(f"El pago se hizo con {self.moneda_pago}")
                                        break
                                    else:
                                        print(f"No se encontro ningun pago en {self.moneda_pago}")
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
                            3. Volver a inicio""",4)
            if sección != None:
                if sección == 1:
                     # Lugar donde podras consultar los registros de envios
                    print("----- Bienvenido al registro de envios -----")
                    cliente = input("Ingrese su nombre: ")
                    fecha_de_entrega = input("Ingrese la fecha de entrega(aaaa/mm/dd): ")
                    orden_compra = int(input("Cual es el ID orden de compra: "))
                    servicio_envio = input("Cual es el servicio de envio (Delivery o Zoom): ").lower()
                    costo = float(input("Introduzca el costo del envio: "))
                    new_shipment = Envio(orden_compra, servicio_envio, costo)
                    self.Envios.append(new_shipment)                
                    
                    if servicio_envio == "delivery" or "entrega": #Si el usuario indica que el servicio de envio es en delivery, al usuario se le otorgan los datos para registrar al delivery 
                        nombre = input("Diga el nombre del repartidor: ")
                        apellido = input("Diga el apellido: ")
                        cedula = input("Diga su cedula: ")
                        edad = int(input("Ingrese su apellido: "))
                        new_repartidor = Repartidor(nombre, apellido, cedula, edad)
                        self.repartidor.append(new_repartidor)
                    else: 
                        print("Selección invalida")
                                        
                elif sección == 2:
                     # Sitio donde podras buscar los envios
                    print("----- Bienvenido a la busqueda de envios -----")
                    sección = self.entrada_menu("""Ingrese un numero para buscar el envio: 
                                                  1. Cliente
                                                  2. Fecha
                                                  3. Salir""",4)
                    if sección == None:
                        if sección == 1:
                            cliente = input("Ingrese su nombre: ")
                            for client in self.Envios:
                                    if client.cliente == cliente:
                                        print(f"Se ha encontrado el cliente de nombre {self.cliente}")
                                        break
                                    else:
                                        print(f"No se ha encontrado el cliente de nombre {self.cliente} ")
                        elif sección == 2: 
                            fecha_de_entrega = input("Ingrese la fecha de entrega: ")
                            for fecha in self.Envios:
                                if fecha.fecha_entrega == fecha_de_entrega:
                                    print(f"La fecha del envio: {self.fecha_entrega}")
                                    break
                                else:
                                    print(f"No se ha encontrado el cliente de nombre {self.fecha_entrega}")  
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
                            """,6)
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
