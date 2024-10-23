#Constructor, metodos y atributos de la clase Envio

class Envio:
    #Constructor de la clase Envio
    def __init__(self, orden_compra, servicio_envio, datos_repartidor, costo):
        self.orden = orden_compra
        self.envio = servicio_envio
        self.datos = datos_repartidor
        self.servicio = costo
        
    def show_attr(self):
        print(f"""
              Orden de Compra = {self.orden}
              Servicio de envio = {self.envio}
              Datos del repartidor = {self.datos}
              Costo del Servicio = {self.servicio}
              """)
class Datos:
    def __init__(self, Cliente, Fecha):
        self.cliente = Cliente
        self.fecha = Fecha
