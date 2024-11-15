#Constructor, metodos y atributos de la clase Envio
from dataclasses import dataclass
@dataclass
class Envios:
    #Constructor de la clase Envio
    
    cliente: str
    cedula: int
    producto: str
    fecha_de_entrega: str
    orden: int
    envio: str
    costo: float
    
    def __init__(self, cliente, producto, cedula, fecha_de_entrega, orden_compra, servicio_envio, costo):
        self.cliente = cliente
        self.cedula = cedula
        self.producto = producto
        self.fecha_de_entrega = fecha_de_entrega
        self.orden = orden_compra
        self.envio = servicio_envio
        self.costo = costo
        self.entregado = False
        
    def show(self):
        print(f"""
              Cliente = {self.cliente}
              Cedula = {self.cedula}
              Producto = {self.producto}
              Fecha de Entrega = {self.fecha_de_entrega}
              Orden de Compra = {self.orden}
              Servicio de envio = {self.envio}
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
    
    
        
    
    

