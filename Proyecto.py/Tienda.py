#Se importan todos los datos usados

from Clientes import Cliente
from Envios import Envio
from Estadistica import Estadistica
from Pagos import Pagos
from Productos import Producto
from Ventas import Venta

class Tienda:
    #Constructor de la clase Tienda
    def __init__(self):
        pass

    while True: #Bucle del menu hasta que se rompa con un break
        try:
            sección = int(input(f"""Bienvenido a nuestra tienda en linea!!! seleccione un numero:
                            1. Productos
                            2. Venta
                            3. Clientes
                            4. Pagos
                            5. Envios
                            6. Indicadores de gestión
                            Ingrese aqui su numero: """))
            #Verfico que la selección no se salga del rango
            if sección not in range(1,7):
                print("Selección Invalida")
            else:
                break
        except:
            print("Selección invalida")
