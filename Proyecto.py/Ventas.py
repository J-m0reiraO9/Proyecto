#Constructor, metodos y atributo de la clase Ventas
from dataclasses import dataclass
@dataclass
class Venta:
    #Constructor de la clase Venta
    
    compra: str
    fecha: str
    productos: str
    cantidad: int
    pago: float
    envio: str
    
    def __init__(self, compra, fecha, productos, cantidad, pago, envio, ):
        self.compra = compra
        self.fecha = fecha
        self.productos = productos
        self.cantidad = cantidad
        self.pago = pago
        self.envio = envio
        
    def show(self):
        print(f"""
              Compra = {self.compra}
              Fecha = {self.fecha}
              Productos = {self.productos}
              Cantidad = {self.cantidad}
              Pago = {self.pago}
              Envio = {self.envio}
              """)

        
