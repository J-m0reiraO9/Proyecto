#Constructor, metodos y atributo de la clase Pagos
from dataclasses import dataclass
@dataclass
class Pagos:
    #Constructor de la clase Pagos
    
    
    cliente: str
    cedula: int
    monto_pago: float 
    moneda: str
    tipo_de_pago: str
    fecha: str

    def __init__(self, cliente, cedula, monto_pago, moneda, Tipo_de_pago, fecha):
        self.cliente = cliente
        self.cedula = cedula
        self.monto_pago = monto_pago
        self.moneda = moneda
        self.tipo_de_pago = Tipo_de_pago
        self.fecha = fecha
    
    def show_attr(self):
        print(f"""
              Cliente que realizo el pago = {self.pago_cliente}
              Cedula = {self.cedula}
              Monto = {self.monto_pago}
              Moneda = {self.moneda}
              Tipo de Pago = {self.tipo_de_pago}
              Fecha = {self.fecha}           
              """)
        
