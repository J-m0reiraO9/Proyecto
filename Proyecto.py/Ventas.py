#Constructor, metodos y atributo de la clase Ventas

from dataclasses import dataclass
@dataclass
class Venta:
    #Constructor de la clase Venta
    
    compra: str
    productos: str
    cantidad: int
    pago: float
    envio: str
    
    def __init__(self, compra, productos, cantidad, pago, envio, ):
        self.compra = compra
        self.productos = productos
        self.cantidad = cantidad
        self.pago = pago
        self.envio = envio
        
    def show(self):
        print(f"""
              Compra = {self.compra}
              Productos = {self.productos}
              Cantidad = {self.cantidad}
              Pago = {self.pago}
              Envio = {self.envio}
              """)
@dataclass
class Total(Venta):
    #Constructor de la clase Total, clase hija de venta
    iva: float
    subtotal: float
    IGTF: float

    def __init__(self, compra, productos, cantidad, pago, envio, iva, subtotal, IGTF):
        super().__init__(compra, productos, cantidad, pago, envio)
        self.iva = 0.16
        self.subtotal = subtotal
        self.IGTF = 0.03
        
