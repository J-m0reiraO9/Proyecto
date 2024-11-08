#Constructor, metodos y atributo de la clase Pagos
from dataclasses import dataclass
@dataclass
class Pagos:
    #Constructor de la clase Pagos
    
    pago_cliente: str
    monto: float 
    moneda: str
    tipo_de_pago: str
    fecha: str

    def __init__(self, pago_cliente, monto, moneda, Tipo_de_pago, fecha):
        self.pago_cliente = pago_cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo_de_pago = Tipo_de_pago
        self.fecha = fecha
    
    def show_attr(self):
        print(f"""
              Cliente que realizo el pago = {self.pago_cliente}
              Monto = {self.monto}
              Moneda = {self.moneda}
              Tipo de Pago = {self.tipo_de_pago}
              Fecha = {self.fecha}           
              """)
        
        
