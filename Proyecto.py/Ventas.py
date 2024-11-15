#Constructor, metodos y atributo de la clase Ventas
from dataclasses import dataclass
from datetime import date
@dataclass
class Venta:
    #Constructor de la clase Venta
    
    cliente: str
    fecha_de_la_venta: date
    id = int
    cantidad: int
    metodo_de_pago: float
    envio: str
    
    def __init__(self, cliente, fecha_de_la_venta, id, cantidad, metodo_de_pago, metodo_de_envio ):
        self.cliente = cliente
        self.fecha_de_la_venta = fecha_de_la_venta
        self.id = id
        self.cantidad = cantidad
        self.metodo_de_pago = metodo_de_pago
        self.metodo_de_envio = metodo_de_envio
        
    def show(self):
        print(f"""
              Cliente = {self.cliente}
              Fecha de la venta= {self.fecha_de_la_venta}
              ID = {self.id}
              Cantidad = {self.cantidad}
              Metodo de Pago = {self.metodo_de_pago}
              Metodo de Envio = {self.metodo_de_envio}
              """)

        
        
