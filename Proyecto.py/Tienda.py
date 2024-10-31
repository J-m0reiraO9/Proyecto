#Se importan todos los datos usados
import json
import requests
from Productos import Producto
from Ventas import Venta
from Clientes import Cliente
from Pagos import Pagos
from Envios import Envio
from Indicadores_de_gestion import Indicadores_de_gestion

class Tienda:
    #Lista para almacenar las Apis
    def __init__(self):
        self.productos = []
        self.ventas = []
        self.clientes = []
        self.pagos = []
        self.envios = []
        self.indicadores_de_gestion = []
        
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
            sección = self.entrada_menu("""Bienvenido a nuestra tienda en linea!!! Seleccione un numero:
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
                    pass
                elif sección == 3:
                    # En esta sección se podra modificar información de cada producto
                    print("-----Bienvenido a la modificación de productos existentes")
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
                elif sección == 2:
                # Sección donde se generan las facturas por cada compra
                    print("----- Bienvenido a la generación de su factura")
                elif sección == 3:
                # Sección a la que podras buscar a los clientes
                    print("----- Bienvenido al registro de clientes")
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
                       print("----- Bienvenido al registro de clientes -----")
                    while True:
                        selección= int(input(f"""Indique un numero: 
                                        1. Cliente Natural
                                        2. Cliente Juridico"""))
                        if selección != int or selección not in range(1,3):
                            print("Seleccion invalida")
                        if selección == 1:
                            self.nombreombre = input("Cual es tu nombre: ")
                            self.apellido = input("Cual es tu apellido: ")
                            self.cedula = int(input("Indique su cedula: "))
                            self.correo = input("Cual es tu correo?: ")
                            self.telefono = int(input("Indique su numero telefonico"))
                            
                            if self.cedula and self.telefono != int or self.telefono and self.cedula != 8:
                                print("Seleccion invalida")
                        
                        if selección ==2:
                            self.nombre_juridico = input("Nombre: ")
                            self.rif = int(input("Rif: "))
                            self.telefono = int(input("Telefono: "))
                            self.correo = input("Correo: ")
                            
                            if self.rif and self.telefono != int or self.telefono and self.rif != 8:
                                print("Selección invalida")
                elif sección == 2:
            # Sección donde podras registar la información del cliente
                    print("----- Bienvenido a la Modificación Información del cliente -----")
                elif sección == 3:
            # Sección donde puedes eliminar clientes
                    print("----- Bienvenido a la eliminación del registro de cliente -----")
                elif sección == 4:
            # Sección donde podras buscar a los clientes
                    print("----- Bienvenido a la busqueda de cliente -----")
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
            #Sección donde podras registrar los pagos hechos.
                    print("----- Bienvenido al lugar donde puedes registrar los pagos -----")
                elif sección == 2:
            #En esta sección se podran Buscar los pagos anteriormente hechos
                    print("----- Bienvenido al lugar donde puedes buscar los pagos -----") 
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
                elif sección == 2:
                     # Sitio donde podras buscar los envios
                    print("----- Bienvenido a la busqueda de envios -----")
                elif sección == 3:
                    break
            
            else:
                print("Selección Invalida")
            
    def menu_indicadores_de_gestion(self):
         #Constructor de la función menu de indicadores de gestión
        while True:
            print("Bienvenido a la sección de Indicadores de gestion!!")
            sección = self.entrada_menu(""" 1. Informes de Ventas
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
