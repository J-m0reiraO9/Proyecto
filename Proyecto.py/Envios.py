#Constructor, metodos y atributos de la clase Envio
from dataclasses import dataclass
@dataclass
class Envios:
    #Constructor de la clase Envio
    
    cliente: str
    cedula: int
    orden: str
    envio: str
    datos: str
    costo: float
    
    def __init__(self, cliente, cedula, orden_compra, servicio_envio, datos_repartidor, costo):
        self.cliente = cliente
        self.cedula = cedula
        self.orden = orden_compra
        self.envio = servicio_envio
        self.datos = datos_repartidor
        self.costo = costo
        
    def show(self):
        print(f"""
              Cliente = {self.cliente}
              Cedula = {self.cedula}
              Orden de Compra = {self.orden}
              Servicio de envio = {self.envio}
              Datos del repartidor = {self.datos}
              Costo del Servicio = {self.costo}
              """)
        
@dataclass
class Repartidor:
    nombre: str
    apellido: str
    cedula: int
    edad: int
    
    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad
    
    def show(self):
        print(f"""
              Nombre = {self.nombre}
              Apellido = {self.apellido}
              Cedula = {self.apellido}
              Edad = {self.edad}""")
    
    

