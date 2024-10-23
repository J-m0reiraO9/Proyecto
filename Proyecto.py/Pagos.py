#Constructor, metodos y atributo de la clase Pagos

class Pagos:
    #Constructor de la clase Pagos
    def __init__(self, pago_cliente, monto, moneda, Tipo_de_pago, fecha):
        self.pago = pago_cliente
        self.monto = monto
        self.moneda = moneda
        self.tipo_de_pago = Tipo_de_pago
        self.fecha = fecha
    
    def show_attr(self):
        print(f"""
              Cliente que realizo el pago = {self.pago}
              Monto = {self.monto}
              Moneda = {self.moneda}
              Tipo de Pago = {self.tipo_de_pago}
              Fecha = {self.fecha}           
              
              """)
        
