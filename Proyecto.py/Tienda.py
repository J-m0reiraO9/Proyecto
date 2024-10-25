#Se importan todos los datos usados

from Productos import Producto
from Ventas import Venta
from Clientes import Cliente
from Pagos import Pagos
from Envios import Envio
from Indicadores_de_gestion import Indicadores_de_gestion


class Tienda:
    #Lista para almacenar las Apis
    def __init__(self):
        self.Producto = []
        self.Venta = []
        self.Cliente = []
        self.Pagos = []
        self.Envios = []
        self.Indicadores_de_Gestion = []
        
    def app(self):
    #Constructor de la clase Tienda:
        while True: #Bucle del menu hasta que se rompa con un break
            try:
                sección = int(input(f"""Bienvenido a nuestra tienda en linea!!! seleccione un numero:
                                1. Productos
                                2. Venta
                                3. Cliente
                                4. Pagos
                                5. Envios
                                6. Indicadores de Gestión
                                7. Salir de la tienda
                                Ingrese aqui su numero: """))
                #Verfico que la selección no se salga del rango
                if sección not in range(1,8):
                    print("Selección Invalida")
                else:
                    break
            except:
                print("Selección invalida")
            if sección == 1:
                self.Producto()
            elif sección == 2:
                self.Venta()
            elif sección == 3:
                self.Cliente()
            elif sección == 4:
                self.Pagos()
            elif sección == 5:
                self.Envios()
            elif sección == 6:
                self.Indicadores_de_Gestion()
            elif sección == 7:
                print("Vuelva Pronto")
                break
        
    def Producto(self):
        #Constructor de la clase producto
        while True:
            print("Bienvenidos al area de productos:")
            try:
                producto = input("""¿Que desea Realizar?: 
                                1. Agregar nuevo productos
                                2. Busqueda de productos
                                3. Modificar información
                                4. Eliminar productos
                                5. Volver al inicio""")
                if producto not in range(1,6):
                    print("Selección Invalida") 
            except:
                print("Selección invalida")
            
            if producto == 1:
                #Registro para almacenar los repuestos
                print("-----Bienvenido a la parte de incorporación de piezas-----")
                pass
                
            elif producto == 2:
                #En esta parte se buscan las piezas
                print("-----Bienvenido a busqueda de piezas-----")
                pass
            elif producto == 3:
                # En esta sección se podra modificar información de cada producto
                print("-----Bienvenido a la modificación de productos existentes")
                pass
            elif producto == 4:
                # En esta sección se podran eliminar información de cada producto
                print("-----Bienvenido a la parte donde eliminas piezas")
            
    def Venta(self):
        while True:
            print("Bienvenido al area de Ventas:")
            try:
                Opcion = input("""¿Que desea realizar?:
                    1. Registro de Venta
                    2. Generación de facturas por cada compra
                    3. Buscador de Ventas
                    4. Volver al Inicio
                    """)
                if Opcion not in range(1,5):
                    print("Selección invalida, vuelva a intentarlo")
            except:
                break
        if Opcion == 1:
            # Sección donde podras y registrar ventas
            print("----- Registro de Ventas -----")
        elif Opcion == 2:
            # Sección donde se generan las facturas por cada compra
            print("----- Bienvenido a la generación de su factura")
        elif Opcion == 3:
            # Sección a la que podras buscar a los clientes
            print("----- Bienvenido al registro de clientes")
        
    def Cliente(self):
        while True:
            print("Bienvenido a la función Clientes!!")
            try:
                cliente = input("""¿Que desea realizar?: 
                                1. Registro de cliente
                                2. Modificar información del cliente 
                                3. Eliminar cliente
                                4. Busqueda de cliente
                                5. Volver al inicio
                                """)
                if cliente not in range(1,6):
                    print("Selección invalida, intente de nuevo")
            except:
                break
        if cliente == 1:
            # Sección donde podras registrar a los clientes
            print("----- Bienvenido al registro de clientes -----")
        elif cliente == 2:
            # Sección donde podras registar la información del cliente
            print("----- Bienvenido a la Modificación Información del cliente -----")
        elif cliente == 3:
            # Sección donde puedes eliminar clientes
            print("----- Bienvenido a la eliminación del registro de cliente -----")
        elif cliente == 4:
            # Sección donde podras buscar a los clientes
            print("----- Bienvenido a la busqueda de cliente -----")
       
    def Pagos(self):
        while True:
            print("Bienvenido a la función de pago de la Tienda!!!")
            try:
                pago = input("""¿Que desea realizar?:
                            1. Registro de pagos
                            2. Busqueda de pagos
                            3. Volver al inicio
                            """)
                if pago not in range(1,4):
                    print("Selección invalida")
            except:
                 break
        if pago == 1:
            #Sección donde podras registrar los pagos hechos.
            print("----- Bienvenido al lugar donde puedes registrar los pagos -----")
        elif pago == 2:
            #En esta sección se podran Buscar los pagos anteriormente hechos
            print("----- Bienvenido al lugar donde puedes buscar los pagos -----") 
            
    def Envios(self):
        while True:
            print("Bienvenido a la zona de envios!!")
            try:
                envios = input("""¿A que desea acceder?: 
                            1. Registro de envios
                            2. Busqueda de envio
                            3. Volver a inicio""")
                if envios not in range(1,4):
                    print("Selección invalida")
            except:
                break
        if envios == 1:
            # Lugar donde podras consultar los registros de envios
            print("----- Bienvenido al registro de envios -----")
        elif envios == 2:
            # Sitio donde podras buscar los envios
            print("----- Bienvenido a la busqueda de envios -----")
        
    def Indicadores_de_Gestion(self):
        while True:
            print("Bienvenido a la sección de Indicadores de gestion!!")
            try:
                gestion = input("""¿A que deseas acceder?: 
                            1. Informes de Ventas
                            2. Informes de Pago
                            3. Informes de envios
                            4. Graficas con las respectivas estadisticas
                            5. Volver a inicio
                            """)
                if gestion not in range(1,6):
                    print("Selección invalida")
            except:
                break
        if gestion == 1:
            #Lugar donde podras consultar los registros de ventas pasados
            print("-----Bienvenido a los informes de ventas -----")
        elif gestion == 2:
            #Lugar donde puedes consultar los registros de pago
            print("----- Bienvenido a los Informes de pago -----")
        elif gestion == 3:
            #Lugar donde revisaras los registros de envios
            print("----- Bienvenido al registro de envios -----")
        elif gestion == 4:
            #Lugar donde veras graficas con las respectivos datos
            print("-----")
            
