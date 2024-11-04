#Se importan todos los datos usados
from Productos import Producto
from Ventas import Venta
from Clientes import Cliente
from Pagos import Pagos
from Envios import Envio
from Indicadores_de_gestion import Indicadores_de_gestion
from Clientes import Juridico

import json
Url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json"

class Tienda:
    #Lista para almacenar las Apis
    def __init__(self):
        self.ids = []
        self.names = []
        self.descriptions = []
        self.prices = []
        self.categories = []
        self.inventories = []
        self.ventas = []
        self.clients = []
        self.juridicos = []
                
    def load_data(self):
        for id in self.ids: Url
        pass
        
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
                    pass  
                elif sección == 2:
                    #En esta parte se buscan las piezas
                    print("-----Bienvenido a busqueda de piezas-----")
                    while True:
                        pieza = input("""Que pieza deseas buscar: """)  
                        if pieza == busqueda:                        
                            pass
                        else:
                            print("Error, La pieza no esta en el inventario")
                elif sección == 3:
                    # En esta sección se podra modificar información de cada producto
                    print("-----Bienvenido a la modificación de productos existentes-----")
                    pass
                elif sección == 4:
                    # En esta sección se podran eliminar información de cada producto
                    print("-----Bienvenido a la parte donde eliminas piezas")
                elif sección == 5:
                    break
            else:
                print("Selección Invalida")    
            
            
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
                        producto_comprado= input("Ingrese el productos que quiere comprar: ")
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
                    print("----- Bienvenido a la generación de su factura")
                elif sección == 3:
                # Sección a la que podras buscar a los clientes
                    print("----- Bienvenido al registro de clientes")
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
                        selección= self.entrada_menu("""Indique un numero: 
                                                        1. Cliente Natural
                                                        2. Cliente Juridico
                                                        3. Salir: """,4)
                        if selección != None:
                                            
                            if selección == 1:
                                nombre = input("Cual es tu nombre: ")
                                apellido = input("Cual es tu apellido: ")
                                cedula = int(input("Indique su cedula: "))
                                correo = input("Cual es tu correo?: ")
                                telefono = input("Indique su numero telefonico: ")
                                   
                                new_client = Cliente(nombre, apellido, cedula, correo, telefono)
                                self.clients.append(new_client)
                                    
                            elif selección == 2:
                                nombre_juridico = input("Ingrese el nombre juridico: ")
                                rif = int(input("Ingrese el Rif de la empresa: "))
                                telefono = (input("Ingrese el numero de Telefono de la empresa: "))
                                correo = input("Ingrese el Correo de la empresa: ")
                                
                                                               
                                new_company = Juridico(nombre_juridico, rif, telefono, correo)
                                self.juridicos.append(new_company)
                                        
                            elif selección == 3:
                                break
                        else:
                            print("Seleccion invalida")
                elif sección == 2:
                # Sección donde podras registar la información del cliente
                    print("----- Bienvenido a la Modificación de Información del cliente -----")
                    while True: 
                        
                        buscar = int(input("Ingrese su cedula: "))
                        while not buscar != int:
                            print("Selección invalida, vuelva a intentarlo")
                        if buscar == cedula:
                            print(f"Los datos actuales del cliente: {self.clients}")
                            selección = self.entrada_menu("""Seleccione un numero para modificar los datos: 
                                                        1. Nombre
                                                        2. Apellido
                                                        3. Cedula
                                                        4. Correo
                                                        5. Telefono
                                                        6. Volver a inicio
                                                        Seleccione: """,7)
                            if selección != None:
                                                
                                if selección == 1:
                                    nuevo_nombre = input("Selecciona su nuevo nombre: ")
                                    new_client = Cliente(nuevo_nombre, apellido, cedula, correo, telefono)
                                    print(new_client)
                                    
                                elif selección == 2: 
                                    nuevo_apellido = input("Seleccione su nuevo apellido: ")
                                    new_client = Cliente(nombre, nuevo_apellido, cedula, correo, telefono)
                                elif selección == 3:
                                    nueva_cedula = int(input("Introduzca su nuevo numero de cedula: "))
                                    if nueva_cedula != int:
                                        print("Selección invalida")
                                    new_client = Cliente(nombre, apellido, cedula, correo, telefono)
                                elif selección == 4:
                                    nuevo_correo = input("Introduzca su nuevo correo electronico: ")
                                    new_client = Cliente(nombre, apellido, cedula, nuevo_correo, telefono)
                                elif selección == 5:
                                    nuevo_telefono = int(input("Seleccione un nuevo numero de telefono: "))
                                    new_client = Cliente(nombre, apellido, cedula, correo, nuevo_telefono)
                                elif selección == 6:
                                    break  
                        else:
                            print("La cedula del cliente no concuerda")
                elif sección == 3:
                # Sección donde puedes eliminar clientes, eliminando a partir de su cedula
                    print("----- Bienvenido a la eliminación del registro de cliente -----")
                    eliminar = int(input("Ingrese la cedula: "))
                    while not eliminar != int:
                        print("Selección invalida, vuelva a intentarlo")
                                
                elif sección == 4:
                # Sección donde podras buscar a los clientes
                    print("----- Bienvenido a la busqueda de cliente -----")
                    while True:
                        selección = self.entrada_menu("""Indique un numero para buscar el cliente: 
                                                                1. Cedula 
                                                                2. Rif
                                                                3. Correo Electronico (Persona Natural)
                                                                4. Correo Electronico (Persona Juridica)
                                                                5. Volver a inicio: """,6) #Busca el usuario catalogando segun la cedula, rif y correo electronico
                        if sección != None:
                            if selección == 1: 
                                cedula = int(input("Indique su cedula: "))
                                for client in self.clients:
                                    if client.cedula == cedula:
                                        print(f"La cedula {cedula} pertenece a {nombre}")
                                    elif client.cedula != cedula:
                                        print(f"No se ha encontrado la cedula: {cedula}")
                            elif selección == 2:
                                rif = int(input("Indique su rif: "))
                                for company in self.juridicos:
                                    if company.rif == rif:
                                        print(f"El rif {rif} pertenece a {correo}")
                                    elif company.rif != rif:
                                        print(f"No se ha encotrado el rif: {rif}")      
                            elif selección == 3:
                                correo = input("Indique su correo electronico: ")
                                for mail in self.clients:
                                    if mail.correo == correo:
                                        print(f"El correo {correo} pertenece a {nombre}")
                                    elif mail.correo != correo:
                                        print(f"No encontramos el correo: {correo}")
                            elif sección == 4:
                                correo = input("Indique su correo electronico: ")
                                for mail_juridico in self.juridicos:
                                    if mail_juridico.correo == correo:
                                        print(f"El correo juridico {correo} pertenece a {nombre}")
                                    elif mail_juridico != correo:
                                        print(f"No encontramos el correo juridico: {correo}") 
                            elif sección == 5:
                                break
                        else:
                            print("Selección Invalida")
               
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
            #Sección donde podras registrar los pagos hechos.
                    print("----- Bienvenido al lugar donde puedes registrar los pagos -----")
                    
                    moneda_pago = self.entrada_menu("""Cual es la Moneda de pago: 
                                                    1. Bolivares
                                                    2. Dolares
                                                    3. Euros
                                                    4. Pesos Colombianos""", 5)
                    tipo_de_pago = self.entrada_menu("""Cual es el tipo de pago:
                                         1. Punto de Venta
                                         2. Pago Movil
                                         3. Transferencia
                                         4. Zelle
                                         5. Efectivo""", 6)
                elif sección == 2:
            #En esta sección se podran Buscar los pagos anteriormente hechos
                    print("----- Bienvenido a la busqueda de pagos -----") 
                    while True:
                        selección = self.entrada_menu("""Indique un numero para buscar el cliente: 
                                                                1. Cliente
                                                                2. Fecha
                                                                3. Tipo de Pago
                                                                4. Moneda de Pago
                                                                5. Volver a inicio: """,6)
                        if sección != None:
                            if selección == 1: 
                                cliente = input("Ingrese su nombre: ")
                            elif selección == 2:
                                fecha = input("Ingrese la fecha de la compra: ")
                            elif selección == 3:
                                tipo_de_pago = input("Ingrese el tipo de pago: ")
                            elif selección == 4:
                                moneda_pago = input("Ingrese la moneda de pago: ")
                            elif selección == 5:
                                break
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
                    servicio_de_envio = self.entrada_menu("""Por cual medio se entrega el envio:
                                              1. Zoom
                                              2. Delivery por Moto""")
                    
                elif sección == 2:
                     # Sitio donde podras buscar los envios
                    print("----- Bienvenido a la busqueda de envios -----")
                    selección = self.entrada_menu("""Ingrese un numero para buscar el envio: 
                                                  1. Cliente
                                                  2. Fecha""")
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
                
