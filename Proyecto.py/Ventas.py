#Constructor, metodos y atributo de la clase Ventas

class Venta:
    #Constructor de la clase Venta
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
    
class Total(Venta):
    def __init__(self, compra, productos, cantidad, pago, envio, Iva, subtotal, IGTF):
        super().__init__(compra, productos, cantidad, pago, envio)
        self.Iva = 0.16
        self.subtotal = subtotal
        self.IGTF = 0.03
